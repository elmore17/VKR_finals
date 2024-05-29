<template>
    <div class="container mx-auto mt-7 grid grid-cols-3 gap-8">
        <!-- block for adding info -->
        <div class="col-span-2">
            <div class="flex flex-row items-center">
                <div class="mr-3">
                    <p class="text-white font-medium text-xl">Заполнение информации</p>
                </div>
                <button data-modal-target="AddFileStudents" data-modal-toggle="AddFileStudents"
                    class="flex flex-row items-center tbg px-3 rounded-xl text-white h-8">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                        stroke="currentColor" class="w-3 h-3">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M12 4.5v15m7.5-7.5h-15" />
                    </svg>
                    Добавить протокол
                </button>
            </div>
            <div class="grid grid-cols-2 gap-5 max-w-3xl">
                <div class="mt-5">
                    <div class="border max-w-96 h-28 pl-5 pt-5 rounded-t-xl colorboxinfo">
                        <p class="text-white font-medium text-lg pb-2">Дата формирования</p>
                        <div class="relative max-w-sm">
                            <div class="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none">
                                <svg class="w-4 h-4 text-gray-500 dark:text-gray-400" aria-hidden="true"
                                    xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
                                    <path
                                        d="M20 4a2 2 0 0 0-2-2h-2V1a1 1 0 0 0-2 0v1h-3V1a1 1 0 0 0-2 0v1H6V1a1 1 0 0 0-2 0v1H2a2 2 0 0 0-2 2v2h20V4ZM0 18a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8H0v10Zm5-8h10a1 1 0 0 1 0 2H5a1 1 0 0 1 0-2Z" />
                                </svg>
                            </div>
                            <input v-model="currentDateStart" id="datepicker" datepicker datepicker-buttons
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
                        <p class="text-white font-medium text-lg pb-2">Председатель ГЭК</p>
                        <div class="">
                            <input v-model="selectNamePred" type="text" list="names"
                                class="bg-none border-dashed containercolorinfo text-sm rounded-3xl block w-44 h-7 ps-3 p-2.5 border-collapse"
                                placeholder="ФИО">
                            <datalist id="names">
                                <option v-for="item in UsersCommission" :key="item.id" :value=item.user_name></option>
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
                            <p class="text-white font-medium text-lg pb-2">Вопросы</p>
                            <button v-if="questions.length < 5" @click="AddQuestionStudents"
                                data-modal-target="AddQuestionStudents" data-modal-toggle="AddQuestionStudents"
                                class="flex flex-row items-center tbg px-3 mr-5 rounded-xl text-white h-8">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                                    stroke-width="1.5" stroke="currentColor" class="w-3 h-3">
                                    <path stroke-linecap="round" stroke-linejoin="round" d="M12 4.5v15m7.5-7.5h-15" />
                                </svg>
                                Добавить
                            </button>
                        </div>
                    </div>
                    <div class="border h-11 pl-5 pt-3 rounded-b-xl colorboxbottom overflow-x-auto">
                        <div v-for="item in questions" class="cursor-pointer hover:font-extralight"
                            @click="updateQuestion(item)">
                            <p :key="item.title" class="cursordrop text-xs mr-1">{{ item.name }} - {{ item.title }}</p>
                        </div>
                    </div>
                </div>
            </div>
            <div v-if="selectedItemDetails != null" class="grid grid-cols-2 mt-5 gap-5 max-w-3xl">
                <div class="mt-5">
                    <div class="border max-w-96 h-28 pl-5 pt-5 rounded-t-xl colorboxinfo">
                        <p class="text-white font-medium text-lg pb-2">Присутствие на защите ВКР</p>
                        <div class="relative max-w-sm">
                            <select v-model="stateuser" id="estimatesVKR"
                                class="bg-none border-dashed containercolorinfo text-sm rounded-3xl block w-44 ps-3 p-2.5 border-collapse"
                                @change="addBe($event)">
                                <option value="true">Да</option>
                                <option value="false">Нет</option>
                            </select>
                        </div>
                    </div>
                    <div class="border max-w-96 h-11 pl-5 pt-3 rounded-b-xl colorboxbottom overflow-x-auto">
                    </div>
                </div>
                <div class="mt-5">
                    <div class="border max-w-96 h-28 pl-5 pt-5 rounded-t-xl colorboxinfo">
                        <p class="text-white font-medium text-lg pb-2">Оценка за ВКР</p>
                        <div class="relative max-w-sm">
                            <select v-model="estimatesVKR" id="estimatesVKR"
                                class="bg-none border-dashed containercolorinfo text-sm rounded-3xl block w-44 ps-3 p-2.5 border-collapse"
                                @change="addEstimates()">
                                <option v-for="item in estimates" :key="item.id" :value="item.id">{{ item.name }}
                                </option>
                            </select>
                        </div>
                    </div>
                    <div class="border max-w-96 h-11 pl-5 pt-3 rounded-b-xl colorboxbottom overflow-x-auto">
                        <p class="cursordrop text-xs">{{ estimatesVKR_Title }}</p>
                    </div>
                </div>
                <div class="mt-5">
                    <div class="border max-w-96 h-28 pl-5 pt-5 rounded-t-xl colorboxinfo">
                        <p class="text-white font-medium text-lg pb-2">Дипломная оценка</p>
                        <div class="">
                            <select v-model="estimatesDip" id="estimatesDip"
                                class="bg-none border-dashed containercolorinfo text-sm rounded-3xl block w-44 ps-3 p-2.5 border-collapse"
                                @change="addEstimates()">
                                <option v-for="item in estimates_dip" :key="item.id" :value="item.id">{{ item.name }}
                                </option>
                            </select>
                        </div>
                    </div>
                    <div class="border max-w-96 h-11 pl-5 pt-3 rounded-b-xl colorboxbottom">
                        <p class="cursordrop text-xs"></p>
                    </div>
                </div>
                <div class="mt-5">
                    <div class="border max-w-96 h-28 pl-5 pt-5 rounded-t-xl colorboxinfo">
                        <p class="text-white font-medium text-lg pb-2">Дата присвоения квалификации</p>
                        <div class="relative max-w-sm">
                            <div class="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none">
                                <svg class="w-4 h-4 text-gray-500 dark:text-gray-400" aria-hidden="true"
                                    xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
                                    <path
                                        d="M20 4a2 2 0 0 0-2-2h-2V1a1 1 0 0 0-2 0v1h-3V1a1 1 0 0 0-2 0v1H6V1a1 1 0 0 0-2 0v1H2a2 2 0 0 0-2 2v2h20V4ZM0 18a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8H0v10Zm5-8h10a1 1 0 0 1 0 2H5a1 1 0 0 1 0-2Z" />
                                </svg>
                            </div>
                            <input v-model="currentDateEnd" id="datepicker_end" datepicker datepicker-buttons
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
            </div>
        </div>

        <!-- block for student and document -->
        <div>
            <div class="h-44 overflow-auto">
                <p class="text-white font-medium text-lg pb-2 text-start">Добавленные протоколы</p>
                <div v-for="item in filelist" :key="item.id" class="flex flex-row" v-on:click="GetInfoFromFile(item)">
                    <div class="flex flex-row mr-auto cursor-pointer">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                            style="color: #71717A;" stroke="currentColor" class="w-6 h-6 mr-1">
                            <path stroke-linecap="round" stroke-linejoin="round"
                                d="M19.5 14.25v-2.625a3.375 3.375 0 0 0-3.375-3.375h-1.5A1.125 1.125 0 0 1 13.5 7.125v-1.5a3.375 3.375 0 0 0-3.375-3.375H8.25m2.25 0H5.625c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 0 0-9-9Z" />
                        </svg>
                        <p class="text-white">{{ item.file_name }}</p>
                    </div>
                    <p style="color: #71717A;">{{ item.date }}</p>
                </div>
            </div>

            <div class="border" style="border-color: #71717A;"></div>

            <div class="mt-8 border rounded-t-xl px-5 py-4 colorboxinfo" style="border-color: #71717A;">
                <p class="text-white font-medium text-lg pb-2 text-start">Студенты</p>
                <div class="flex flex-row justify-between mt-7">
                    <p class="text-white">Заполненных студентов</p>
                    <p style="color: #71717A;">{{ count }} / {{ students.length }}</p>
                </div>
                <div class="w-full bg-gray-200 rounded-full dark:bg-gray-700 mt-1">
                    <div class="tbg text-xs font-medium text-black text-center p-0.5 leading-none rounded-full"
                        :style="{ 'width': wigth }"> {{ wigth }}</div>
                </div>
                <button v-if="wigth == '100.00%' && count == students.length"
                    class="tbg px-2 mt-2 w-full rounded-xl text-white" @click="DownloadDOCX">Скачать протокол</button>
            </div>
            <div class="overflow-auto border rounded-b-xl colorboxbottom max-h-60">
                <div v-for="item in students" :key="item.id"
                    class=" h-11 pl-5 pt-2 hover:bg-white rounded-xl cursor-pointer"
                    :class="{ 'bg-white': item === selectedItemDetails }" @click="toggleDetails(item)">
                    <p class="cursordrop text-lg">{{ item.name }}</p>
                </div>
            </div>
        </div>
    </div>







    <div v-for="item in questions" :key="item.id" :id="'popup-modal-update' + questions.indexOf(item)" tabindex="-1"
        class="hidden overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full">
        <div class="relative p-4 w-auto max-w-full max-h-full">
            <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">
                <button type="button" :id="'closeModal' + questions.indexOf(item)"
                    class="absolute top-3 end-2.5 text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white"
                    :data-modal-hide="'popup-modal-update' + questions.indexOf(item)">
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
                    <textarea v-model="textquestionModal" :id="'textdraftsModal' + questions.indexOf(item)"
                        class="resize rounded-md mt-1 mb-6 font-sans w-80 border-none bg-gray-100 p-3"
                        placeholder="Введите новый текст"></textarea>
                </div>
                <div class="flex items-center p-4 md:p-5 border-t border-gray-200 rounded-b dark:border-gray-600">
                    <button :data-modal-hide="'popup-modal-update' + questions.indexOf(item)" type="button"
                        :id="'delElem' + questions.indexOf(item)"
                        class="text-white bg-red-600 hover:bg-red-800 focus:ring-4 focus:outline-none focus:ring-red-300 dark:focus:ring-red-800 font-medium rounded-lg text-sm inline-flex items-center px-5 py-2.5 text-center">
                        Удалить
                    </button>
                    <button :data-modal-hide="'popup-modal-update' + questions.indexOf(item)" type="button"
                        :id="'updateInfo' + questions.indexOf(item)"
                        class="py-2.5 px-5 ms-3 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700">Обновить</button>
                </div>
            </div>
        </div>
    </div>



    <!-- Modals page -->
    <div id="AddFileStudents" tabindex="-1" aria-hidden="true"
        class="hidden overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full">
        <div class="relative p-4 w-full max-w-2xl max-h-full">
            <!-- Modal content -->
            <div class="relative bg-white rounded-lg shadow">
                <!-- Modal header -->
                <div class="flex items-center justify-between p-4 md:p-5 border-b rounded-t dark:border-gray-600">
                    <h3 class="text-xl font-semibold text-gray-900">
                        Загрузка протокола
                    </h3>
                    <button type="button"
                        class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white"
                        data-modal-hide="AddFileStudents">
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
                    <div class="flex items-center justify-center w-full">
                        <label for="dropzone-file"
                            class="flex flex-col items-center justify-center w-full h-64 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-50 dark:hover:bg-bray-800 dark:bg-gray-700 hover:bg-gray-100 dark:border-gray-600 dark:hover:border-gray-500 dark:hover:bg-gray-600">
                            <div class="flex flex-col items-center justify-center pt-5 pb-6">
                                <svg class="w-8 h-8 mb-4 text-gray-500 dark:text-gray-400" aria-hidden="true"
                                    xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 16">
                                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"
                                        stroke-width="2"
                                        d="M13 13h3a3 3 0 0 0 0-6h-.025A5.56 5.56 0 0 0 16 6.5 5.5 5.5 0 0 0 5.207 5.021C5.137 5.017 5.071 5 5 5a4 4 0 0 0 0 8h2.167M10 15V6m0 0L8 8m2-2 2 2" />
                                </svg>
                                <p class="mb-2 text-sm text-gray-500 dark:text-gray-400" id="textprotocol"><span
                                        class="font-semibold">Нажмите чтобы загрузить</span> или перетащите файл</p>
                                <p class="text-xs text-gray-500 dark:text-gray-400" id="textformatdata">DOCX</p>
                            </div>
                            <input @change="fileprotocol" id="dropzone-file" type="file" class="hidden" />
                        </label>
                    </div>
                </div>
                <!-- Modal footer -->
                <div class="flex items-center p-4 md:p-5 border-t border-gray-200 rounded-b dark:border-gray-600">
                    <button class="py-2.5 px-5 ms-3 text-sm font-medium tbg rounded-lg text-white"
                        @click="ImportProtocol()">
                        Добавить протокол
                    </button>
                    <button data-modal-hide="AddFileStudents" type="button"
                        class="py-2.5 px-5 ms-3 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700">Отмена</button>
                </div>
            </div>
        </div>
    </div>

    <div id="AddQuestionStudents" tabindex="-1" aria-hidden="true"
        class="hidden overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full">
        <div class="relative p-4 w-full max-w-2xl max-h-full">
            <!-- Modal content -->
            <div class="relative bg-white rounded-lg shadow">
                <!-- Modal header -->
                <div class="flex items-center justify-between p-4 md:p-5 border-b rounded-t dark:border-gray-600">
                    <h3 class="text-xl font-semibold text-gray-900 dark:text-white">
                        Добавление вопроса
                    </h3>
                    <button type="button" id="AddQuestionStudentsClouse"
                        class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white"
                        data-modal-hide="AddQuestionStudents">
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
                    <form class="max-w-sm">
                        <select v-model="idCommissionUser" id="underline_select"
                            class="block py-2.5 px-0 w-full text-sm text-gray-500 bg-transparent border-0 border-b-2 border-gray-200 appearance-none dark:text-gray-400 dark:border-gray-700 focus:outline-none focus:ring-0 focus:border-gray-200 peer">
                            <option v-for="item in UsersCommission" :key="item.id" :value="item.id">{{ item.user_name }}
                            </option>
                        </select>
                    </form>
                    <label for="message" class="block mb-2 text-sm font-medium text-white">Введите вопрос</label>
                    <textarea v-model="textQuestion" id="message" rows="4"
                        class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300"
                        placeholder="Ваш текст..."></textarea>
                </div>
                <!-- Modal footer -->
                <div class="flex items-center p-4 md:p-5 border-t border-gray-200 rounded-b dark:border-gray-600">
                    <button @click="AddQuestion()"
                        class="py-2.5 px-5 ms-3 text-sm font-medium tbg rounded-lg text-white">
                        Добавить вопрос
                    </button>
                    <button data-modal-hide="AddQuestionStudents" type="button" id="AddQuestionStudentsClouseModal"
                        class="py-2.5 px-5 ms-3 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700">Отмена</button>
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
import { Modal } from 'flowbite';
import FileServices from '../services/file.service';
import UserService from '../services/user.service';

export default {
    data() {
        return {
            adminUser: null,
            selectFile: null,
            selectFileDownload: null,
            selectNamePred: null,
            filelist: [],
            students: [],
            UsersCommission: [],
            selectedDate: '',
            selectedItems: [],
            selectedItemDetails: null,
            questions: [],
            idCommissionUser: null,
            textQuestion: null,
            estimates: [],
            estimates_dip: [],
            estimatesVKR: null,
            estimatesVKR_Title: '',
            estimatesDip: null,
            count: 0,
            wigth: '0%',
            message: '',
            currentDateStart: '',
            currentDateEnd: '',
            textquestionModal: '',
            stateuser: null
        }
    },
    mounted() {

        const today = new Date();
        const year = today.getFullYear();
        const month = String(today.getMonth() + 1).padStart(2, '0');
        const day = String(today.getDate()).padStart(2, '0');
        this.currentDateStart = `${year}-${month}-${day}`;
        this.currentDateEnd = `${year}-${month}-${day}`;

        FileServices.getfilelist().then(
            response => {
                this.filelist = response.data.file_list;
            }
        );
        UserService.getUserCommission().then(
            (response) => {
                this.UsersCommission = response.data.users_commission;
            }
        );
        UserService.getUserBoard().then(
            response => {
                this.adminUser = response.data.users[0].id_userbd;
            }
        );
    },
    methods: {
        fileprotocol(event) {
            const file = event.target.files[0];
            this.selectFile = file;
            if (this.selectFile != null) {
                document.getElementById('textprotocol').innerText = file.name;
                document.getElementById('textformatdata').innerText = '';
            }
        },
        ImportProtocol() {
            let formData = {
                file: this.selectFile
            }
            this.$store.dispatch("file/uploadfile", formData)
                .then(
                    response => {
                        if (response.status == "success") {
                            const $targetEl = document.getElementById("AddFileStudents");
                            const modal = new Modal($targetEl);
                            modal.hide();
                            FileServices.getfilelist().then(
                                response => {
                                    this.filelist = response.data.file_list;
                                }
                            );
                        }
                    }
                );
        },
        GetInfoFromFile(item) {
            this.wigth = "0%";
            this.selectFileDownload = null;
            this.questions = [];
            this.selectedItemDetails = null;
            this.selectFileDownload = item;
            FileServices.getdatefromfile(item).then(
                response => {
                    if (response.date_start != '') {
                        this.currentDateStart = response.date_start;
                    }
                    else {
                        const today = new Date();
                        const year = today.getFullYear();
                        const month = String(today.getMonth() + 1).padStart(2, '0');
                        const day = String(today.getDate()).padStart(2, '0');
                        this.currentDateStart = `${year}-${month}-${day}`;
                        this.currentDateEnd = `${year}-${month}-${day}`;
                    }
                }
            );
            FileServices.getinfofromfile(item).then(
                response => {
                    this.students = response.students;
                    this.count = 0;
                    this.students.forEach((element) =>
                        FileServices.checkstateuser(element).then(
                            response => {
                                if (response.state == true) {
                                    this.count += 1;
                                    this.wigth = ((this.count / this.students.length) * 100).toFixed(2) + '%';
                                }
                            }
                        )
                    );
                }
            );
        },
        SelectCommission(item, checked) {
            if (checked) {
                this.selectedItems.push(item);
            } else {
                const index = this.selectedItems.indexOf(item);
                if (index !== -1) {
                    this.selectedItems.splice(index, 1);
                }
            }
        },
        toggleDetails(item) {
            if (this.selectedItemDetails && this.selectedItemDetails.id === item.id) {
                this.selectedItemDetails = null;
                this.questions = [];
                this.estimates = [];
                this.estimates_dip = [];
                this.estimatesVKR = '';
                this.estimatesVKR_Title = '';
            } else {
                this.selectedItemDetails = item;
                this.questions = [];
                this.estimates = [];
                this.estimates_dip = [];
                this.estimatesVKR = '';
                this.estimatesVKR_Title = '';
                FileServices.getquestioncommission(item).then(
                    response => {
                        this.questions = response.questions;
                    }
                );
                FileServices.getestimates().then(
                    response => {
                        this.estimates = response.data.estimates;
                    }
                );
                FileServices.getestimatesdip().then(
                    response => {
                        this.estimates_dip = response.data.estimates;
                    }
                )
                FileServices.getestimatesuser(item).then(
                    response => {
                        if (response.estimates.length != 0) {
                            this.estimatesVKR = response.estimates[0].value;
                            this.estimatesVKR_Title = response.estimates[0].title;
                            this.estimatesDip = response.estimates[0].value_graduate;
                        }
                    }
                );
                this.count = 0;
                this.students.forEach((element) =>
                    FileServices.checkstateuser(element).then(
                        response => {
                            if (response.state == true) {
                                this.count += 1;
                                this.wigth = ((this.count / this.students.length) * 100).toFixed(2) + '%';
                            }
                        }
                    )
                );
                FileServices.getdatefromfile(this.selectFileDownload).then(
                    response => {
                        document.getElementById('datepicker_end').value = response.date_end;
                    }
                );
                FileServices.getstateuserbe(this.selectedItemDetails).then(
                    response => {
                        this.stateuser = response.state;
                    }
                );
            }
        },
        AddQuestionStudents() {
            const $targetEl = document.getElementById("AddQuestionStudents");
            const $buttonCloseModal = document.getElementById('AddQuestionStudentsClouse');
            const $buttonCloseModalButton = document.getElementById('AddQuestionStudentsClouseModal');
            const modal = new Modal($targetEl);
            modal.show();
            $buttonCloseModal.onclick = function () {
                modal.hide();
            };
            $buttonCloseModalButton.onclick = function () {
                modal.hide();
            };
        },
        AddQuestion() {
            if (this.selectedItemDetails != null && this.idCommissionUser != null && this.textQuestion != null) { //нужно дописать исключение
                let formData = {
                    idUserCommission: this.idCommissionUser,
                    idStudent: this.selectedItemDetails.id,
                    textQuestion: this.textQuestion
                };
                this.$store.dispatch('file/addquestioncommission', formData).then(
                    response => {
                        if (response.status == 'success') {
                            const $targetEl = document.getElementById("AddQuestionStudents");
                            const modal = new Modal($targetEl);
                            modal.hide();
                            FileServices.getquestioncommission(this.selectedItemDetails).then(
                                response => {
                                    this.questions = response.questions;
                                }
                            );
                        }
                    }
                );
            }
        },
        addEstimates() {
            let formData = {
                student_id: this.selectedItemDetails.id,
                score_gw: this.estimatesVKR,
                score_g: this.estimatesDip
            };
            this.$store.dispatch('file/updateestimatesuser', formData).then(
                response => {
                    if (response.status == 'success') {
                        FileServices.getestimatesuser(this.selectedItemDetails).then(
                            response => {
                                this.estimatesVKR = response.estimates[0].value;
                                this.estimatesVKR_Title = response.estimates[0].title;
                                this.estimatesDip = response.estimates[0].value_graduate;
                            }
                        );
                        this.count = 0;
                        this.students.forEach((element) =>
                            FileServices.checkstateuser(element).then(
                                response => {
                                    if (response.state == true) {
                                        this.count += 1;
                                        this.wigth = ((this.count / this.students.length) * 100).toFixed(2) + '%';
                                    }
                                }
                            )
                        );
                    }
                }
            );
            this.students.forEach((element) =>
                FileServices.checkstateuser(element).then(
                    response => {
                        this.count = 0;
                        if (response.state == true) {
                            this.count += 1;
                            this.wigth = (this.count / this.students.length) * 100 + '%';
                        }
                    }
                )
            );
        },
        DownloadDOCX() {
            this.selectedDate = document.getElementById('datepicker').value;
            let filteredUsersCommission;
            if (this.selectNamePred !== null) {
                filteredUsersCommission = this.UsersCommission.filter(user => {
                    return !this.selectNamePred.includes(user.user_name);
                });
            } else {
                filteredUsersCommission = this.UsersCommission;
            }
            let formData = {
                userbd: this.adminUser,
                fileID: this.selectFileDownload.id,
                date: this.selectedDate,
                namepred: this.selectNamePred,
                userscommission: filteredUsersCommission
            }
            this.$store.dispatch('file/downloadfile', formData).then(
                response => {
                    if (response.status == 'success') {
                        location.href = 'http://127.0.0.1:83/downloadfile?id=' + this.selectFileDownload.id;
                    }
                },
                (error) => {
                    this.message = 'Проверьте, заполнено ли поле "Председатель ГЭК"';
                    setTimeout(() => {
                        this.message = '';
                    }, 5000);
                }
            )
        },
        updateQuestion(item) {
            const $targetEl = document.getElementById('popup-modal-update' + this.questions.indexOf(item));
            const $buttonCloseModal = document.getElementById('closeModal' + this.questions.indexOf(item));
            const $buttonUpdateInfo = document.getElementById('updateInfo' + this.questions.indexOf(item));
            const $buttonDelElem = document.getElementById('delElem' + this.questions.indexOf(item));
            const modal = new Modal($targetEl);
            this.textquestionModal = item.title;
            modal.show();
            $buttonCloseModal.onclick = function () {
                modal.hide();
            };
            var array = this.questions;
            var request = this.$store;
            var itemStudent = this.selectedItemDetails;
            $buttonUpdateInfo.onclick = () => {
                const old_text = item.title;
                const new_text = document.getElementById('textdraftsModal' + array.indexOf(item)).value;
                let formData = {
                    old_text: old_text,
                    new_text: new_text
                }
                request.dispatch('file/updateDataQuestion', formData).then(
                    response => {
                        if (response.status == 'success') {
                            FileServices.getquestioncommission(itemStudent).then(
                                response => {
                                    this.questions = response.questions;
                                }
                            );
                        }
                    }
                );
                modal.hide();
            };
            $buttonDelElem.onclick = () => {
                let formData = {
                    name: item.name,
                    data: item.title
                }
                this.$store.dispatch('file/delquestioncommission', formData).then(
                    response => {
                        if (response.status == 'success') {
                            FileServices.getquestioncommission(itemStudent).then(
                                response => {
                                    this.questions = response.questions;
                                }
                            );
                            this.count = 0;
                            this.students.forEach((element) =>
                                FileServices.checkstateuser(element).then(
                                    response => {
                                        if (response.state == true) {
                                            this.count += 1;
                                            this.wigth = ((this.count / this.students.length) * 100).toFixed(2) + '%';
                                        }
                                    }
                                )
                            );
                        }
                    }
                );
                modal.hide();
            }
        },
        addBe(event) {
            let formData = {
                student_id: this.selectedItemDetails.id,
                state: event.target.value
            }
            this.$store.dispatch('file/updatestateuser', formData).then(
                response => {
                    if (response.status == 'success') {
                        FileServices.getstateuserbe(this.selectedItemDetails).then(
                            response => {
                                this.stateuser = response.state;
                            }
                        );
                    }
                }
            );
        }
    }
}

</script>