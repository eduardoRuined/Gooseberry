<script setup>
    import { ref } from 'vue';
    import {useRouter} from 'vue-router';
    import { useAuthStore } from '../stores/auth';

    const username=ref('')
    const password=ref('')
    const error=ref(null)
    const auth=useAuthStore()
    const router=useRouter()

    async function handleSubmit() {
        error.value=null
        try{
            await auth.login(username.value,password.value)
            router.push('/')
        }
        catch(err){
            error.value='Usuario o contraseña incorrectos'
        }
    }
</script>

<template>
    <div class="login">
        <h1>Iniciar sesion</h1>
        <form @submit.prevent="handleSubmit">
            <input v-model="username" type="text" placeholder="Usuario"/>
            <input v-model="password" type="password", placeholder="Contraseña"/>
            <button type="submit">Entrar</button>
        </form>
        <p v-if="error" class="error">{{ error }}</p>
    </div>
</template>

<style scoped>
    .login{
        max-width: 300px;
        margin: 60px auto;
        display: flex;
        flex-direction: column;
        gap: 12px;
    }
    form{
        display: flex;
        flex-direction: column;
        gap: 12px;
    }
    input{
        padding: 10px;
        border-radius: 4px;
        border: 1px solid #333;
        background: #121212;
        color: #fff;
    }
    button{
        background: #1db954;
        color: #000;
        border: none;
        border-radius: 20px;
        padding: 10px;
        font-weight: 600;
        cursor: pointer;
    }
    .error{
        color: #f15e6c;
    }

</style>