const routes = [
  {
    path: "/auth",
    component: () => import("layouts/AuthLayout.vue"),
    children: [{ path: "", component: () => import("pages/AuthPage.vue") }],
  },
  {
    path: "",
    component: () => import("layouts/MainLayout.vue"),
    meta: {
      requireAuth: true,
    },
    children: [
      {
        path: "patient",
        component: () => import("pages/IndexPage.vue"),
      },
      {
        path: "history",
        component: () => import("pages/HistorialPacientePage.vue"),
      },
    ],
  },
  {
    path: "",
    component: () => import("layouts/DoctorLayout.vue"),
    children: [
      { path: "doctor", component: () => import("pages/DoctorPage.vue") },
    ],
  },
  // Catch all unmatched routes
  {
    path: "/:catchAll(.*)*",
    component: () => import("pages/ErrorNotFound.vue"),
  },
];

export default routes;
