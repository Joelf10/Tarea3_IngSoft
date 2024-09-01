<template>
    <q-card class="my-card q-ma-md" style="" bordered>
        <q-card-section :horizontal="!$q.screen.lt.lg">
            <q-img
                style=" min-height: 250px"
                :src="propsObject.imgPath"
            ></q-img>
            <q-card-section>
                <q-card-section>
                    <div class="text-h6">{{ propsObject.title }}</div>
                </q-card-section>
                <q-card-section>
                    {{ propsObject.description }}
                </q-card-section>
                <q-card-actions align="right">
                    <q-btn
                        v-if="propsObject.openPatient"
                        color="positive"
                        icon-right="fa-solid fa-arrow-right"
                        :label="propsObject.labelButton"
                        style="border-radius: 45px"
                        @click="propsObject.openPatient()"
                        class="col-5"
                    />
                    <q-btn
                        v-else
                        color="positive"
                        icon-right="fa-solid fa-arrow-right"
                        :label="propsObject.labelButton"
                        style="border-radius: 45px"
                        :to="propsObject.to"
                        class="col-5"
                    />
                </q-card-actions>
            </q-card-section>
        </q-card-section>
    </q-card>
</template>
<script>
import { defineComponent } from 'vue';

export default defineComponent({
    name: 'PatientActionComponent',
    props: {
        propsObject: { type: Object, required: true },
    },
    setup() {
        return {};
    },
});
</script>
