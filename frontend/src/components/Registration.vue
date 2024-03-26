<template>
    <form class="container mx-auto bg-white mt-32 flex flex-col items-center w-96 h-auto rounded-2xl">
      <img src="/WhiteLogo.svg" class="logo mt-7" alt="kis logo" />
      <h1 class="text font-sans text-sm font-bold">Регистрация</h1>
      <input v-model="login"  type="text" placeholder="Логин" class="mt-16 mb-6 font-sans w-80 border-none bg-gray-100 p-3 rounded">
      <input v-model="name"  type="text" placeholder="ФИО" class="mb-6 font-sans w-80 border-none bg-gray-100 p-3 rounded">
      <input v-model="password1" type="password" placeholder="Пароль" class="mb-6 font-sans w-80 border-none bg-gray-100 p-3 rounded">
      <input v-model="password2" type="password" placeholder="Повторите пароль" class="mb-11 font-sans w-80 border-none bg-gray-100 p-3 rounded">
      <button type="submit" @click.prevent="onSubmit"  class="mb-3 text-white tbg w-48 pt-1 pb-1 rounded font-sans">Зарегистрироваться</button>
      <a href="/" class="mb-7 font-sans text-slate-500/60">Войти</a>
    </form>
</template>

<script>
export default{
    name: 'Registration',
    data(){
      return{
        login: '',
        name: '',
        password1: '',
        password2: ''
      }
    },
    computed:{
      loggedIn(){
        return this.$store.state.auth.status.loggedIn;
      },
    },
    mounted() {
      if (this.loggedIn) {
        this.$router.push("/");
      }
    },
    methods:{
      onSubmit(){
        let formData = {
          login: this.login,
          name: this.name,
          password1: this.password1,
          password2: this.password2
        }
        this.$store.dispatch("auth/register", formData).then(
          () => {
            this.$router.push("/");
          }
        );
      }
    }
}
</script>