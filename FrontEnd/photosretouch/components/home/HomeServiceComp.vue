<script>
    export default {
        data: () => ({
            BaseURL: ''
        }),
        computed: {
            AllServices () {return this.$store.state.services_info}
        },
        mounted() {
            this.BaseURL = this.$axios.defaults.baseURL;
        }
    }
</script>

<template>
    <section class="service-two-area home-service-background">
        <div id="animation">
            <div class="animation1">
                <img src="@/static/images/HomeComp/ServiceComp/ServiceBackgroundCircleAnimation.webp"
                    alt="Animation One">
            </div>
            <div class="animation2">
                <img src="@/static/images/HomeComp/ServiceComp/ServiceBackgroundCircleAnimation.webp"
                    alt="Animation Two">
            </div>
            <div class="animation3">
                <img src="@/static/images/HomeComp/ServiceComp/ServiceBackgroundCircleAnimation.webp"
                    alt="Animation Three">
            </div>
            <div class="animation4">
                <img src="@/static/images/HomeComp/ServiceComp/ServiceBackgroundCircleAnimation.webp"
                    alt="Animation Four">
            </div>
        </div>
        <div class="container">
            <div class="row">
                <div class="col-lg-5">
                    <div class="service-two-col clearfix">
                        <h2>The most comprehensive Photo Editing Services </h2>
                        <p>We are Photos Retouch, Photo editor with a real passion for creating beautiful images of all that we
                            editing with our team of Photographers & Photoeditors. We strive to capture the true
                            essence of your wedding story.</p>
                        <div v-for="service in AllServices.slice(0,1)" :key="service.id" class="service-two-box f-right">
                            <div class="service-two-icon">
                                <img loading="lazy" decoding="async" :src="BaseURL + service.service_simble" alt="Icon">
                            </div>
                            <h4>{{service.name}}</h4>
                            <p v-html="service.description"></p>
                        </div>
                    </div>
                </div>
                <div class="col-lg-7 custom-col">
                    <div class="row">
                        <div v-for="service in AllServices.slice(1,2)" :key="service.id" class="col-lg-6 custom-col">
                            <div class="service-two-box">
                                <div class="service-two-icon">
                                    <img loading="lazy" decoding="async" :src="BaseURL + service.service_simble" alt="Icon">
                                </div>
                                <h4>{{service.name}}</h4>
                                <p v-html="service.description"></p>
                            </div>
                        </div>
                        <div v-for="service in AllServices.slice(2,3)" :key="service.id" class="col-lg-6 custom-col">
                            <div class="service-two-box top-space">
                                <div class="service-two-icon">
                                    <img loading="lazy" decoding="async" :src="BaseURL + service.service_simble" alt="Icon">
                                </div>
                                <h4>{{service.name}}</h4>
                                <p v-html="service.description"></p>
                            </div>
                        </div>
                        <div v-for="service in AllServices.slice(3,4)" :key="service.id" class="col-lg-6 custom-col">
                            <div class="service-two-box to-top">
                                <div class="service-two-icon">
                                    <img loading="lazy" decoding="async" :src="BaseURL + service.service_simble" alt="Icon">
                                </div>
                                <h4>{{service.name}}</h4>
                                <p v-html="service.description"></p>
                            </div>
                        </div>
                        <div v-for="service in AllServices.slice(4,5)" :key="service.id" class="col-lg-6 custom-col">
                            <div class="service-two-box">
                                <div class="service-two-icon">
                                    <img loading="lazy" decoding="async" :src="BaseURL + service.service_simble" alt="Icon">
                                </div>
                                <h4>{{service.name}}</h4>
                                <p v-html="service.description"></p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<style scoped>
    .home-service-background {
        background-color: #2DA8CE;
        position: relative;
    }

    /* Animation One */
    @keyframes bg_anima1 {
        from {
            height: 40px;
            width: 40px;
        }

        to {
            height: 60px;
            width: 60px;
        }
    }

    #animation .animation1 {
        position: absolute;
        top: 10%;
        right: 10%;
        height: 70px;
        width: 70px;
        transition: all .8s ease;
        animation: bg_anima1 2s alternate infinite;
        -webkit-animation: bg_anima1 2s alternate infinite;
    }

    /* Animation Two */
    @keyframes bg_anima2 {
        from {
            height: 200px;
            width: 200px;
        }

        to {
            height: 220px;
            width: 220px;
        }
    }
    #animation .animation2 {
        position: absolute;
        top: 20%;
        left: 25%;
        height: 100px;
        width: 100px;
        transition: all .8s ease;
        animation: bg_anima3 2s alternate infinite;
        -webkit-animation: bg_anima3 2s alternate infinite;
    }

    /* Animation Three */
    @keyframes bg_anima3 {
        from {
            height: 100px;
            width: 100px;
        }

        to {
            height: 150px;
            width: 150px;
        }
    }

    #animation .animation3 {
        position: absolute;
        bottom: 10%;
        left: 10%;
        height: 200px;
        width: 200px;
        transition: all .8s ease;
        animation: bg_anima2 2s alternate infinite;
        -webkit-animation: bg_anima2 2s alternate infinite;
    }
    /* Animation Four */
    @keyframes bg_anima4 {
        from {
            height: 250px;
            width: 250px;
        }

        to {
            height: 350px;
            width: 350px;
        }
    }

    #animation .animation4 {
        position: absolute;
        bottom: 10%;
        right: 10%;
        height: 250px;
        width: 250px;
        transition: all .8s ease;
        animation: bg_anima4 2s alternate infinite;
        -webkit-animation: bg_anima4 2s alternate infinite;
    }

    .animation1 img,
    .animation2 img,
    .animation3 img,
    .animation4 img {
        height: 100%;
        width: 100%;
    }


    .service-two-box .service-two-icon:before {
        background: #2DA8CE;
    }
</style>