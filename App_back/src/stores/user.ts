import { api } from 'boot/axios';
import { defineStore } from 'pinia';
import { Ref, ref } from 'vue';

export const useUserStore = defineStore('user', () => {
    const token: Ref<string | null> = ref(null);
    const client = ref();
    const access = ({
        email,
        password,
    }: {
        email: string;
        password: string;
    }) => {
        return new Promise((resolve, reject) => {
            api.post('auth/login', { email, password })
                .then((response) => {
                    token.value = response.data.token;
                    client.value = response.data;
                    sessionStorage.setItem('token', String(token.value));
                    sessionStorage.setItem('email', String(client.value.email));
                    sessionStorage.setItem('role', String(client.value.role));
                    sessionStorage.setItem('id', String(client.value.id));
                    resolve({ message: 'Se ha logueado' });
                })
                .catch((err) => {
                    if (err.message === 'password is wrong') {
                        reject({ message: 'Contraseña incorrecta' });
                    } else {
                        reject({ message: 'Ha ocurrido un problema' });
                    }
                });
        });
    };

    const register = async ({
        fullname,
        email,
        password,
        dni,
    }: {
        fullname: string;
        email: string;
        password: string;
        dni: string;
    }) => {
        return new Promise((resolve, reject) => {
            api.post('auth/register', { fullname, email, password, dni })
                .then(() => {
                    resolve({ message: 'Se ha registrado con exito' });
                })
                .catch(() => {
                    reject({
                        message: 'No se ha podido loguear vuelva a intentarlo',
                    });
                });
        });
    };
    return {
        token,
        client,
        access,
        register,
    };
});
