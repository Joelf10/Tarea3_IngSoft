<template>
  <div class="container">
    <template v-if="asignacion">
      <div class="card mt-5 mx-auto" style="width: 400px;">
        <h2 class="card-header">
          Detalles de la cita médica
        </h2>
        <div class="card-body">
          <p>Doctor asignado: {{ asignacion.doctor }}</p>
          <p>Cita programada para el {{ moment(asignacion.fechas[0]).format('D-M-Y') }}</p>
        </div>
        <div class="card-footer">
          <button @click="pacienteStore.eliminarCita" class="btn btn-danger">Eliminar</button>
        </div>
      </div>
    </template>
    <template v-else>
      <div class="card mx-auto mt-5" style="width: 400px;">
        <h2 class="card-header text-center">
          Crear cita
        </h2>
        <form class="card-body" method="post" @submit.prevent="enviarFormulario">
            <p class="form-label">Selecciona una fecha para tu cita:</p>
            <select class="form-select" required v-model="campos.fecha_cita">
              <option :value="moment(i).format('Y-M-D')" v-for="i in general?.fechas_disponibles" :key="i">
                {{ new Date(i).toLocaleDateString() }}
              </option>
            </select>
            
          <p class="form-label mt-2">Selecciona un doctor:</p>
          <select class="form-select" required v-model="campos.doctor">
            <option :value="i.nombre" v-for="i in general?.doctores_disponibles" :key="i.nombre">
              {{ i.nombre }}
            </option>
          </select>            
          <button class="btn btn-primary mt-3 w-100" type="submit" :disabled="cargando">Programar cita</button>
        </form>
      </div>
    </template>
  </div>
</template>

<script setup lang="ts">
import { useAutenticacionStore } from "@/stores/autenticacion";
import { usePacienteStore } from "@/stores/paciente";
import { storeToRefs } from "pinia";
import {onBeforeMount, ref, reactive} from "vue";
import moment from "moment";


const autenticacionStore = useAutenticacionStore();
const pacienteStore = usePacienteStore();
const {general, asignacion} = storeToRefs(pacienteStore)

const cargando = ref(false)
const campos = reactive({
  fecha_cita: '',
  doctor: ''
})

const enviarFormulario = async()=>{
  cargando.value = true;
  await pacienteStore.crearCita(autenticacionStore.usuarioActual!.nombre, campos)
  cargando.value = false;
  campos.doctor = ''
  campos.fecha_cita = ''
  
}

onBeforeMount(async()=>{
  await pacienteStore.consultarCita(autenticacionStore.usuarioActual!.nombre)
  await pacienteStore.getDatosGenerales()
})

</script>

<style scoped>

</style>