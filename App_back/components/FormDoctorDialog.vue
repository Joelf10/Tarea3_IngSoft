<template>
    <q-dialog ref="dialogRef" @hide="onDialogHide" style="width: 900px">
        <q-card
            class="q-dialog-plugin"
            style="width: 500px; max-width: 80vw; border-radius: 20px"
        >
            <q-card-section>
                <span class="text-h5">Crear Horario</span>
            </q-card-section>
            <q-card-section>
                <q-form class="">
                    <div class="row">
                        <div class="col-12 q-pa-md">
                            <q-input
                                v-model="text"
                                type="text"
                                label="Cedula"
                            />
                        </div>
                        <div class="col-12 q-pa-md">
                            <q-input v-model="date" label="Fecha" mask="date">
                                <template v-slot:append>
                                    <q-icon name="event" class="cursor-pointer">
                                        <q-popup-proxy
                                            cover
                                            transition-show="scale"
                                            transition-hide="scale"
                                        >
                                            <q-date v-model="date">
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
                            <q-input label="Horario" v-model="time">
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
                                            <q-time v-model="time">
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
                    @click="onDialogCancel"
                    no-caps
                />
            </q-card-actions>
        </q-card>
    </q-dialog>
</template>
<script>
import { useDialogPluginComponent } from 'quasar';
import { ref } from 'vue';

export default {
    name: 'FormDoctor',
    emits: [...useDialogPluginComponent.emits],

    setup() {
        const { dialogRef, onDialogHide, onDialogOK, onDialogCancel } =
            useDialogPluginComponent();

        const dni = ref();

        return {
            dialogRef,
            onDialogHide,
            onOKClick() {
                onDialogOK();
            },
            onCancelClick: onDialogCancel,
            dni,
        };
    },
};
</script>
