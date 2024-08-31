<template>
  <q-layout class="background--gradiant" view="hHh lpR fFf">
    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>
<style scoped>
.background--gradiant {
  background: linear-gradient(
    113deg,
    #003f91 32.46%,
    rgba(0, 63, 145, 0.47) 62.83%,
    rgba(153, 153, 153, 0.17) 86.64%
  );
}
</style>
