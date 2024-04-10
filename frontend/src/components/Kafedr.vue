<template>
    <NavBarKafedr />
    <InfoZK />
</template>

<script>
import NavBarKafedr from './NavBarKafedr.vue';
import InfoZK from './InfoZK.vue';

export default {
    name: 'Kafedr',
    components: {
        NavBarKafedr,
        InfoZK
    },
    data() {
        return {
            selectedSection: null
        };
    }
}
</script>

<style>
.colorboxinfo {
    background-color: #111111;
    border-color: #71717A;
}

.colorboxbottom {
    background-color: #09090B;
    border-color: #71717A;
}
</style>