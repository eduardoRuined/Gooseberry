import os
import re 
from django.http import StreamingHttpResponse,Http404 
from django.conf import settings
from rest_framework.decorators import api_view
from .models import Song

range_re= re.compile(r'bytes\s*=(\d+)\s*-\s*(\d*)', re.I)

def stream_file(request, file_path):
    if not os.path.exists(file_path):
        raise Http404('Archivo no encontrado')

    file_size= os.path.getsize(file_path)
    range_header=request.META.get('HTTP_RANGE', '').strip()
    range_match=range_re.match(range_header)

    if range_match:
        first_byte= int(range_match.group(1))
        last_byte= range_match.group(2)
        last_byte= int(last_byte) if last_byte else file_size - 1
        last_byte= min(last_byte, file_size-1)
        length= last_byte-first_byte+1

        with open(file_path, 'rb') as f:
            f.seek(first_byte)
            data= f.read(length)

        response=StreamingHttpResponse(
            iter([data]),
            status=206,
            content_type='audio/mpeg'
        )
        response['Content-Length']= str(length)
        response['Content-Range']=f'bytes {first_byte}-{last_byte}/{file_size}'
    else:
        with open(file_path, 'rb') as f:
            data= f.read()
        response= StreamingHttpResponse(
            iter({data}),
            content_type='audio/mpeg'
        )
        response['Content-Length']=str(file_size)

    response['Accept-Ranges']='bytes'
    return response

@api_view(['GET'])
def stream_song(request, song_id):
    try:
        song=Song.objects.get(id=song_id)
    except Song.DoesNotExist:
        raise Http404('Canción no encontrada')

    file_path= song.audio_file.path
    return stream_file(request,file_path)