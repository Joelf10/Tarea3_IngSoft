import moment from 'moment';
import { h } from 'vue';

const getIcon = (val: any) => {
    if (val === null) {
        return h('i', {
            class: 'q-icon text-warning fa-solid fa-clock',
            style: 'font-size: 24px',
        });
    }
    if (val === true) {
        return h('i', {
            class: 'q-icon text-positive fa-solid fa-check',
            style: 'font-size: 24px',
        });
    }
    if (val === false) {
        return h('i', {
            class: 'q-icon text-negative fa-solid fa-xmark',
            style: 'font-size: 24px',
        });
    }
};

/* eslint-disable @typescript-eslint/no-explicit-any */
export default [
    {
        name: 'department',
        field: (data: any) => data.collaborator.department,
        label: 'Departamento',
        sortable: true,
        align: 'left',
    },
    {
        name: 'date_appointment',
        field: (data: any) =>
            moment(data.appointment_date).format('DD/MM/YYYY'),
        label: 'Fecha de Cita',
        sortable: true,
        align: 'center',
    },
    {
        name: 'hour_appointment',
        field: (data: any) => moment(data.appointment_date).format('HH:mm'),
        label: 'Hora de Cita',
        sortable: true,
        align: 'center',
    },
    {
        name: 'appointment_state',
        field: 'appointment_state',
        format: (val: any) => getIcon(val),
        label: 'Estado',
        sortable: true,
        align: 'center',
    },
];
