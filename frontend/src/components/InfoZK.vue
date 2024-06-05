<template>
    <div class="container mx-auto mt-7 grid grid-cols-3 gap-8">
        <div class="col-span-2">
            <div class="grid grid-cols-2 gap-5 max-w-3xl">
                <div class="mt-5">
                    <div class="border max-w-96 h-28 pl-5 pt-5 rounded-t-xl colorboxinfo">
                        <p class="text-white font-medium text-lg pb-2">Дата проведения</p>
                        <div class="relative max-w-sm">
                            <div class="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none">
                                <svg class="w-4 h-4 text-gray-500 dark:text-gray-400" aria-hidden="true"
                                    xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
                                    <path
                                        d="M20 4a2 2 0 0 0-2-2h-2V1a1 1 0 0 0-2 0v1h-3V1a1 1 0 0 0-2 0v1H6V1a1 1 0 0 0-2 0v1H2a2 2 0 0 0-2 2v2h20V4ZM0 18a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8H0v10Zm5-8h10a1 1 0 0 1 0 2H5a1 1 0 0 1 0-2Z" />
                                </svg>
                            </div>
                            <input v-model="currentDate" id="datepicker" datepicker datepicker-buttons
                                datepicker-autohide datepicker-autoselect-today datepicker-format="yyyy-mm-dd"
                                type="text"
                                class="bg-none border-dashed containercolorinfo text-sm rounded-3xl block w-44 h-7 ps-10 p-2.5 border-collapse"
                                placeholder="Выберете дату">
                        </div>
                    </div>
                    <div class="border max-w-96 h-11 pl-5 pt-3 rounded-b-xl colorboxbottom">
                        <p class="cursordrop text-xs"></p>
                    </div>
                </div>
                <div class="mt-5">
                    <div class="border max-w-96 h-28 pl-5 pt-5 rounded-t-xl colorboxinfo">
                        <p class="text-white font-medium text-lg pb-2">Председатель</p>
                        <div class="">
                            <input v-model="selectName" type="text" list="names"
                                class="bg-none border-dashed containercolorinfo text-sm rounded-3xl block w-44 h-7 ps-3 p-2.5 border-collapse"
                                placeholder="ФИО">
                            <datalist id="names">
                                <option v-for="item in UsersPPS" :key="item.id" :value=item.name></option>
                            </datalist>
                        </div>
                    </div>
                    <div class="border max-w-96 h-11 pl-5 pt-3 rounded-b-xl colorboxbottom">
                        <p class="cursordrop text-xs"></p>
                    </div>
                </div>
                <div class="mt-5 col-span-2">
                    <div class="border h-28 pl-5 pt-5 rounded-t-xl colorboxinfo">
                        <div class="flex justify-between flex-nowrap items-start">
                            <p class="text-white font-medium text-lg pb-2">Повеска дня</p>
                            <button id="dropdownSearchButton" data-dropdown-toggle="dropdownSearch"
                                class="flex flex-row items-center tbg px-2 mr-5 rounded-xl text-white h-8">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                                    stroke-width="1.5" stroke="currentColor" class="w-3 h-3">
                                    <path stroke-linecap="round" stroke-linejoin="round" d="M12 4.5v15m7.5-7.5h-15" />
                                </svg>
                                Добавить
                            </button>
                        </div>
                        <ul class="pl-5 h-12 text-white overflow-auto">
                            <li class="list-decimal" v-for="item in checkedItems" :key="item.id">
                                <h1>{{ item.name }}</h1>
                            </li>
                        </ul>
                    </div>
                    <div class="border h-auto pl-5 pt-3 rounded-b-xl colorboxbottom overflow-x-auto">
                        <div v-for="item in json" :data-modal-target="'popup-modal-update' + json.indexOf(item)"
                            :data-modal-toggle="'popup-modal-update' + json.indexOf(item)"
                            class="cursor-pointer hover:font-extralight" @click="updatedraft(item)">
                            <p :key="item.id" class="cursordrop text-2xl mr-1">{{ item.title }} {{ item.key }}</p>
                        </div>
                        <button data-modal-target="AddDraft" data-modal-toggle="AddDraft"
                            class="flex flex-row items-center tbg px-2 mr-5 mb-3 rounded-lg text-white h-8">
                            Добавить
                        </button>
                    </div>
                </div>
            </div>
        </div>
        <div>
            <div class="h-44 overflow-auto">
                <p class="text-white font-medium text-lg pb-2 text-start">Черновики</p>
                <div v-for="item in filelist" :key="item.id" class="flex flex-row" v-on:click="GetInfoFromFileZK(item)">
                    <div class="flex flex-row mr-auto cursor-pointer">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                            style="color: #71717A;" stroke="currentColor" class="w-6 h-6 mr-1">
                            <path stroke-linecap="round" stroke-linejoin="round"
                                d="M19.5 14.25v-2.625a3.375 3.375 0 0 0-3.375-3.375h-1.5A1.125 1.125 0 0 1 13.5 7.125v-1.5a3.375 3.375 0 0 0-3.375-3.375H8.25m2.25 0H5.625c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 0 0-9-9Z" />
                        </svg>
                        <p class="text-white">{{ item.name }}</p>
                    </div>
                    <p style="color: #71717A;">{{ item.data }}</p>
                </div>
            </div>
            <div class="border" style="border-color: #71717A;"></div>
            <div class="mt-10 border rounded-xl px-5 py-4 colorboxinfo" style="border-color: #71717A;">
                <p class="text-white font-medium text-lg pb-2 text-start">Действия</p>
                <button data-modal-target="popup-modal" data-modal-toggle="popup-modal"
                    class="tbg px-2 mt-2 w-full rounded-sm text-white h-8">Сохранить черновик</button>
                <button v-if="downloadFileId != ''" class="tbg px-2 mt-2 w-full rounded-sm text-white h-8"
                    @click="DownloadFileKZ()">Скачать документ</button>
            </div>
        </div>
    </div>

    <div id="popup-modal" tabindex="-1"
        class="hidden overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full">
        <div class="relative p-4 w-full max-w-md max-h-full">
            <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">
                <button type="button"
                    class="absolute top-3 end-2.5 text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white"
                    data-modal-hide="popup-modal">
                    <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none"
                        viewBox="0 0 14 14">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6" />
                    </svg>
                    <span class="sr-only">Close modal</span>
                </button>
                <div class="p-4 md:p-5 text-center">
                    <svg class="mx-auto mb-4 text-gray-400 w-12 h-12 dark:text-gray-200" aria-hidden="true"
                        xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M10 11V6m0 8h.01M19 10a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" />
                    </svg>
                    <h3 class="mb-5 text-lg font-normal text-gray-500 dark:text-gray-400">Для создания черновика задайте
                        имя</h3>
                    <input v-model="filename" type="text" placeholder="Введите название файла"
                        class="mt-1 mb-6 font-sans w-80 border-none bg-gray-100 p-3 rounded">
                    <button data-modal-hide="popup-modal" type="button"
                        class="text-white tbg focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center"
                        @click="SaveDraftFile">
                        Создать
                    </button>
                    <button data-modal-hide="popup-modal" type="button"
                        class="py-2.5 px-5 ms-3 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700">Отмена</button>
                </div>
            </div>
        </div>
    </div>

    <!-- Dropdown menu -->
    <div id="dropdownSearch" class="z-10 hidden bg-white rounded-lg shadow w-60 dark:bg-gray-700">
        <div class="p-3">
            <label for="input-group-search" class="sr-only">Search</label>
            <div class="relative">
                <div class="absolute inset-y-0 rtl:inset-r-0 start-0 flex items-center ps-3 pointer-events-none">
                    <svg class="w-4 h-4 text-gray-500 dark:text-gray-400" aria-hidden="true"
                        xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z" />
                    </svg>
                </div>
                <input type="text" id="input-group-search"
                    class="block w-full p-2 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50  dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                    placeholder="Поиск">
            </div>
        </div>
        <ul class="h-48 px-3 pb-3 overflow-y-auto text-sm text-gray-700 dark:text-gray-200"
            aria-labelledby="dropdownSearchButton">
            <li v-for="item in questions" :key="item[0]">
                <div v-for="it in item[1]" :key="it.id"
                    class=" flex items-center ps-2 rounded hover:bg-gray-100 dark:hover:bg-gray-600">
                    <input :id="`checkbox-item-` + it.id" type="checkbox" value=""
                        class="w-4 h-4 text-teal-400 bg-gray-100 border-gray-300 rounded focus:ring-0"
                        @change="checkboxQuestion(it)">
                    <label :for="`checkbox-item-` + it.id"
                        class="w-full py-2 ms-2 text-sm font-medium text-gray-900 rounded dark:text-gray-300">{{
                            it.name }}</label>
                </div>
            </li>
        </ul>
    </div>


    <div id="AddDraft" tabindex="-1" aria-hidden="true"
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
                        data-modal-hide="AddDraft">
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
                        <select v-model="namedraft" @change="getListDrafts"
                            class="bg-white border-dashed text-sm rounded-3xl block w-80 ps-3 p-2.5 border-collapse">
                            <option v-for="item in namedraft_array" :key="item.id" :value="item.name">{{ item.name }}
                            </option>
                        </select>
                    </div>
                    <div class="">
                        <select v-model="titledraft"
                            class="bg-white border-dashed text-sm rounded-3xl block w-80 ps-3 p-2.5 border-collapse">
                            <option v-for="item in checkedItems" :key="item.id" :value="item.id">{{ item.name }}
                            </option>
                        </select>
                    </div>
                    <textarea v-model="textdrafts" @input="showOptions"
                        class="resize rounded-md mt-1 mb-6 font-sans w-80 border-none bg-gray-100 p-3"
                        placeholder="Введите новый текст"></textarea>
                    <div v-show="showDropdown" class="dropdown">
                        <ul>
                            <li v-for="item in exempletext" :key="item.id" @click="setText(item.text)">{{ item.text }}
                            </li>
                        </ul>
                    </div>
                    <div v-if="namedraft == 'Выступили'" class="flex flex-col">
                        <h1>Голосование</h1>
                        <h1>За:</h1>
                        <input v-model="za" type="number" min="0" :max="numberAll" placeholder="Введите число за"
                            class="mt-1 mb-6 font-sans w-80 border-none bg-gray-100 p-3 rounded"
                            :onchange="updateNumber">
                        <h1>Против:</h1>
                        <input v-model="prot" type="number" min="0" :max="numberAll" placeholder="Введите число против"
                            class="mt-1 mb-6 font-sans w-80 border-none bg-gray-100 p-3 rounded"
                            :onchange="updateNumber">
                        <h1>Воздерживаются:</h1>
                        <input v-model="vozd" type="number" min="0" :max="numberAll"
                            placeholder="Введите число воздержавшихся"
                            class="mt-1 mb-6 font-sans w-80 border-none bg-gray-100 p-3 rounded"
                            :onchange="updateNumber">
                    </div>
                </div>
                <!-- Modal footer -->
                <div class="flex items-center p-4 md:p-5 border-t border-gray-200 rounded-b dark:border-gray-600">
                    <button data-modal-hide="AddDraft" type="button"
                        class="text-white tbg focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center"
                        @click="addtitledraft">Принять</button>
                    <button data-modal-hide="AddDraft" type="button"
                        class="py-2.5 px-5 ms-3 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100  focus:z-10 focus:ring-4 focus:ring-gray-100">Отмена</button>
                </div>
            </div>
        </div>
    </div>


    <div v-for="item in json" :key="item.id" :id="'popup-modal-update' + json.indexOf(item)" tabindex="-1"
        class="hidden overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full">
        <div class="relative p-4 w-auto max-w-full max-h-full">
            <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">
                <button type="button" :id="'closeModal' + json.indexOf(item)"
                    class="absolute top-3 end-2.5 text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white"
                    :data-modal-hide="'popup-modal-update' + json.indexOf(item)">
                    <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none"
                        viewBox="0 0 14 14">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6" />
                    </svg>
                    <span class="sr-only">Close modal</span>
                </button>
                <div class="p-4 md:p-5 text-center">
                    <h3 class="mb-5 text-lg font-normal text-gray-500 dark:text-gray-400">Желаете обновить
                        элемент?</h3>
                    <textarea v-model="textdraftsModal" :id="'textdraftsModal' + json.indexOf(item)"
                        class="resize rounded-md mt-1 mb-6 font-sans w-80 border-none bg-gray-100 p-3"
                        placeholder="Введите новый текст"></textarea>
                </div>
                <div class="flex items-center p-4 md:p-5 border-t border-gray-200 rounded-b dark:border-gray-600">
                    <button :data-modal-hide="'popup-modal-update' + json.indexOf(item)" type="button"
                        :id="'delElem' + json.indexOf(item)"
                        class="text-white bg-red-600 hover:bg-red-800 focus:ring-4 focus:outline-none focus:ring-red-300 dark:focus:ring-red-800 font-medium rounded-lg text-sm inline-flex items-center px-5 py-2.5 text-center">
                        Удалить
                    </button>
                    <button :data-modal-hide="'popup-modal-update' + json.indexOf(item)" type="button"
                        :id="'updateInfo' + json.indexOf(item)"
                        class="py-2.5 px-5 ms-3 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700">Обновить</button>
                </div>
            </div>
        </div>
    </div>



    <div v-if="this.message != ''" id="error"
        class="flex items-center p-4 mb-4 text-red-800 rounded-lg bg-red-50 dark:bg-gray-800 dark:text-red-400 absolute right-0 bottom-0 w-52"
        role="alert">
        <svg class="flex-shrink-0 w-4 h-4" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor"
            viewBox="0 0 20 20">
            <path
                d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z" />
        </svg>
        <span class="sr-only">Info</span>
        <div class="ms-3 text-sm font-medium">
            {{ this.message }}
        </div>
    </div>
</template>

<script>
import PPS from '../services/pps.service';
import FileServices from '../services/file.service';
import UserService from '../services/user.service';
import { Modal } from 'flowbite';
export default {
    data() {
        return {
            selectName: null,
            UsersPPS: null,
            draftsList: null,
            questions: null,
            filelist: null,
            filename: null,
            checkedItems: [],
            namedraft: null,
            namedraft_array: null,
            textdrafts: null,
            titledraft: null,
            json: [],
            score: 0,
            score_title: 1,
            score_title_two: 1,
            message: '',
            exempletext: null,
            showDropdown: false,
            currentDate: '',
            adminUser: '',
            filenamedownload: '',
            downloadFileId: '',
            textdraftsModal: '',
            za: 0,
            prot: 0,
            vozd: 0,
            numberAll: null
        }
    },
    mounted() {
        PPS.getpps().then(
            response => {
                this.UsersPPS = response.data.pps;
            }
        );
        FileServices.getquestion().then(
            response => {
                this.questions = response.data.question;
            }
        );
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

        UserService.getUserBoard().then(
            response => {
                this.adminUser = response.data.users[0].id_userbd;
            }
        );

        FileServices.getdraftsfile().then(
            response => {
                this.filelist = response.data.file;
            }
        );

        const today = new Date();
        const year = today.getFullYear();
        const month = String(today.getMonth() + 1).padStart(2, '0');
        const day = String(today.getDate()).padStart(2, '0');
        this.currentDate = `${year}-${month}-${day}`;
    },
    methods: {
        updateNumber() {
            this.numberAll = this.UsersPPS.length
            this.numberAll = this.numberAll - this.za
            this.numberAll = this.numberAll - this.prot
            this.numberAll = this.numberAll - this.vozd
        },
        checkboxQuestion(item) {
            const checkbox = document.getElementById('checkbox-item-' + item.id);
            if (checkbox.checked) {
                this.checkedItems.push(item);
            } else {
                this.checkedItems = this.checkedItems.filter(id => id !== item);
            }
        },
        getListDrafts() {
            FileServices.getdrafts().then(
                response => {
                    this.draftsList = response.data.draft;
                }
            );
            let nameDRF = this.namedraft;
            let searchelem = this.draftsList.find(function (item) {
                return item[0] === nameDRF;
            });
            this.exempletext = searchelem[1];
        },
        addtitledraft() {
            if (this.checkedItems.length != 0 && this.textdrafts != null) {
                if (this.json.length == 0) {
                    let formData = {
                        key: this.score_title,
                        titledraft: this.titledraft,
                        title: this.namedraft,
                        text: this.textdrafts
                    }
                    this.json.push(formData)
                }
                else if (this.json[this.json.length - 1].titledraft != this.titledraft) {
                    this.score_title += 1;
                    let formData = {
                        key: this.score_title,
                        titledraft: this.titledraft,
                        title: this.namedraft,
                        text: this.textdrafts
                    }
                    this.json.push(formData)
                }
                else if (this.namedraft == this.json[this.json.length - 1].title) {
                    let formData = {
                        key: this.score_title + '.' + this.score_title_two,
                        titledraft: this.titledraft,
                        title: this.namedraft,
                        text: this.textdrafts
                    }
                    this.json.push(formData)
                    this.score_title_two += 1;
                }
                else if (this.json[this.json.length - 1].title == 'Слушали' && this.namedraft == 'Постановили') {
                    this.score_title_two = 1;
                    this.score_title += 1;
                    let formData = {
                        key: this.score_title,
                        titledraft: this.titledraft,
                        title: this.namedraft,
                        text: this.textdrafts
                    }
                    this.json.push(formData)
                }
                else if (this.json[this.json.length - 1].title == 'Постановили' && this.namedraft == 'Слушали') {
                    this.score_title += 1;
                    let formData = {
                        key: this.score_title,
                        titledraft: this.titledraft,
                        title: this.namedraft,
                        text: this.textdrafts
                    }
                    this.json.push(formData)
                }
                else if (this.namedraft == 'Выступили') {
                    this.score_title += 1;
                    let formData = {
                        key: this.score_title,
                        titledraft: this.titledraft,
                        title: this.namedraft,
                        text: this.textdrafts,
                        za: this.za > 0 ? this.za : 'нет',
                        prot: this.prot ? this.prot : 'нет',
                        vozd: this.vozd ? this.vozd : 'нет'
                    }
                    this.json.push(formData)
                }
                this.score += 1;

                let nameDRF = this.namedraft;
                let searchelem = this.namedraft_array.find(function (item) {
                    if (item.name === nameDRF) {
                        return item.name === nameDRF;
                    }
                });
                if (this.textdrafts != null) {
                    let formData = {
                        id_name: searchelem.id,
                        text_draft: this.textdrafts
                    }
                    this.$store.dispatch('file/adddrafts', formData);
                }
            }
            else {
                this.message = 'Проверьте, заполнена ли "Повестка дня" или текст';
                setTimeout(() => {
                    this.message = '';
                }, 5000);
            }
        },
        updatedraft(item) {
            const $targetEl = document.getElementById('popup-modal-update' + this.json.indexOf(item));
            const $buttonCloseModal = document.getElementById('closeModal' + this.json.indexOf(item));
            const $buttonUpdateInfo = document.getElementById('updateInfo' + this.json.indexOf(item));
            const $buttonDelElem = document.getElementById('delElem' + this.json.indexOf(item));
            const modal = new Modal($targetEl);
            this.textdraftsModal = item.text;
            modal.show();
            $buttonCloseModal.onclick = function () {
                modal.hide();
            };
            var array = this.json;
            $buttonUpdateInfo.onclick = function () {
                const new_text = document.getElementById('textdraftsModal' + array.indexOf(item)).value;
                item.text = new_text;
                modal.hide();
            };
            $buttonDelElem.onclick = function () {
                array.splice(array.indexOf(item), 1);
                modal.hide();
            }
        },
        SaveDraftFile() {
            if (this.json.length != 0 && this.filename != null && this.selectName != null) {
                let formData = {
                    data: this.currentDate,
                    pred: this.selectName,
                    adminuser: this.adminUser,
                    file_name: this.filename,
                    json: JSON.stringify(this.json),
                    checkedItems: JSON.stringify(this.checkedItems)
                }
                this.$store.dispatch('file/adddraftfile', formData).then(
                    response => {
                        if (response.status == 'success') {
                            FileServices.getdraftsfile().then(
                                response => {
                                    this.filelist = response.data.file;
                                }
                            );
                        }
                    }
                );
            }
            else {
                this.message = 'Проверьте, заполнено ли название файла или повеска дня';
                setTimeout(() => {
                    this.message = '';
                }, 5000);
            }

        },
        showOptions() {
            if (this.textdrafts.length > 0) {
                this.showDropdown = true;
            } else {
                this.showDropdown = false;
            }
        },
        setText(text) {
            this.textdrafts = text;
            this.showDropdown = false;
        },
        GetInfoFromFileZK(item) {
            this.downloadFileId = item.id;
            FileServices.getdraftsfileinfo(item).then(
                response => {
                    this.currentDate = response.file.data;
                    this.selectName = response.file.chairperson;
                    this.json = JSON.parse(JSON.parse(response.file.text));
                    this.checkedItems = JSON.parse(response.file.checkedItems)
                    this.filename = response.file.name;
                    this.score = this.json.length;
                    this.score_title = this.json.length;
                }
            );
        },
        DownloadFileKZ() {
            let formData = {
                data: this.currentDate,
                pred: this.selectName,
                json: this.json,
                adminuser: this.adminUser,
                pps: this.UsersPPS,
                checkedItems: this.checkedItems,
                fileId: this.downloadFileId
            }
            this.$store.dispatch('file/downloadfileZK', formData).then(
                response => {
                    if (response.status == 'success') {
                        location.href = 'http://127.0.0.1:5000/downloadfileZK?id=' + this.downloadFileId;
                    }
                }
            );
        }
    }
}
</script>