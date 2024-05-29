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
                <router-link class="pl-2 pr-2 pt-1 pb-1" to='/mainpage'>Заседание кафедры</router-link>
            </button>
            <div class="mb-4 ml-3 mr-3 linenav font-semibold">/</div>
            <button id="dropdownDefaultButton" data-dropdown-toggle="dropdown"
                class="text-white font-medium rounded-lg text-sm text-center inline-flex items-center mb-4"
                type="button">
                <div class="textnavbutton rounded-full h-5 w-5 me-2">
                    <img src="/iconfornavbar.svg" class="px-1 py-1" alt="kis logo black" />
                </div>
                Заседание
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
                        <a data-modal-target="AddPPS" data-modal-toggle="AddPPS"
                            class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white cursor-pointer">ППС</a>
                    </li>
                    <li>
                        <a data-modal-target="ListQuestion" data-modal-toggle="ListQuestion"
                            class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white cursor-pointer">Повестка
                            заседания</a>
                    </li>
                    <li>
                        <a data-modal-target="ListTextDrafts" data-modal-toggle="ListTextDrafts"
                            class="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white cursor-pointer"
                            @click='updatelist'>Шаблоны
                            текстов</a>
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



    <!-- Modal window -->
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
    <div id="AddPPS" tabindex="-1" aria-hidden="true"
        class="hidden overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full">
        <div class="relative p-4 w-full max-w-4xl max-h-full">
            <!-- Modal content -->
            <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">
                <!-- Modal header -->
                <div class="flex items-center justify-between p-4 md:p-5 border-b rounded-t dark:border-gray-600">
                    <h3 class="text-xl font-semibold text-gray-900 dark:text-white">
                        Добавление ППС
                    </h3>
                    <button type="button"
                        class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white"
                        data-modal-hide="AddPPS">
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
                    <button data-modal-hide="AddPPS" data-modal-target="formaddpps" data-modal-toggle="formaddpps"
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
                                        Кафедра
                                    </th>
                                    <th scope="col" class="px-6 py-3">
                                        Должность
                                    </th>
                                    <th scope="col" class="px-6 py-3">
                                        Ученое звание
                                    </th>
                                    <th scope="col" class="px-6 py-3">
                                        Степень
                                    </th>
                                    <th scope="col" class="px-6 py-3">

                                    </th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="item in UsersPPS" :key="item.id"
                                    class="odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800 border-b dark:border-gray-700">
                                    <th scope="row"
                                        class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                                        {{ item.name }}
                                    </th>
                                    <td class="px-6 py-4">
                                        {{ item.departament }}
                                    </td>
                                    <td class="px-6 py-4">
                                        {{ item.role }}
                                    </td>
                                    <td class="px-6 py-4">
                                        {{ item.academic_title }}
                                    </td>
                                    <td class="px-6 py-4">
                                        {{ item.degree }}
                                    </td>
                                    <td class="px-6 py-4">
                                        <a class="font-medium text-black cursor-pointer"
                                            @click="deluserpps(item)">Удалить</a>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    </div>



    <div id="ListQuestion" tabindex="-1" aria-hidden="true"
        class="hidden overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full">
        <div class="relative p-4 w-full max-w-2xl max-h-full">
            <!-- Modal content -->
            <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">
                <!-- Modal header -->
                <div class="flex items-center justify-between p-4 md:p-5 border-b rounded-t dark:border-gray-600">
                    <h3 class="text-xl font-semibold text-gray-900 dark:text-white">
                        Повестки заседаний
                    </h3>
                    <button type="button"
                        class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white"
                        data-modal-hide="ListQuestion">
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
                    <button data-modal-hide="ListQuestion" data-modal-target="AddListQuestion"
                        data-modal-toggle="AddListQuestion"
                        class="text-white tbg focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center">Добавить</button>
                    <div v-for="items in questionList" :key="items[0]"
                        class="relative overflow-x-auto shadow-md sm:rounded-lg">
                        <h1 class="text-center pb-1">{{ items[0] }}</h1>
                        <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
                            <thead
                                class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                                <tr>
                                    <th scope="col" class="px-6 py-3">
                                        Содержание вопроса
                                    </th>
                                    <th scope="col" class="px-6 py-3">

                                    </th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="item in items[1]" :key="item.id"
                                    class="odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800 border-b dark:border-gray-700">
                                    <th scope="row"
                                        class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                                        {{ item.name }}
                                    </th>
                                    <td class="px-6 py-4">
                                        <a class="font-medium text-black cursor-pointer"
                                            @click="delquestions(item)">Удалить</a>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div id="ListTextDrafts" tabindex="-1" aria-hidden="true"
        class="hidden overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full">
        <div class="relative p-4 w-full max-w-2xl max-h-full">
            <!-- Modal content -->
            <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">
                <!-- Modal header -->
                <div class="flex items-center justify-between p-4 md:p-5 border-b rounded-t dark:border-gray-600">
                    <h3 class="text-xl font-semibold text-gray-900 dark:text-white">
                        Текстовые шаблоны
                    </h3>
                    <button type="button"
                        class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white"
                        data-modal-hide="ListTextDrafts">
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
                    <button data-modal-hide="ListTextDrafts" data-modal-target="AddListDraftText"
                        data-modal-toggle="AddListDraftText"
                        class="text-white tbg focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center">Добавить</button>
                    <div v-for="items in draftsList" :key="items[0]"
                        class="relative overflow-x-auto shadow-md sm:rounded-lg">
                        <h1 class="text-center pb-1">{{ items[0] }}</h1>
                        <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
                            <thead
                                class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                                <tr>
                                    <th scope="col" class="px-6 py-3">
                                        Содержание текста
                                    </th>
                                    <th scope="col" class="px-6 py-3">

                                    </th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="item in items[1]" :key="item.id"
                                    class="odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800 border-b dark:border-gray-700">
                                    <th scope="row"
                                        class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                                        {{ item.text }}
                                    </th>
                                    <td class="px-6 py-4">
                                        <a class="font-medium text-black cursor-pointer"
                                            @click="deldraft(item)">Удалить</a>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    </div>


    <div id="AddListQuestion" tabindex="-1" aria-hidden="true"
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
                        data-modal-hide="AddListQuestion">
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
                    <input type="text" v-model="enteredMonth" list="months" @input="updateMonthName" placeholder="Месяц"
                        class="mt-1 mb-1 font-sans w-80 border-none bg-gray-100 p-3 rounded">
                    <datalist id="months">
                        <option v-for="(month, index) in months" :key="index">{{ month }}</option>
                    </datalist>
                    <input v-model="question" type="text" placeholder="Введите вопрос"
                        class="mt-1 mb-6 font-sans w-80 border-none bg-gray-100 p-3 rounded">
                </div>
                <!-- Modal footer -->
                <div class="flex items-center p-4 md:p-5 border-t border-gray-200 rounded-b dark:border-gray-600">
                    <button data-modal-hide="AddListQuestion" type="button"
                        class="text-white tbg focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center"
                        @click="addquestion">Принять</button>
                    <button data-modal-hide="AddListQuestion" type="button"
                        class="py-2.5 px-5 ms-3 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100  focus:z-10 focus:ring-4 focus:ring-gray-100">Отмена</button>
                </div>
            </div>
        </div>
    </div>

    <div id="AddListDraftText" tabindex="-1" aria-hidden="true"
        class="hidden overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full">
        <div class="relative p-4 w-auto max-w-full max-h-full">
            <!-- Modal content -->
            <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">
                <!-- Modal header -->
                <div class="flex items-center justify-between p-4 md:p-5 border-b rounded-t dark:border-gray-600">
                    <h3 class="text-xl font-semibold text-gray-900 dark:text-white">
                        Форма добавления
                    </h3>
                    <button type="button"
                        class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white"
                        data-modal-hide="AddListDraftText">
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
                    <div class="">
                        <select v-model="namedraft" id="namedraft"
                            class="bg-white border-dashed text-sm rounded-3xl block w-44 ps-3 p-2.5 border-collapse">
                            <option v-for="item in namedraft_array" :key="item.id" :value="item.id">{{ item.name }}
                            </option>
                        </select>
                    </div>
                    <textarea v-model="textdrafts"
                        class="resize rounded-md mt-1 mb-6 font-sans w-80 border-none bg-gray-100 p-3"
                        placeholder="Введите новый текст"></textarea>
                </div>
                <!-- Modal footer -->
                <div class="flex items-center p-4 md:p-5 border-t border-gray-200 rounded-b dark:border-gray-600">
                    <button data-modal-hide="AddListDraftText" type="button"
                        class="text-white tbg focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center"
                        @click="addtextdraft">Принять</button>
                    <button data-modal-hide="AddListDraftText" type="button"
                        class="py-2.5 px-5 ms-3 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100  focus:z-10 focus:ring-4 focus:ring-gray-100">Отмена</button>
                </div>
            </div>
        </div>
    </div>

    <div id="formaddpps" tabindex="-1" aria-hidden="true"
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
                        data-modal-hide="formaddpps">
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
                    <input v-model="departament" list="departament" type="text" placeholder="Кафедра"
                        class="mt-1 mb-6 font-sans w-80 border-none bg-gray-100 p-3 rounded">
                    <datalist id="departament">
                        <option v-for="item in name_drafts_departament" :key="item.id" :value=item.name></option>
                    </datalist>
                    <input v-model="post" list="role" type="text" placeholder="Должность"
                        class="mt-1 mb-6 font-sans w-80 border-none bg-gray-100 p-3 rounded">
                    <datalist id="role">
                        <option v-for="item in name_drafts_role" :key="item.id" :value=item.name></option>
                    </datalist>
                    <input v-model="academic_title" list="academic_title" type="text" placeholder="Ученое звание"
                        class="mt-1 mb-6 font-sans w-80 border-none bg-gray-100 p-3 rounded">
                    <datalist id="academic_title">
                        <option v-for="item in name_drafts_academic_title" :key="item.id" :value=item.name></option>
                    </datalist>
                    <input v-model="degree" list="academic_degree" type="text" placeholder="Степень"
                        class="mt-1 mb-6 font-sans w-80 border-none bg-gray-100 p-3 rounded">
                    <datalist id="academic_degree">
                        <option value="к.т.н."></option>
                        <option value="д.т.н."></option>
                        <option value="к.ф.-м.н."></option>
                        <option value="к.э.н."></option>
                    </datalist>
                </div>
                <!-- Modal footer -->
                <div class="flex items-center p-4 md:p-5 border-t border-gray-200 rounded-b dark:border-gray-600">
                    <button data-modal-hide="formaddpps" type="button"
                        class="text-white tbg focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center"
                        @click="addpps">Принять</button>
                    <button data-modal-hide="formaddpps" type="button"
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
import PPS from '../services/pps.service';
import FileServices from '../services/file.service';
export default {
    data() {
        return {
            UserLogin: '',
            UserName: '',
            UsersPPS: [],
            FIO: '',
            post: '',
            message: '',
            newfio: '',
            idAdmin: '',
            departament: '',
            academic_title: '',
            enteredMonth: '',
            degree: null,
            months: [
                'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
                'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'
            ],
            question: '',
            questionList: null,
            namedraft: '',
            namedraft_array: null,
            textdrafts: '',
            draftsList: null,
            name_drafts_academic_title: [],
            name_drafts_departament: [],
            name_drafts_role: []
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
        PPS.getpps().then(
            response => {
                this.UsersPPS = response.data.pps;
            }
        );
        FileServices.getquestion().then(
            response => {
                this.questionList = response.data.question;
            }
        );
        EventBus.on("logout", () => {
            this.logOut();
        });
        FileServices.getnamedrafts().then(
            response => {
                this.namedraft_array = response.data.name_drafts;
            }
        );
        FileServices.getdrafts().then(
            response => {
                this.draftsList = response.data.draft;
            }
        );
        FileServices.getroleandmoreinfo().then(
            response => {
                this.name_drafts_academic_title = response.data.name_drafts_academic_title;
                this.name_drafts_departament = response.data.name_drafts_departament;
                this.name_drafts_role = response.data.name_drafts_role;
            }
        );
    },
    methods: {
        logOut() {
            this.$store.dispatch('auth/logout');
            this.$router.push('/');
        },
        addpps() {
            if (this.degree != null && this.FIO != '' && this.departament != '' && this.post != '' && this.academic_title != '') {
                let formDate = {
                    name: this.FIO,
                    departament: this.departament,
                    post: this.post,
                    academic_title: this.academic_title,
                    degree: this.degree
                };
                this.$store.dispatch('user/addpps', formDate).then(
                    response => {
                        if (response.status = "success") {
                            PPS.getpps().then(
                                response => {
                                    PPS.getpps().then(
                                        response => {
                                            this.UsersPPS = response.data.pps;
                                        }
                                    );
                                }
                            );
                        }
                        else {
                            this.message = 'Пользователь с таким ФИО уже существует';
                            setTimeout(() => {
                                this.message = '';
                            }, 5000);
                        }
                    }
                )
            }
            else {
                this.message = 'Данные не заполнены или заполнены неверно';
                setTimeout(() => {
                    this.message = '';
                }, 5000);
            }
        },
        deluserpps(item) {
            let formData = {
                id: item.id
            }
            this.$store.dispatch('user/deluserspps', formData).then(
                response => {
                    if (response.status == 'success') {
                        PPS.getpps().then(
                            response => {
                                this.UsersPPS = response.data.pps;
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
        },
        updateMonthName() {
            const enteredMonth = this.enteredMonth.trim().toLowerCase();
            if (enteredMonth) {
                const foundMonth = this.months.find(month => month.toLowerCase() === enteredMonth);
                this.monthName = foundMonth || '';
            } else {
                this.monthName = '';
            }
        },
        addquestion() {
            if (this.enteredMonth != '', this.question != '') {
                let formData = {
                    month: this.enteredMonth,
                    question: this.question
                };
                this.$store.dispatch('file/addquestion', formData).then(
                    response => {
                        if (response.status == 'success') {
                            FileServices.getquestion().then(
                                response => {
                                    this.questionList = response.data.question;
                                }
                            );
                        }
                    }
                );
            }
            else {
                this.message = 'Данные не заполнены или заполнены неверно';
                setTimeout(() => {
                    this.message = '';
                }, 5000);
            }
        },
        addtextdraft() {
            if (this.namedraft != '' && this.textdrafts != '') {
                let formData = {
                    id_name: this.namedraft,
                    text_draft: this.textdrafts
                }
                this.$store.dispatch('file/adddrafts', formData).then(
                    response => {
                        if (response.status == 'success') {
                            FileServices.getdrafts().then(
                                response => {
                                    this.draftsList = response.data.draft;
                                }
                            );
                        }
                    }
                );
            } else {
                this.message = 'Данные не заполнены или заполнены неверно';
                setTimeout(() => {
                    this.message = '';
                }, 5000);
            }

        },
        deldraft(item) {
            let formData = {
                id: item.id
            };
            this.$store.dispatch('file/deldraft', formData).then(
                response => {
                    if (response.status == 'success') {
                        FileServices.getdrafts().then(
                            response => {
                                this.draftsList = response.data.draft;
                            }
                        );
                    }
                }
            )
        },
        delquestions(item) {
            let formData = {
                id: item.id
            };
            this.$store.dispatch('file/delquestion', formData).then(
                response => {
                    if (response.status == 'success') {
                        FileServices.getquestion().then(
                            response => {
                                this.questionList = response.data.question;
                            }
                        );
                    }
                }
            );
        },
        updatelist() {
            FileServices.getdrafts().then(
                response => {
                    this.draftsList = response.data.draft;
                }
            );
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