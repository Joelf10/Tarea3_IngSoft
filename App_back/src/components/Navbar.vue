<template>
  <header>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">
          {{usuarioActual ? `Bienvenido ${usuarioActual.nombre}`:'App Citas Médicas'}}
        </a>
        <button 
          v-if="usuarioActual"
          @click="autenticacionStore.salir"
          class="ml-auto me-3 btn btn-danger">Salir</button>
      </div>
    </nav>
  </header>
</template>

<script setup lang="ts">
import { useAutenticacionStore } from '@/stores/autenticacion';
import { storeToRefs } from 'pinia';

const autenticacionStore = useAutenticacionStore()
const {usuarioActual} = storeToRefs(autenticacionStore)
</script>

<style scoped>

</style>