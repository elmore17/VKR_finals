<template>
    <NavBarKafedr />
</template>

<script>
import NavBarKafedr from './NavBarKafedr.vue';

export default {
    name: 'Kafedr',
    components: {
        NavBarKafedr,
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