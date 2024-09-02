<template>
    <q-page padding class="row justify-center items-center">
        <q-card
            style="width: 1080px; height: 650px; border-radius: 16px"
            class="my-card row justify-around items-center"
        >
            <Transition name="slide-fade">
                <q-img
                    class="absolute-left transition__image"
                    :src="imageResult"
                    height="650px"
                    :style="{
                        'z-index': 1,
                        'border-radius':
                            border[0] +
                            'px ' +
                            border[1] +
                            'px ' +
                            border[2] +
                            'px ' +
                            border[3] +
                            'px ',
                        transform: `translateX(${imagePosition})`,
                        'max-width': 540 + 'px',
                    }"
                />
            </Transition>
            <div class="col-5">
                <q-form v-if="registerFormActive" class="">
                    <div class="q-pb-md">
                        <span class="text-h4" style="font-weight: 600"
                            >Registrate</span
                        >
                        <p class="text-subtitle1">
                            Ingresa los siguientes datos
                        </p>
                    </div>
                    <div class="row q-py-md">
                        <div class="col-12 q-py-md">
                            <q-input
                                v-model="fullname"
                                outlined
                                type="text"
                                label="Nombre Completo"
                            />
                        </div>
                        <div class="col-12 q-py-md">
                            <q-input
                                v-model="dni"
                                outlined
                                type="text"
                                label="Cedula"
                            />
                        </div>
                        <div class="col-12 q-py-md">
                            <q-input
                                v-model="email"
                                outlined
                                type="text"
                                label="Email"
                            />
                        </div>
                        <div class="col-12 q-py-md">
                            <q-input
                                v-model="password"
                                outlined
                                type="password"
                                label="Password"
                            />
                        </div>
                        <div class="col-12 q-py-md">
                            <q-checkbox
                                v-model="terms"
                                label="Acepto terminos y condiciones"
                            />
                        </div>
                    </div>
                    <q-card-actions class="q-px-none" align="between">
                        <q-btn
                            :disabled="!terms"
                            label="Sign Up"
                            color="primary"
                            class="col-12 button__style"
                            @click="
                                userStore
                                    .register({
                                        fullname,
                                        email,
                                        password,
                                        dni,
                                    })
                                    .then((data) => {
                                        $q.notify({
                                            message: data.message,
                                            color: 'positive',
                                            position: 'top',
                                        });
                                        imagePosition = 0 + '%';
                                        border = [16, 0, 0, 16];
                                        registerFormActive = false;
                                        loginFormActive = true;
                                        fullname = '';
                                        email = '';
                                        password = '';
                                    })
                                    .catch((error) => {
                                        console.log(error);
                                    })
                            "
                        />
                    </q-card-actions>
                </q-form>
            </div>
            <div class="col-5 q-pa-md">
                <q-form v-if="loginFormActive" class="">
                    <div class="q-pb-md">
                        <span class="text-h4" style="font-weight: 600"
                            >Bienvenido</span
                        >
                        <p class="text-subtitle1">
                            Ingresa tu correo y contraseña para iniciar sesión
                        </p>
                    </div>
                    <div class="row q-py-md">
                        <div class="col-12 q-py-md">
                            <q-input
                                v-model="email"
                                outlined
                                type="text"
                                label="Email"
                            />
                        </div>
                        <div class="col-12 q-py-md">
                            <q-input
                                v-model="password"
                                outlined
                                type="password"
                                label="Password"
                            />
                        </div>
                    </div>
                    <q-card-actions class="q-px-none" align="between">
                        <q-btn
                            label="Login"
                            color="primary"
                            class="col-5 button__style"
                            @click="
                                userStore
                                    .access({ email, password })
                                    .then((data) => {
                                        $q.notify({
                                            message: data.message,
                                            color: 'positive',
                                            position: 'top',
                                        });
                                        $router.push('/patient');
                                    })
                                    .catch((err) => {
                                        $q.notify({
                                            message: err.message,
                                            color: 'negative',
                                            position: 'top',
                                        });
                                    })
                            "
                        />
                        <q-btn
                            label="Sign Up"
                            color="primary"
                            outline
                            class="col-5 button__style"
                            @click="
                                (imagePosition = 100 + '%'),
                                    (border = [0, 16, 16, 0]),
                                    (imageResult = imagePaths[1]),
                                    (registerFormActive = true),
                                    (loginFormActive = false)
                            "
                        />
                    </q-card-actions>
                </q-form>
            </div>
        </q-card>
    </q-page>
</template>

<script>
import { defineComponent, ref } from 'vue';
import { useUserStore } from '../stores/user';

export default defineComponent({
    name: 'AuthPage',
    setup() {
        const border = ref([16, 0, 0, 16]);
        const imagePosition = ref(0);
        const imagePaths = ref([
            'src/assets/login.svg',
            'src/assets/register.svg',
        ]);
        const imageResult = ref('src/assets/login.svg');
        const registerFormActive = ref(false);
        const loginFormActive = ref(true);

        const userStore = useUserStore();

        const fullname = ref('');
        const email = ref('');
        const password = ref('');
        const dni = ref('');
        const terms = ref(false);

        return {
            border,
            imagePosition,
            imagePaths,
            imageResult,
            loginFormActive,
            registerFormActive,
            fullname,
            email,
            password,
            terms,
            userStore,
            dni,
        };
    },
});
</script>

<style scoped>
.button__style {
    height: 50px;
    border-radius: 8px;
}

.transition__image {
    transition: transform 1s ease;
}
</style>
