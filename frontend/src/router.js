import { createApp } from 'vue'
import App from './App.vue'
import Authorization from './components/Authorization.vue';
import Registration from './components/Registration.vue';
import { createRouter, createWebHistory } from "vue-router"
import MainPage from './components/MainPage.vue';

const routeInfos = [
    {
        path : "/",
        name: Authorization,
        component : Authorization
    },
    {
        path : "/registration",
        name: Registration,
        component : Registration
    },
    {
        path: "/mainpage",
        name: MainPage,
        component: MainPage
    }
]

const router = createRouter({
history : createWebHistory(),
routes : routeInfos
})

router.beforeEach((to, from, next) => {
    const publicPages = ['/', '/registration'];
    const authRequired = !publicPages.includes(to.path);
    const loggedIn = localStorage.getItem('user');
  
    // trying to access a restricted page + not logged in
    // redirect to login page
    if (authRequired && !loggedIn) {
      next('/login');
    } else {
      next();
    }
});

export default router;