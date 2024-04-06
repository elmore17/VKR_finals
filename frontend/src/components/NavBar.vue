<script setup>
import { onMounted } from 'vue'
import { initFlowbite } from 'flowbite'
// initialize components based on data attribute selectors
onMounted(() => {
    initFlowbite();
});
</script>

<template>
    <nav class="container mx-auto flex flex-row justify-between items-end">
        <div class="flex flex-row items-end">
            <img src="/BlackLogo.svg" class="logo mt-7" alt="kis logo black" />
            <button class="textnavbutton rounded-xl h-6 w-auto font-semibold text-xs mb-4">
                <router-link class="pl-2 pr-2 pt-1 pb-1" to='/kafedr'>ГЭК</router-link>
            </button>
            <div class="mb-4 ml-3 mr-3 linenav font-semibold">/</div>
            <button id="dropdownDefaultButton" data-dropdown-toggle="dropdown"
                class="text-white font-medium rounded-lg text-sm text-center inline-flex items-center mb-4"
                type="button">
                <div class="textnavbutton rounded-full h-5 w-5 me-2">
                    <img src="/iconfornavbar.svg" class="px-1 py-1" alt="kis logo black" />
                </div>
                Формирование списков
                <svg class="w-2.5 h-2.5 ms-3 cursordrop" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"
                    fill="none" viewBox="0 0 10 6">
                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="m1 1 4 4 4-4" />
                </svg>
            </button>

            <!-- Dropdown menu navbar-->
            <div id="dropdown"
                class="z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow w-44 dark:bg-gray-700">
                <ul class="py-2 text-sm text-gray-700 dark:text-gray-200" aria-labelledby="dropdownDefaultButton">
                    <li>
                        <a data-modal-target="AddCommissionPeople" data-modal-toggle="AddCommissionPeople"
                            class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white cursor-pointer">Добавление
                            челенов комиссии</a>
                    </li>
                </ul>
            </div>
        </div>
        <div>
            <button id="dropdownAvatarNameButton" data-dropdown-toggle="dropdownAvatarName"
                class="flex items-center text-sm pe-1 font-medium text-white mb-4" type="button">
                {{ UserLogin }}
                <svg class="w-2.5 h-2.5 ms-3 cursordrop" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"
                    fill="none" viewBox="0 0 10 6">
                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="m1 1 4 4 4-4" />
                </svg>
            </button>

            <!-- Dropdown menu profile-->
            <div id="dropdownAvatarName"
                class="z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow w-44 dark:bg-gray-700 dark:divide-gray-600">
                <div class="px-4 py-3 text-sm text-gray-900 dark:text-white">
                    <div class="font-medium ">{{ UserName }}</div>
                </div>
                <ul class="py-2 text-sm text-gray-700 dark:text-gray-200"
                    aria-labelledby="dropdownInformdropdownAvatarNameButtonationButton">
                    <li>
                        <a data-modal-target="settings" data-modal-toggle="settings"
                            class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white cursor-pointer">Настройки</a>
                    </li>
                </ul>
                <div class="py-2">
                    <a class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white cursor-pointer"
                        @click.prevent="logOut">Выход</a>
                </div>
            </div>
        </div>
    </nav>

    <div id="settings" tabindex="-1" aria-hidden="true"
        class="hidden overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full">
        <div class="relative p-4 w-full max-w-2xl max-h-full">
            <!-- Modal content -->
            <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">
                <!-- Modal header -->
                <div class="flex items-center justify-between p-4 md:p-5 border-b rounded-t dark:border-gray-600">
                    <h3 class="text-xl font-semibold text-gray-900 dark:text-white">
                        Обновление
                    </h3>
                    <button type="button"
                        class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white"
                        data-modal-hide="settings">
                        <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none"
                            viewBox="0 0 14 14">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6" />
                        </svg>
                        <span class="sr-only">Close modal</span>
                    </button>
                </div>
                <!-- Modal body -->
                <div class="p-4 md:p-5 space-y-4">
                    <input v-model="newfio" type="text" placeholder="Новое ФИО"
                        class="mt-1 mb-1 font-sans w-80 border-none bg-gray-100 p-3 rounded">
                </div>
                <!-- Modal footer -->
                <div class="flex items-center p-4 md:p-5 border-t border-gray-200 rounded-b dark:border-gray-600">
                    <button data-modal-hide="settings" type="button"
                        class="text-white tbg focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center"
                        @click="settingadmin">Принять</button>
                    <button data-modal-hide="settings" type="button"
                        class="py-2.5 px-5 ms-3 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700">Отмена</button>
                </div>
            </div>
        </div>
    </div>
    <!-- Main modal -->
    <div id="AddCommissionPeople" tabindex="-1" aria-hidden="true"
        class="hidden overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full">
        <div class="relative p-4 w-full max-w-2xl max-h-full">
            <!-- Modal content -->
            <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">
                <!-- Modal header -->
                <div class="flex items-center justify-between p-4 md:p-5 border-b rounded-t dark:border-gray-600">
                    <h3 class="text-xl font-semibold text-gray-900 dark:text-white">
                        Добавление членов комиссии
                    </h3>
                    <button type="button"
                        class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white"
                        data-modal-hide="AddCommissionPeople">
                        <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none"
                            viewBox="0 0 14 14">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6" />
                        </svg>
                        <span class="sr-only">Close modal</span>
                    </button>
                </div>
                <!-- Modal body -->
                <div class="p-4 md:p-5 space-y-4 max-h-96 overflow-auto">
                    <button v-if="UsersCommission.length <= 11" data-modal-hide="AddCommissionPeople"
                        data-modal-target="formaddcommission" data-modal-toggle="formaddcommission"
                        class="text-white tbg focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center">Добавить</button>
                    <div class="relative overflow-x-auto shadow-md sm:rounded-lg">
                        <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
                            <thead
                                class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                                <tr>
                                    <th scope="col" class="px-6 py-3">
                                        ФИО
                                    </th>
                                    <th scope="col" class="px-6 py-3">
                                        Должность
                                    </th>
                                    <th scope="col" class="px-6 py-3">

                                    </th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="item in UsersCommission" :key="item.id"
                                    class="odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800 border-b dark:border-gray-700">
                                    <th scope="row"
                                        class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                                        {{ item.user_name }}
                                    </th>
                                    <td class="px-6 py-4">
                                        {{ item.post }}
                                    </td>
                                    <td class="px-6 py-4">
                                        <a class="font-medium text-black cursor-pointer"
                                            @click="delusercommisiion(item)">Удалить</a>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div id="formaddcommission" tabindex="-1" aria-hidden="true"
        class="hidden overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full">
        <div class="relative p-4 w-auto max-w-2xl max-h-full">
            <!-- Modal content -->
            <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">
                <!-- Modal header -->
                <div class="flex items-center justify-between p-4 md:p-5 border-b rounded-t dark:border-gray-600">
                    <h3 class="text-xl font-semibold text-gray-900 dark:text-white">
                        Форма добавления
                    </h3>
                    <button type="button"
                        class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white"
                        data-modal-hide="formaddcommission">
                        <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none"
                            viewBox="0 0 14 14">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6" />
                        </svg>
                        <span class="sr-only">Close modal</span>
                    </button>
                </div>
                <!-- Modal body -->
                <div class="p-4 md:p-5 space-y-4">
                    <input v-model="FIO" type="text" placeholder="ФИО"
                        class="mt-1 mb-1 font-sans w-80 border-none bg-gray-100 p-3 rounded">
                    <input v-model="post" type="text" placeholder="Должность"
                        class="mt-1 mb-6 font-sans w-80 border-none bg-gray-100 p-3 rounded">
                    <input id="datepicker_start" datepicker datepicker-buttons datepicker-autohide
                        datepicker-autoselect-today datepicker-format="yyyy-mm-dd" type="text"
                        class="mt-1 mb-6 font-sans w-80 border-none bg-gray-100 p-3 rounded"
                        placeholder="Выберете дату начала">
                    <input id="datepicker_end" datepicker datepicker-buttons datepicker-autohide
                        datepicker-autoselect-today datepicker-format="yyyy-mm-dd" type="text"
                        class="mt-1 mb-6 font-sans w-80 border-none bg-gray-100 p-3 rounded"
                        placeholder="Выберете дату конец">
                </div>
                <!-- Modal footer -->
                <div class="flex items-center p-4 md:p-5 border-t border-gray-200 rounded-b dark:border-gray-600">
                    <button data-modal-hide="formaddcommission" type="button"
                        class="text-white tbg focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center"
                        @click="addcommissionuser">Принять</button>
                    <button data-modal-hide="formaddcommission" type="button"
                        class="py-2.5 px-5 ms-3 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100  focus:z-10 focus:ring-4 focus:ring-gray-100">Отмена</button>
                </div>
            </div>
        </div>
    </div>
    <div v-if="message != ''" id="error"
        class="flex items-center p-4 mb-4 text-red-800 rounded-lg bg-red-50 dark:bg-gray-800 dark:text-red-400 absolute right-0 bottom-0 w-52"
        role="alert">
        <svg class="flex-shrink-0 w-4 h-4" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor"
            viewBox="0 0 20 20">
            <path
                d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z" />
        </svg>
        <span class="sr-only">Info</span>
        <div class="ms-3 text-sm font-medium">
            {{ message }}
        </div>
    </div>
</template>

<script>
import UserService from '../services/user.service';
import EventBus from "../common/EventBus";
export default {
    data() {
        return {
            UserLogin: '',
            UserName: '',
            UsersCommission: [],
            FIO: '',
            post: '',
            data_start: '',
            data_end: '',
            message: '',
            newfio: '',
            idAdmin: ''

        };
    },
    computed: {
        currentUser() {
            return this.$store.state.auth.user;
        }
    },
    mounted() {
        if (!this.currentUser) {
            this.$router.push('/');
        }
        UserService.getUserBoard().then(
            (response) => {
                this.UserLogin = response.data.users;
                this.UserLogin = this.UserLogin.map(user => user.login).join(', ');
                this.idAdmin = response.data.users[0].id_userbd
                this.UserName = response.data.users;
                this.UserName = this.UserName.map(user => user.name).join(', ');
            },
            (error) => {
                if (error.response && error.response.status === 403) {
                    EventBus.dispatch("logout");
                }
            });
        UserService.getUserCommission().then(
            (response) => {
                this.UsersCommission = response.data.users_commission;
            }
        );
        EventBus.on("logout", () => {
            this.logOut();
        });
    },
    methods: {
        logOut() {
            this.$store.dispatch('auth/logout');
            this.$router.push('/');
        },
        addcommissionuser() {
            this.data_start = document.getElementById('datepicker_start').value
            this.data_end = document.getElementById('datepicker_end').value
            if (this.data_start != '' && this.data_end != '' && this.FIO != '' && this.post != '') {
                let formData = {
                    fullname: this.FIO,
                    post: this.post,
                    date_start: this.data_start,
                    date_end: this.data_end
                }
                this.$store.dispatch('user/adduserscommission', formData).then(
                    response => {
                        if (response.status == 'success') {
                            UserService.getUserCommission().then(
                                (response) => {
                                    this.UsersCommission = response.data.users_commission;
                                }
                            );
                        }
                        else {
                            this.message = 'Такой пользователь уже существует';
                            setTimeout(() => {
                                this.message = '';
                            }, 5000);
                        }
                    }
                );
            }
            else {
                this.message = 'Есть незаполненные поля';
                setTimeout(() => {
                    this.message = '';
                }, 5000);
            }
        },
        delusercommisiion(item) {
            let formData = {
                id: item.id
            }
            this.$store.dispatch('user/deluserscommission', formData).then(
                response => {
                    if (response.status == 'success') {
                        UserService.getUserCommission().then(
                            (response) => {
                                this.UsersCommission = response.data.users_commission;
                            }
                        );
                    }
                }
            );
        },
        settingadmin() {
            let formData = {
                newFIO: this.newfio,
                idAdmin: this.idAdmin
            }
            if (this.newfio != '') {
                this.$store.dispatch('user/settingadmin', formData).then(
                    response => {
                        UserService.getUserBoard().then(
                            (response) => {
                                this.UserLogin = response.data.users;
                                this.UserLogin = this.UserLogin.map(user => user.login).join(', ');
                                this.idAdmin = response.data.users[0].id_userbd
                                this.UserName = response.data.users;
                                this.UserName = this.UserName.map(user => user.name).join(', ');
                            },
                            (error) => {
                                if (error.response && error.response.status === 403) {
                                    EventBus.dispatch("logout");
                                }
                            });
                    }
                );
            }
            else {
                this.message = 'Нет нового ФИО';
                setTimeout(() => {
                    this.message = '';
                }, 5000);
            }
        }
    },
    beforeDestroy() {
        EventBus.remove("logout");
    }
};
</script>

<style>
.textnavbutton {
    color: #71717A;
    background: #18181B;
}

.linenav {
    color: #18181B;
}

.cursordrop {
    color: #71717A;
}
</style>