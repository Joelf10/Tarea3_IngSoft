<template>
    <q-dialog ref="dialogRef" @hide="onDialogHide" style="width: 900px">
        <q-card class="q-dialog-plugin q-pa-md" style="border-radius: 16px">
            <q-card-section>
                <span class="text-h5">Crear Cita</span>
            </q-card-section>
            <q-card-section>
                <q-form class="">
                    <div class="row">
                        <div class="col-12 q-pa-md">
                            <q-select
                                v-model="patient.collaborator_id"
                                type="text"
                                :options="list_doctor"
                                label="Doctores"
                                emit-value
                                map-options
                            />
                        </div>
                        <div class="col-12 q-pa-md">
                            <q-input
                                v-model="patient.appointment_date"
                                label="Fecha"
                                mask="date"
                            >
                                <template v-slot:append>
                                    <q-icon name="event" class="cursor-pointer">
                                        <q-popup-proxy
                                            cover
                                            transition-show="scale"
                                            transition-hide="scale"
                                        >
                                            <q-date
                                                v-model="
                                                    patient.appointment_date
                                                "
                                            >
                                                <div
                                                    class="row items-center justify-end"
                                                >
                                                    <q-btn
                                                        v-close-popup
                                                        label="Close"
                                                        color="primary"
                                                        flat
                                                    />
                                                </div>
                                            </q-date>
                                        </q-popup-proxy>
                                    </q-icon>
                                </template>
                            </q-input>
                        </div>
                        <div class="col-12 q-pa-md">
                            <q-input
                                label="Horario"
                                v-model="patient.appointment_time"
                            >
                                <template v-slot:append>
                                    <q-icon
                                        name="access_time"
                                        class="cursor-pointer"
                                    >
                                        <q-popup-proxy
                                            cover
                                            transition-show="scale"
                                            transition-hide="scale"
                                        >
                                            <q-time
                                                v-model="
                                                    patient.appointment_time
                                                "
                                            >
                                                <div
                                                    class="row items-center justify-end"
                                                >
                                                    <q-btn
                                                        v-close-popup
                                                        label="Close"
                                                        color="primary"
                                                        flat
                                                    />
                                                </div>
                                            </q-time>
                                        </q-popup-proxy>
                                    </q-icon>
                                </template>
                            </q-input>
                        </div>
                    </div>
                </q-form>
            </q-card-section>
            <q-card-actions align="right">
                <q-btn
                    style="border-radius: 8px"
                    color="positive"
                    label="Agendar"
                    @click="onOKClick"
                    class="q-mr-lg text-weight-regular"
                    no-caps
                />
                <q-btn
                    style="border-radius: 8px; color: #757575"
                    outline
                    label="Cancelar"
                    class="text-weight-regular"
                    no-caps
                    @click="onCancelClick"
                />
            </q-card-actions>
        </q-card>
    </q-dialog>
</template>
<script lang="ts">
import { useDialogPluginComponent } from 'quasar';
import { useList } from 'src/composable/useList';
import { IFormPatient } from 'src/interfaces/IFormPatient';
import { PropType, ref, Ref } from 'vue';

export default {
    name: 'FormPatient',
    emits: [...useDialogPluginComponent.emits],

    setup(props) {
        const { dialogRef, onDialogHide, onDialogOK, onDialogCancel } =
            useDialogPluginComponent();
        const patient: Ref<IFormPatient> = ref({ ...props.data });
        const { list_doctor } = useList();

        return {
            dialogRef,
            onDialogHide,
            patient,
            list_doctor,
            onOKClick() {
                onDialogOK(patient);
            },
            onCancelClick: onDialogCancel,
        };
    },
    props: {
        data: { type: Object as PropType<IFormPatient>, required: false },
    },
};
</script>
