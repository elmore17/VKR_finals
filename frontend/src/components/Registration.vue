<template>
  <form class="container mx-auto bg-white mt-20 flex flex-col items-center w-96 h-auto rounded-2xl">
    <img src="/WhiteLogo.svg" class="logo mt-7" alt="kis logo" />
    <h1 class="text font-sans text-sm font-bold">Регистрация</h1>
    <input v-model="login" type="text" placeholder="Логин"
      class="mt-16 mb-6 font-sans w-80 border-none bg-gray-100 p-3 rounded">
    <input v-model="name" type="text" placeholder="ФИО" class="mb-6 font-sans w-80 border-none bg-gray-100 p-3 rounded">
    <input v-model="kaf_name" list="departament" type="text" placeholder="Кафедра полное название"
      class="mb-6 font-sans w-80 border-none bg-gray-100 p-3 rounded">
    <datalist id="departament">
      <option v-for="item in name_drafts_departament" :key="item.id" :value=item.full_name></option>
    </datalist>
    <input v-model="role" list="role" type="text" placeholder="Введите должность"
      class="mb-6 font-sans w-80 border-none bg-gray-100 p-3 rounded">
    <datalist id="role">
      <option v-for="item in name_drafts_role" :key="item.id" :value=item.name></option>
    </datalist>
    <input v-model="password1" type="password" placeholder="Пароль"
      class="mb-6 font-sans w-80 border-none bg-gray-100 p-3 rounded">
    <input v-model="password2" type="password" placeholder="Повторите пароль"
      class="mb-11 font-sans w-80 border-none bg-gray-100 p-3 rounded">
    <button type="submit" @click.prevent="onSubmit"
      class="mb-3 text-white tbg w-48 pt-1 pb-1 rounded font-sans">Зарегистрироваться</button>
    <a href="/" class="mb-7 font-sans text-slate-500/60">Войти</a>
  </form>
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
import FileServices from '../services/file.service';
export default {
  name: 'Registration',
  data() {
    return {
      login: '',
      name: '',
      password1: '',
      password2: '',
      kaf_name: '',
      role: '',
      message: '',
      name_drafts_departament: [],
      name_drafts_role: []
    }
  },
  computed: {
    loggedIn() {
      return this.$store.state.auth.status.loggedIn;
    },
  },
  mounted() {
    if (this.loggedIn) {
      this.$router.push("/");
    }
    FileServices.getroleandmoreinfo().then(
      response => {
        this.name_drafts_departament = response.data.name_drafts_departament;
        this.name_drafts_role = response.data.name_drafts_role;
      }
    );
  },
  methods: {
    onSubmit() {
      let formData = {
        login: this.login,
        name: this.name,
        kaf_name: this.kaf_name,
        role: this.role,
        password1: this.password1,
        password2: this.password2
      }
      this.$store.dispatch("auth/register", formData).then(
        () => {
          this.$router.push("/");
        },
        (error) => {
          this.loading = false;
          this.message =
            'Такой пользователь уже существует';
          setTimeout(() => {
            this.message = '';
          }, 5000);
        }
      );
    }
  }
}
</script>