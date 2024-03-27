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
            <p class="pl-2 pr-2 pt-1 pb-1">ГЭК</p>
            </button>
            <div class="mb-4 ml-3 mr-3 linenav font-semibold">/</div>
            <button id="dropdownDefaultButton" data-dropdown-toggle="dropdown" class="text-white font-medium rounded-lg text-sm text-center inline-flex items-center mb-4" type="button">
                <div class="textnavbutton rounded-full h-5 w-5 me-2">
                    <img src="/iconfornavbar.svg" class="px-1 py-1" alt="kis logo black" />
                </div>
                Формирование списков
                <svg class="w-2.5 h-2.5 ms-3 cursordrop" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 10 6">
                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 4 4 4-4"/>
                </svg>
            </button>

            <!-- Dropdown menu navbar-->
            <div id="dropdown" class="z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow w-44 dark:bg-gray-700">
                <ul class="py-2 text-sm text-gray-700 dark:text-gray-200" aria-labelledby="dropdownDefaultButton">
                <li>
                    <a data-modal-target="AddCommissionPeople" data-modal-toggle="AddCommissionPeople" class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white cursor-pointer">Добавление челенов комиссии</a>
                </li>
                <li>
                    <a href="#" class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">Settings</a>
                </li>
                <li>
                    <a href="#" class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">Earnings</a>
                </li>
                </ul>
            </div>
        </div>
        <div>
            <button id="dropdownAvatarNameButton" data-dropdown-toggle="dropdownAvatarName" class="flex items-center text-sm pe-1 font-medium text-white mb-4" type="button">
            {{ UserLogin }}
            <svg class="w-2.5 h-2.5 ms-3 cursordrop" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 10 6">
            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 4 4 4-4"/>
            </svg>
            </button>

            <!-- Dropdown menu profile-->
            <div id="dropdownAvatarName" class="z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow w-44 dark:bg-gray-700 dark:divide-gray-600">
                <div class="px-4 py-3 text-sm text-gray-900 dark:text-white">
                <div class="font-medium ">{{ UserName }}</div>
                </div>
                <ul class="py-2 text-sm text-gray-700 dark:text-gray-200" aria-labelledby="dropdownInformdropdownAvatarNameButtonationButton">
                <li>
                    <a href="#" class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">Настройки</a>
                </li>
                </ul>
                <div class="py-2">
                <a  class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white cursor-pointer" @click.prevent="logOut">Выход</a>
                </div>
            </div>
        </div>
    </nav>

    <!-- Main modal -->
    <div id="AddCommissionPeople" tabindex="-1" aria-hidden="true" class="hidden overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full">
        <div class="relative p-4 w-full max-w-2xl max-h-full">
            <!-- Modal content -->
            <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">
                <!-- Modal header -->
                <div class="flex items-center justify-between p-4 md:p-5 border-b rounded-t dark:border-gray-600">
                    <h3 class="text-xl font-semibold text-gray-900 dark:text-white">
                        Добавление членов комиссии
                    </h3>
                    <button type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white" data-modal-hide="AddCommissionPeople">
                        <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"/>
                        </svg>
                        <span class="sr-only">Close modal</span>
                    </button>
                </div>
                <!-- Modal body -->
                    <div class="p-4 md:p-5 space-y-4">
                        <button>Добавить</button>
                        <div class="relative overflow-x-auto shadow-md sm:rounded-lg">
                        <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
                            <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                                <tr>
                                    <th scope="col" class="px-6 py-3">
                                        ФИО
                                    </th>
                                    <th scope="col" class="px-6 py-3">
                                        Должность
                                    </th>
                                    <th scope="col" class="px-6 py-3">
                                        Редактирование
                                    </th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="item in UsersCommission" :key="item.id" class="odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800 border-b dark:border-gray-700">
                                    <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                                        {{item.user_name}}
                                    </th>
                                    <td class="px-6 py-4">
                                        {{item.post}}
                                    </td>
                                    <td class="px-6 py-4">
                                        <a href="#" class="font-medium text-black hover:underline">Редактировать</a>
                                    </td>
                                </tr>  
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import UserService from '../services/user.service';
import EventBus from "../common/EventBus";

export default{
    data(){
        return{
            UserLogin: '',
            UserName: '',
            UsersCommission: []
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
        }
    },
    beforeDestroy() {
        EventBus.remove("logout");
    }
};
</script>

<style>
.textnavbutton{
    color: #71717A;
    background: #18181B;
}
.linenav{
    color: #18181B;
}
.cursordrop{
    color: #71717A;
}
</style>