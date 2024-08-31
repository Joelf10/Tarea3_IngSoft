/* eslint-disable @typescript-eslint/no-explicit-any */
import { api } from 'src/boot/axios';
import { useUserStore } from 'src/stores/user';
import { ref } from 'vue';

const row = ref();
const store = useUserStore();
const data = (currentemail: string) => {
    return new Promise((resolve, reject) => {
        api.get('client/' + currentemail, {
            headers: {
                Authorization: `Bearer ${String(
                    sessionStorage.getItem('token')
                )}`,
            },
        })
            .then((response) => {
                resolve(response.data);
            })
            .catch((err) => {
                reject(err);
            });
    });
};
data(String(sessionStorage.getItem('email')))
    .then((res: any) => {
        row.value = res.data.appointments;
    })
    .catch((err) => {
        console.log(err);
    });

export const useUser = () => ({
    data,
    row,
});
