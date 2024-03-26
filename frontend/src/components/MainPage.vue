<template>
    <NavBar />
    <InfoGak />
</template>

<script>
import NavBar from './NavBar.vue';
import InfoGak from './InfoGak.vue'

export default{
    name: 'MainPage',
    components: {
        NavBar,
        InfoGak,
    },
}
</script>

<style>
.colorboxinfo{
    background-color: #111111;
    border-color: #71717A;
}

.colorboxbottom{
    background-color: #09090B;
    border-color: #71717A;
}
</style>