<template>
    <q-page padding>
        <q-table
            title="Historial de Citas"
            :rows="row"
            :columns="columns"
            row-key="name"
        />
    </q-page>
</template>

<script>
import { defineComponent, ref } from 'vue';
import { useUser } from 'src/composable/user';
import historyGeneralTable from 'src/data/historyGeneralTable';

export default defineComponent({
    name: 'HistorialPage',
    setup() {
        const columns = ref(historyGeneralTable);
        const { row } = useUser();
        return { row, columns };
    },
});
</script>
