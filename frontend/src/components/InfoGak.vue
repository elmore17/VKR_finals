<template>
<div class="container mx-auto mt-7 grid grid-cols-3 gap-8">
        <!-- block for adding info -->
        <div class="col-span-2">
            <div class="flex flex-row items-center">
                <div class="mr-3">
                    <p class="text-white font-medium text-xl">Заполнение информации</p>
                </div>
                <button data-modal-target="AddFileStudents" data-modal-toggle="AddFileStudents"  class="flex flex-row items-center tbg px-2 rounded-xl">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-3 h-3">
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
                                <svg class="w-4 h-4 text-gray-500 dark:text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
                                    <path d="M20 4a2 2 0 0 0-2-2h-2V1a1 1 0 0 0-2 0v1h-3V1a1 1 0 0 0-2 0v1H6V1a1 1 0 0 0-2 0v1H2a2 2 0 0 0-2 2v2h20V4ZM0 18a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8H0v10Zm5-8h10a1 1 0 0 1 0 2H5a1 1 0 0 1 0-2Z"/>
                                </svg>
                            </div>
                            <input id="datepicker" datepicker datepicker-buttons datepicker-autohide datepicker-autoselect-today datepicker-format="yyyy-mm-dd" type="text" class="bg-none border-dashed containercolorinfo text-sm rounded-3xl block w-44 h-7 ps-10 p-2.5 border-collapse" placeholder="Выберете дату">
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
                            <input v-model="selectNamePred"  type="text" list="names" class="bg-none border-dashed containercolorinfo text-sm rounded-3xl block w-44 h-7 ps-3 p-2.5 border-collapse" placeholder="ФИО">
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
                            <p class="text-white font-medium text-lg pb-2">Члены ГЭК</p>
                            <button data-dropdown-toggle="AddGosCommission"  class="flex flex-row items-center tbg px-2 mr-5 rounded-xl">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-3 h-3">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M12 4.5v15m7.5-7.5h-15" />
                                </svg>
                                Добавить
                            </button>
                        </div>
                    </div>
                    <div class="flex flex-col flex-wrap content-start border h-11 pl-5 pt-3 rounded-b-xl colorboxbottom overflow-x-auto">
                        <p v-for="item in selectedItems" :key="item.id"  class="cursordrop text-xs mr-1">{{item.user_name}},</p>
                    </div>
                </div>
                <div class="mt-5 col-span-2">
                    <div class="border h-28 pl-5 pt-5 rounded-t-xl colorboxinfo">
                        <div class="flex justify-between flex-nowrap items-start">
                            <p class="text-white font-medium text-lg pb-2">Вопросы</p>
                            <button data-modal-target="AddQuestionStudents" data-modal-toggle="AddQuestionStudents"  class="flex flex-row items-center tbg px-2 mr-5 rounded-xl">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-3 h-3">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M12 4.5v15m7.5-7.5h-15" />
                                </svg>
                                Добавить
                            </button>
                        </div>
                    </div>
                    <div class="border h-11 pl-5 pt-3 rounded-b-xl colorboxbottom overflow-x-auto">
                        <div v-for="item in questions" class="cursor-pointer hover:font-extralight">
                            <p :key="item.title" class="cursordrop text-xs mr-1">{{ item.name }} - {{ item.title }}</p>
                        </div>    
                    </div>
                </div>
            </div>
            <div v-if="selectedItemDetails != null" class="grid grid-cols-2 mt-5  gap-5 max-w-3xl">
                <div class="mt-5">
                    <div class="border max-w-96 h-28 pl-5 pt-5 rounded-t-xl colorboxinfo">
                        <p class="text-white font-medium text-lg pb-2">Оценка за ВКР</p>
                        <div class="relative max-w-sm">
                            <select v-model="estimatesVKR" id="estimatesVKR" class="bg-none border-dashed containercolorinfo text-sm rounded-3xl block w-44 ps-3 p-2.5 border-collapse" @change="addEstimates()">
                                <option v-for="item in estimates" :key="item.id" :value="item.id">{{ item.name }}</option>
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
                            <select v-model="estimatesDip" id="estimatesDip" class="bg-none border-dashed containercolorinfo text-sm rounded-3xl block w-44 ps-3 p-2.5 border-collapse" @change="addEstimates()">
                                <option v-for="item in estimates_dip" :key="item.id"  :value="item.id">{{ item.name }}</option>
                            </select>
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
            <div class="h-44">
            <p class="text-white font-medium text-lg pb-2 text-start">Добавленные протоколы</p>
            <div v-for="item in filelist" :key="item.id"  class="flex flex-row" v-on:click="GetInfoFromFile(item)">
                <div  class="flex flex-row mr-auto cursor-pointer">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" style="color: #71717A;"  stroke="currentColor" class="w-6 h-6 mr-1">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M19.5 14.25v-2.625a3.375 3.375 0 0 0-3.375-3.375h-1.5A1.125 1.125 0 0 1 13.5 7.125v-1.5a3.375 3.375 0 0 0-3.375-3.375H8.25m2.25 0H5.625c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 0 0-9-9Z" />
                    </svg>
                    <p class="text-white">{{item.file_name}}</p>
                </div>
                    <p style="color: #71717A;">03.03.24</p>
                </div>
            </div>
            
            <div class="border" style="border-color: #71717A;"></div>
            
            <div class="mt-8 border rounded-t-xl px-5 py-4 colorboxinfo" style="border-color: #71717A;">
                <p class="text-white font-medium text-lg pb-2 text-start">Студенты</p>
                <div class="flex flex-row justify-between mt-7">
                    <p class="text-white">Заполненных студентов</p>
                    <p style="color: #71717A;">{{ count }} / {{ students.length }}</p>
                </div>
                <div  class="w-full bg-gray-200 rounded-full dark:bg-gray-700 mt-1">
                    <div class="tbg text-xs font-medium text-blue-100 text-center p-0.5 leading-none rounded-full" :style="{'width': wigth}"> {{ wigth }}</div>
                </div>
                <button v-if="wigth == '100%'" class="tbg px-2 mt-2 w-full rounded-xl" @click="DownloadDOCX">Скачать протокол</button>
            </div>
            <div class="overflow-auto border rounded-b-xl colorboxbottom max-h-60">
                <div v-for="item in students" :key="item.id" class=" h-11 pl-5 pt-2 hover:bg-white rounded-b-xl cursor-pointer" :class="{ 'bg-white': item === selectedItemDetails }" @click="toggleDetails(item)">
                    <p class="cursordrop text-lg">{{item.name}}</p>
                </div>
            </div>
        </div>
    </div>


    <!-- Modals page -->
    <div id="AddFileStudents" tabindex="-1" aria-hidden="true" class="hidden overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full">
        <div class="relative p-4 w-full max-w-2xl max-h-full">
            <!-- Modal content -->
            <div class="relative colorboxinfo rounded-lg shadow">
                <!-- Modal header -->
                <div class="flex items-center justify-between p-4 md:p-5 border-b rounded-t dark:border-gray-600">
                    <h3 class="text-xl font-semibold text-white">
                        Загрузка протокола
                    </h3>
                    <button type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white" data-modal-hide="AddFileStudents">
                        <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"/>
                        </svg>
                        <span class="sr-only">Close modal</span>
                    </button>
                </div>
                <!-- Modal body -->
                <div class="p-4 md:p-5 space-y-4">
                    <div class="flex items-center justify-center w-full">
                        <label for="dropzone-file" class="flex flex-col items-center justify-center w-full h-64 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-50 dark:hover:bg-bray-800 dark:bg-gray-700 hover:bg-gray-100 dark:border-gray-600 dark:hover:border-gray-500 dark:hover:bg-gray-600">
                            <div class="flex flex-col items-center justify-center pt-5 pb-6">
                                <svg class="w-8 h-8 mb-4 text-gray-500 dark:text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 16">
                                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 13h3a3 3 0 0 0 0-6h-.025A5.56 5.56 0 0 0 16 6.5 5.5 5.5 0 0 0 5.207 5.021C5.137 5.017 5.071 5 5 5a4 4 0 0 0 0 8h2.167M10 15V6m0 0L8 8m2-2 2 2"/>
                                </svg>
                                <p class="mb-2 text-sm text-gray-500 dark:text-gray-400" id="textprotocol"><span class="font-semibold">Нажмите чтобы загрузить</span> или перетащите файл</p>
                                <p class="text-xs text-gray-500 dark:text-gray-400" id="textformatdata">DOCX</p>
                            </div>
                            <input @change="fileprotocol" id="dropzone-file" type="file" class="hidden" />
                        </label>
                    </div> 
                </div>
                <!-- Modal footer -->
                <div class="flex items-center p-4 md:p-5 border-t border-gray-200 rounded-b dark:border-gray-600">
                    <button  class="py-2.5 px-5 ms-3 text-sm font-medium tbg rounded-lg" @click="ImportProtocol()">
                    Добавить протокол
                    </button>
                    <button data-modal-hide="AddFileStudents" type="button" class="py-2.5 px-5 ms-3 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700">Отмена</button>
                </div>
            </div>
        </div>
    </div>


    <div id="AddGosCommission" class="z-10 hidden bg-white rounded-lg shadow w-60 dark:bg-gray-700">
        <ul class="h-48 px-3 pb-3 overflow-y-auto text-sm text-gray-700 dark:text-gray-200" aria-labelledby="dropdownSearchButton">
            <li v-for="item in UsersCommission" :key="item.id" >
                <div class="flex items-center p-2 rounded hover:bg-gray-100 dark:hover:bg-gray-600">
                    <input :id="`checkbox-item-`+ item.id" type="checkbox" value="" class="w-4 h-4 text-gray-900 bg-gray-100 border-gray-300 rounded focus:ring-black dark:focus:ring-blue-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500" @change="SelectCommission(item, $event.target.checked)">
                    <label :for="`checkbox-item-`+ item.id" class="w-full ms-2 text-sm font-medium text-gray-900 rounded dark:text-gray-300">{{item.user_name}}</label>
                </div>
            </li>
        </ul>
        <a href="#" class="flex items-center p-3 text-sm font-medium text-red-600 border-t border-gray-200 rounded-b-lg bg-gray-50 dark:border-gray-600 hover:bg-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:text-red-500 hover:underline">
            <svg class="w-4 h-4 me-2" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 18">
                <path d="M6.5 9a4.5 4.5 0 1 0 0-9 4.5 4.5 0 0 0 0 9ZM8 10H5a5.006 5.006 0 0 0-5 5v2a1 1 0 0 0 1 1h11a1 1 0 0 0 1-1v-2a5.006 5.006 0 0 0-5-5Zm11-3h-6a1 1 0 1 0 0 2h6a1 1 0 1 0 0-2Z"/>
            </svg>
            Удалить
        </a>
    </div>

    <div id="AddQuestionStudents" tabindex="-1" aria-hidden="true" class="hidden overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full">
        <div class="relative p-4 w-full max-w-2xl max-h-full">
            <!-- Modal content -->
            <div class="relative colorboxinfo rounded-lg shadow">
                <!-- Modal header -->
                <div class="flex items-center justify-between p-4 md:p-5 border-b rounded-t dark:border-gray-600">
                    <h3 class="text-xl font-semibold text-white">
                        Добавление вопроса
                    </h3>
                    <button type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white" data-modal-hide="AddQuestionStudents">
                        <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"/>
                        </svg>
                        <span class="sr-only">Close modal</span>
                    </button>
                </div>
                <!-- Modal body -->
                <div class="p-4 md:p-5 space-y-4">
                    <form class="max-w-sm">
                        <select v-model="idCommissionUser" id="underline_select" class="block py-2.5 px-0 w-full text-sm text-gray-500 bg-transparent border-0 border-b-2 border-gray-200 appearance-none dark:text-gray-400 dark:border-gray-700 focus:outline-none focus:ring-0 focus:border-gray-200 peer">
                            <option v-for="item in UsersCommission" :key="item.id" :value="item.id">{{item.user_name}}</option>
                        </select>
                    </form>
                    <label for="message" class="block mb-2 text-sm font-medium text-white">Введите вопрос</label>
                    <textarea v-model="textQuestion" id="message" rows="4" class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300" placeholder="Ваш текст..."></textarea>
                </div>
                <!-- Modal footer -->
                <div class="flex items-center p-4 md:p-5 border-t border-gray-200 rounded-b dark:border-gray-600">
                    <button @click="AddQuestion()" class="py-2.5 px-5 ms-3 text-sm font-medium tbg rounded-lg">
                        Добавить вопрос
                    </button>
                    <button data-modal-hide="AddQuestionStudents" type="button" class="py-2.5 px-5 ms-3 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700">Отмена</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { Modal } from 'flowbite';
import FileServices from '../services/file.service';
import UserService from '../services/user.service';
export default{
    data() {
        return {
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
            estimatesVKR: '',
            estimatesVKR_Title: '',
            estimatesDip: '',
            count: 0,
            wigth: '0%'
        }
    },
    mounted() {
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
    },
    methods:{
        fileprotocol(event){
            const file = event.target.files[0];
            this.selectFile = file;
            if(this.selectFile != null){
                document.getElementById('textprotocol').innerText = file.name;
                document.getElementById('textformatdata').innerText = '';
            }
        },
        ImportProtocol(){
            let formData = { 
                file: this.selectFile
            }
            this.$store.dispatch("file/uploadfile", formData)
                .then(
                response => {
                    if(response.status == "success"){
                        const $targetEl = document.getElementById("AddFileStudents");
                        const modal = new Modal($targetEl);
                        modal.hide();
                    }
                }
            );
        },
        GetInfoFromFile(item){
            this.selectFileDownload = null;
            this.selectFileDownload = item;
            FileServices.getinfofromfile(item).then(
                response => {
                    this.students = response.students;
                    this.count = 0;
                    this.students.forEach((element) => 
                        FileServices.checkstateuser(element).then(
                            response => {
                                if (response.state == true){
                                    this.count += 1;
                                    this.wigth = (this.count/this.students.length) * 100 + '%';
                                }
                            }
                        )
                    );
                }
            );
        },
        SelectCommission(item, checked){
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
                        if(response.estimates.length != 0){
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
                            if (response.state == true){
                                this.count += 1;
                                this.wigth = (this.count/this.students.length) * 100 + '%';
                            }
                        }
                    )
                );
            }
        },
        AddQuestion(){
            if(this.selectedItemDetails != null && this.idCommissionUser != null && this.textQuestion != null){ //нужно дописать исключение
                let formData = { 
                    idUserCommission: this.idCommissionUser,
                    idStudent: this.selectedItemDetails.id,
                    textQuestion: this.textQuestion
                };
                this.$store.dispatch('file/addquestioncommission', formData).then(
                    response => {
                        if(response.status == 'success'){
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
        addEstimates(){
            let formData = { 
                student_id: this.selectedItemDetails.id,
                score_gw: this.estimatesVKR,
                score_g: this.estimatesDip
            };
            this.$store.dispatch('file/updateestimatesuser', formData).then(
                response => {
                    if(response.status == 'success'){
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
                                    if (response.state == true){
                                        this.count += 1;
                                        this.wigth = (this.count/this.students.length) * 100 + '%';
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
                        if (response.state == true){
                            this.count += 1;
                            this.wigth = (this.count/this.students.length) * 100 + '%';
                        }
                    }
                )
            );
        },
        DownloadDOCX(){
            this.selectedDate = document.getElementById('datepicker').value;
            let formData = {
                fileID: this.selectFileDownload.id,
                date: this.selectedDate,
                namepred: this.selectNamePred,
                userscommission: this.UsersCommission
            }
            this.$store.dispatch('file/downloadfile', formData).then(
                response => {
                    console.log(response);
                }
            );
        }
    }
}

</script>