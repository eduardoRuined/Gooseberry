import { defineStore } from "pinia";
import { ref } from "vue";
import api from  '../services/api';

export const useAuthStore=defineStore('auth',()=>{
    const token=ref(localStorage.getItem('access_token'))
    const isAuthenticated=ref(!!token.value)
    async function login(username,password) {
        const response= await api.post('/token/',{username,password})
        token.value=response.data.access 
        localStorage.setItem('access_token',response.data.access)
        localStorage.setItem('refresh_token',response.data.refresh)
        isAuthenticated.value=true
    }
    function logout(){
        token.value=null 
        isAuthenticated.value= false
        localStorage.removeItem('access_token')
        localStorage.removeItem('refresh_token')
    }
    return{token,isAuthenticated,login,logout}
})
