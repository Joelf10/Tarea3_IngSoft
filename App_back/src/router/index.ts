import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/LoginView.vue'
import { useAutenticacionStore } from '@/stores/autenticacion';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'login',
      component: HomeView
    },
    {
      path: '/paciente/cita',
      name: 'pacienteCita',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/CitaView.vue')
    },
    {
      path: '/registro-normal',
      name: 'registroNormal',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/RegistroNormalView.vue')
    },
    {
      path: '/registro-doctor',
      name: 'registroDoctor',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/RegistroDoctorView.vue')
    },
    {
      path: '/doctor/asignaciones',
      name: 'doctorAsignaciones',
      component: () => import('../views/AsignacionesView.vue')
    }
  ]
})

router.beforeEach((to, from, next) => {
  const {usuarioActual} = useAutenticacionStore()

  if (usuarioActual === null && (to.path.startsWith('/paciente') || to.path.startsWith('/doctor'))) {
    next('/');
  } else {
    // Permitir el acceso a la ruta
    next();
  }
});

export default router
