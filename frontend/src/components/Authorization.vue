<template>
  <form  class="container mx-auto bg-white mt-36 flex flex-col items-center w-96 h-auto rounded-2xl">
    <img src="/WhiteLogo.svg" class="logo mt-7" alt="kis logo" />
    <h1 class="text font-sans text-sm font-bold">Авторизация</h1>
    <input v-model="login"  type="text" placeholder="Логин" class="mt-16 mb-6 font-sans w-80 border-none bg-gray-100 p-3 rounded">
    <input v-model="password" type="password" placeholder="Пароль" class="mb-20 font-sans w-80 border-none bg-gray-100 p-3 rounded">
    <button type="submit" @click.prevent = "onSubmit"  class="mb-3 text-white tbg w-48 pt-1 pb-1 rounded font-sans">Войти</button>
    <a href="/registration" class="mb-7 font-sans text-slate-500/60">Зарегистрироваться</a>
  </form>
  <div v-if=" this.message != '' "  id="error" class="flex items-center p-4 mb-4 text-red-800 rounded-lg bg-red-50 dark:bg-gray-800 dark:text-red-400 absolute right-0 bottom-0 w-52" role="alert">
    <svg class="flex-shrink-0 w-4 h-4" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
      <path d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z"/>
    </svg>
    <span class="sr-only">Info</span>
    <div class="ms-3 text-sm font-medium">
      {{ this.message }}
    </div>
  </div>
</template>

<script>
export default{
  name: 'Authorization',
  data() {
    return {
      login: '',
      password: '',
      message: ''
    }
  },
  computed:{
    loggedIn(){
      return this.$store.state.auth.status.loggedIn;
    },
  },
  created(){
    if(this.loggedIn){
      return this.$router.push('/mainpage');
    }
  },
  methods:{
    onSubmit(){
      let formData = {
        login: this.login,
        password: this.password,
      }
      this.$store.dispatch("auth/login", formData).then(
        () => {
          this.$router.push("/mainpage");
        },
        (error) => {
          this.loading = false;
          this.message =
            'Неверный логин или пароль';
            setTimeout(() => {
                this.message = '';
            }, 5000);
        }
      );
    }
  }
}

</script>

<style>
body{
  background-color: #0F0F0F;
}
.text{
  color: rgba(45, 212, 191, 1);
}
.tbg{
  background: rgba(45, 212, 191, 1);
}
input::-webkit-input-placeholder {
    color: #ccc;
   } 
input::-moz-placeholder {
color: #ccc;
}

.containercolorinfo{
  color: #71717A;
  background-color: #0F0F0F;
}
</style>
