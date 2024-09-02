<template>
    <q-layout view="hHh lpR fFf">
        <q-header style="height: 60px; border-radius: 0px 0px 16px 16px" reveal>
            <q-toolbar
                class="bg-primary text-white"
                style="height: 60px; border-radius: 0px 0px 16px 16px"
            >
                <q-btn flat round dense icon="assignment_ind" />
                <q-toolbar-title> Medical Office </q-toolbar-title>
                <q-btn
                    icon-right="fa-solid fa-right-from-bracket"
                    label="Salir"
                    color="secondary"
                    class="q-ma-md"
                    @click="logout()"
                />
            </q-toolbar>
        </q-header>
        <q-page-container>
            <router-view />
        </q-page-container>
    </q-layout>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
    name: 'MainLayout',
    setup() {
        const logout = () => {
            sessionStorage.clear();
            location.reload();
        };
        return { logout };
    },
});
</script>
