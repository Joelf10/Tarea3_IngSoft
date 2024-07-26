import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { API } from '@/constant'
import { useRouter } from 'vue-router'
import router from '@/router'

interface Usuario{
  nombre: string
  rol: string
}

interface IState{
  usuarioActual: Usuario | null
}

export const useAutenticacionStore = defineStore('autenticacion', {
  state:():IState=>(
    {
      usuarioActual: null
    }
  ),
  actions: {
    async login(body:{nombre:string, password:string}){
      try {
        const response = await fetch(`${API}/api/login`,
          {
            method: 'POST',
            headers:{
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({
              nombre: body.nombre,
              'contraseña': body.password
            })
          }
        );
        if(response.status == 200){
          const json = await response.json()
          this.usuarioActual = json;
          if(json.rol !== 'doctor'){
            router.push('/paciente/cita')
          }else{
            router.push('/doctor/asignaciones')
          }
        }else{
          alert('Credenciales incorrectas!')
        }
      } catch (error) {
        console.log(error);        
      }
    },
    async registroNormal(body:{nombre:string, password:string, cedula: string, fecha_nacimiento: string}){
      try {
        const response = await fetch(`${API}/api/registro`,
          {
            method: 'POST',
            headers:{
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({
              nombre: body.nombre,
              'contraseña': body.password,
              cedula: body.cedula,
              fecha_nacimiento: body.fecha_nacimiento
            })
          }
        );
        if(response.status == 200){
          router.push('/')
        }
      } catch (error) {
        console.log(error);        
      }
    },
    async registroDoctor(body:{nombre:string, password:string}){
      try {
        const response = await fetch(`${API}/api/registro_doctor`,
          {
            method: 'POST',
            headers:{
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({
              nombre: body.nombre,
              'contraseña': body.password
            })
          }
        );
        if(response.status == 200){
          await response.json()
          router.push('/')
        }
      } catch (error) {
        console.log(error);        
      }
    },
    salir(){
      this.usuarioActual = null;
      router.push('/')
    }
  }
})