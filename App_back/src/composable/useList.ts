import { api } from 'src/boot/axios';
import { IFormPatient } from 'src/interfaces/IFormPatient';
import { ref } from 'vue';

const list_doctor = ref();
const user_id = Number(sessionStorage.getItem('id'));
const list = async () => {
    return await api.get('client/doctor').then((res) => {
        const docs = res.data.map((data: any) => {
            return {
                value: data.collaborator.id,
                label: `${data.fullname} | Departamento: ${data.collaborator.department}`,
            };
        });

        list_doctor.value = docs;
    });
};

const createAppointment = async (patient: IFormPatient) => {
    patient.client_id = user_id;
    api.post('medical-appointment', patient).then((res) => {
        console.log(res);
    });
};

list();
export const useList = () => ({
    list_doctor,
    createAppointment,
});
