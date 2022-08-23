<script>
    import TheHeaderVue from '@/components/TheHeader.vue';
    export default {
        name: "NotFoundView",
        components: {TheHeaderVue},
        mounted() {
            document.title = "Photos Retouch | Not Found";
            document.querySelector('#MainHeader').classList.add('header-two-area');
        }
    };
</script>

<template>
    <div>
        <TheHeaderVue/>
        <section class="mt-5 not-found-sec">
            <div class="container">
                <div class="not-found">
                    <h1>Not Found</h1>
                    <p>Oops, we couldn't find that page. Try going
                        <router-link to="/">HOME</router-link>
                    </p>
                </div>
            </div>
        </section>
    </div>
</template>

<style>
    .not-found-sec {
        padding-top: 160px;
    }
    .container .not-found a {
        color: #3EEDF6;
    }
</style>