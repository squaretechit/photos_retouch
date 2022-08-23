<script>
    import { ref } from "vue";
    import { baseURL } from "@/axios-api";
    import store from "@/store";
    export default {
        data: () => ({
            BaseURL: baseURL,
            AllServices: ref(store.state.services_info)
        })
    }
</script>

<template>
    <section class="service-area service-three-area">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-lg-6">
                    <div class="my-title">
                        <h2>Our Popular Services</h2>
                        <p>We are Ptoga photographers with a real passion for creating beautiful images of all that we photograph</p>
                    </div>
                </div>
            </div>
            <div class="row">
                <div v-for="service in AllServices" :key="service.id" class="col-lg-6">
                    <router-link :to="{name:'SingleService', params:{service_name: service.url}}">
                        <div class="service-col">
                            <img :src="BaseURL + service.service_simble" alt="Service Picture">
                            <h4 class="text-uppercase">{{service.name}}</h4>
                            <p class="text-black" v-html="service.description"></p>
                        </div>
                    </router-link>
                </div>
            </div>
        </div>
    </section>
</template>

<style>
    .text-black {
        color: #000;
    }
    .service-three-area .service-col {
        min-height: 250px;
    }
    .service-col h4 {
        font-size: 20px;
    }
    .service-col img {
        height: 130px;
        width: 130px;
    }
</style>