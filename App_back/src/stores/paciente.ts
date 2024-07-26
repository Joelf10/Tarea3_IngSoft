import { defineStore } from 'pinia'
import { API } from '@/constant'
import router from '@/router'

interface IGeneral{
  doctores_disponibles:{
    nombre: string
  }[],
  fechas_disponibles: string[]
}

interface IState{
  asignacion: null | any,
  general: null | IGeneral,
  asignaciones: any
}

export const usePacienteStore = defineStore('paciente', {
  state:():IState=>(
    {
      asignacion: null,
      general: null,
      asignaciones: {}
    }
  ),
  actions: {
    async getDatosGenerales(){
      try {
        const respuesta = await fetch(`${API}/api/datos-citas`);
        const json = await respuesta.json()
        this.general = json
      } catch (error) {
        console.log(error);        
      }
    },
    async consultarCita(usuario: string){
      try {
        const response = await fetch(`${API}/api/citas/${usuario}`);
        const json = await response.json()
        if(response.status == 200){
          this.asignacion = json
        }
      } catch (error) {
        console.log(error);        
      }
    },
    async crearCita(usuario: string, body:{fecha_cita: string, doctor: string}){
      try {
        const response = await fetch(`${API}/api/citas/${usuario}`,
          {
            method: 'POST',
            headers:{
              'Content-Type': 'application/json'
            },
            body: JSON.stringify(body)
          }
        );
        this.asignacion = await response.json()
      } catch (error) {
        console.log(error);        
      }
    },
    async eliminarCita(usuario: string){
      try {
        const response = await fetch(`${API}/api/citas/${usuario}`,{method:'DELETE'});
        if(response.status === 200){
          this.asignacion = null;
        }    
      } catch (error) {
        console.log(error);        
      }
    },
    async obtenerAsignaciones(){
      try {
        const response = await fetch(`${API}/api/asignaciones`);
        if(response.status === 200){
          this.asignaciones = (await response.json()).asignaciones;
        }
      } catch (error) {
        console.log(error);
      }
    }
  }
})