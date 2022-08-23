<script>
    import TheHeaderVue from "@/components/TheHeader.vue";
    import serviceComp from "@/components/serviceComp/serviceComp.vue";
    import mainServiceComp from "@/components/serviceComp/mainServiceComp.vue";
    import HomeContactSeparatorComp from "@/components/homeComp/HomeContactSeparatorComp.vue";
    import FooterComp from "@/components/FooterComp.vue";
    export default {
        name: "ServiceView",
        components: {
            TheHeaderVue,
            serviceComp,
            mainServiceComp,
            HomeContactSeparatorComp,
            FooterComp
        },
        mounted() {
            document.title = "Photos Retouch | Services";
            document.querySelector('#MainHeader').classList.remove('header-two-area');
        }
    };
</script>

<template>
    <div>
        <TheHeaderVue/>
        <serviceComp />
        <mainServiceComp />
        <HomeContactSeparatorComp />
        <FooterComp />
    </div>
</template>