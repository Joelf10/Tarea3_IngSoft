<template>
    <q-page padding>
        <div class="q-pa-md">
            <div class="form-small__blue"></div>
            <div class="absolute title">
                <div class="q-pb-md">
                    <span class="text-h2 text-weight-regular">Bienvenido!</span>
                </div>
                <div class="q-py-md text-center">
                    <p class="text-h5 text-weight-light">
                        Revisa tus citas pendientes en el calendario
                    </p>
                </div>
            </div>
            <div class="q-pa-md column absolute card-select">
                <div class="q-py-lg text-center">
                    <q-date style="width: 28vw; height: 24vw" v-model="days" />
                </div>
                <q-card-actions class="q-py-xl" align="center">
                    <q-btn
                        style="
                            width: 270px;
                            height: 75px;
                            border-radius: 45px;
                            font-size: 22px;
                        "
                        icon="fa fa-plus"
                        no-caps
                        color="positive"
                        label="Nuevo Horario"
                        class="q-mr-md text-weight-regular"
                        @click="openDialog()"
                    />
                </q-card-actions>
            </div>
            <div class="col-6 form-big__blue text-center">
                <q-img
                    style="max-width: 502px; max-height: 579px"
                    src="../assets/doctor.svg"
                    spinner-color="primary"
                    spinner-size="82px"
                />
            </div>
        </div>
    </q-page>
</template>
<script>
import { ref } from 'vue';
import FormDoctorDialog from 'src/components/FormDoctorDialog.vue';
import { useQuasar } from 'quasar';

export default {
    setup() {
        const $q = useQuasar();
        return {
            days: ref(['2023/01/01']),
            date: ref(''),
            tab: ref('one'),
            openDialog: () => {
                $q.dialog({
                    component: FormDoctorDialog,
                });
            },
        };
    },
};
</script>
<style scoped>
.form-small__blue {
    position: absolute;
    top: 0;
    left: 0;
    border-radius: 0px 0px 50px 0px;
    width: 110px;
    height: 177px;
    background-color: #003f91;
}
.form-big__blue {
    position: absolute;
    top: 0;
    right: 0;
    border-radius: 0px 0px 0px 50px;
    width: 30vw;
    background-color: #003f91;
}
.card-select {
    top: 25%;
    left: 15%;
}
.title {
    top: 10%;
    left: 10%;
}
</style>
