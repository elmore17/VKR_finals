import { createApp } from 'vue'
import App from './App.vue'
import Authorization from './components/Authorization.vue';
import Registration from './components/Registration.vue';
import { createRouter, createWebHistory } from "vue-router"
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
    }
]

const router = createRouter({
history : createWebHistory(),
routes : routeInfos
})

export default router;