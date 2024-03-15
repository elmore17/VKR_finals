<template>
  <form  class="container mx-auto bg-white mt-36 flex flex-col items-center w-96 h-auto rounded-2xl">
    <img src="/WhiteLogo.svg" class="logo mt-7" alt="kis logo" />
    <h1 class="text font-sans text-sm font-bold">Авторизация</h1>
    <input v-model="login"  type="text" placeholder="Логин" class="mt-16 mb-6 font-sans w-80 border-none bg-gray-100 p-3 rounded">
    <input v-model="password" type="password" placeholder="Пароль" class="mb-20 font-sans w-80 border-none bg-gray-100 p-3 rounded">
    <button type="submit" @click.prevent = "onSubmit"  class="mb-3 text-white tbg w-48 pt-1 pb-1 rounded font-sans">Войти</button>
    <a href="/registration" class="mb-7 font-sans text-slate-500/60">Зарегистрироваться</a>
  </form>
</template>

<script>
export default{
  name: 'Authorization',
  data() {
    return {
      login: '',
      password: '',
    }
  },
  computed:{
    loggedIn(){
      return this.$store.state.auth.status.loggedIn;
    },
  },
  created(){
    if(this.loggedIn){
      return this.$router.push('/registration');
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
          this.$router.push("/registration");
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
</style>
