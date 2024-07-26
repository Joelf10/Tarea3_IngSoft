<template>
  <main class="container-fluid centrar">
    <div class="mx-auto" style="width: 400px;">
      <div class="card">
        <h2 class="card-header text-center">Login</h2>
        <form class="card-body" @submit.prevent="enviarFormulario">
          <input 
            class="form-control"
            type="text" 
            v-model="campos.nombre"
            placeholder="Nombre"
            required>
          <input 
            class="form-control mt-2"
            type="password"
            v-model="campos.password"
            placeholder="Contraseña"
            required>
          <button 
            class="btn btn-primary w-100 mt-3"
            :disabled="cargando"
            type="submit">
            Ingresar
          </button>
          <a href="/registro-normal">Registro pacientes</a> <br>
          <a href="/registro-doctor">Registro doctores</a>
        </form>
      </div>
    </div>
  </main>
</template>

<script setup lang="ts">
import { useAutenticacionStore } from "@/stores/autenticacion";
import {reactive, ref} from "vue";

const cargando = ref(false)
const campos = reactive({
  nombre: '',
  password: ''
})

const {login} = useAutenticacionStore()

const enviarFormulario = async()=>{
  cargando.value = true;
  await login(campos);
  cargando.value = false;
}

</script>

<style scoped>
.centrar{
  height: 100vh;
  display: flex;
  align-items: center;
}
</style>