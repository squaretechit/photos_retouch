<script>
    import TheHeaderVue from "@/components/TheHeader.vue";
    import BlogComp from "@/components/blogComp/BlogComp.vue";
    import BlogStartComp from "@/components/blogComp/BlogStartComp.vue";
    import HomeContactSeparatorComp from "@/components/homeComp/HomeContactSeparatorComp.vue";
    import FooterComp from "@/components/FooterComp.vue";
    export default {
        name: "BlogView",
        components: {
            TheHeaderVue,
            BlogComp,
            BlogStartComp,
            HomeContactSeparatorComp,
            FooterComp
        },
        mounted() {
            document.title = "Photos Retouch | Blog";
            document.querySelector('#MainHeader').classList.remove('header-two-area');
        }
    };
</script>

<template>
    <div>
        <TheHeaderVue />
        <BlogComp />
        <BlogStartComp />
        <HomeContactSeparatorComp />
        <FooterComp />
    </div>
</template>