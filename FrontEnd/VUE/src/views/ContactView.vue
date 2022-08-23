<script>
    import TheHeaderView from "@/components/TheHeader.vue"
    import ContactComp from "@/components/contactComp/ContactComp.vue";
    import ContactUsStartComp from "@/components/contactComp/ContactUsStartComp.vue";
    import HomeContactSeparatorComp from "@/components/homeComp/HomeContactSeparatorComp.vue";
    import FooterComp from "@/components/FooterComp.vue";
    export default {
        name: "ContactView",
        components: {
            TheHeaderView,
            ContactComp,
            ContactUsStartComp,
            HomeContactSeparatorComp,
            FooterComp
        },
        mounted() {
            document.title = "Photos Retouch | Contact";
            document.querySelector('#MainHeader').classList.remove('header-two-area');
        }
    };
</script>

<template>
    <div>
        <TheHeaderView />
        <ContactComp />
        <ContactUsStartComp />
        <HomeContactSeparatorComp />
        <FooterComp />
    </div>
</template>