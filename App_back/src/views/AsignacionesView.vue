<template>
  <div class="container">
    <h1 class="text-center">Consultas</h1>
    <table class="table">
      <thead>
        <tr>
          <th scope="col">Doctor</th>
          <th scope="col">Paciente</th>
          <th scope="col">Fechas</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(i,j) in asignaciones" :key="j">
          <td>{{ i.doctor }}</td>
          <td>{{j}}</td>
          <td>{{ new Date(i.fechas[0]).toLocaleDateString() }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup lang="ts">
import { usePacienteStore } from '@/stores/paciente';
import { storeToRefs } from 'pinia';
import { onBeforeMount } from 'vue';

const pacienteStore = usePacienteStore()
const {asignaciones} = storeToRefs(pacienteStore)

onBeforeMount(async()=>{
  await pacienteStore.obtenerAsignaciones()
})
</script>

<style scoped>

</style>