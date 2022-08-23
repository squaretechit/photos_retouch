<template>
    <section class="separator-area mt-5">
        <div class="container">
            <div class="row">
                <div class="col-lg-12">
                    <div class="separator-col">
                        <div class="banner-img">
                            <img loading="lazy" decoding="async"
                                src="@/static/images/HomeComp/ContactSeparatorComp/banner.jpeg" alt="Banner"
                                class="img-fluid">
                            <div class="banner-box">
                                <h5>Take time to know about us</h5>
                                <h2>Hello! We are Photos Retouch Team</h2>
                                <p class="text-justify">With our team of Photoeditors we strive to capture the true essence
                                    of your wedding story and tell it through still images and cinematic films.We are committed to operating in a professional manner, upholding the highest safety standards at all times. We always try to learning and improving reliable, punctual and trustworthy friendly and respectful at all times to each other.</p>
                            <Nuxt-link class="btn btn-primary my-btn" :to="{name:'about'}">About Us</Nuxt-link>
                            </div>
                        </div>
                        <img loading="lazy" decoding="async"
                            src="@/static/images/HomeComp/ContactSeparatorComp/pattren.png" alt="Left Pattren"
                            class="left-pattren">
                        <img loading="lazy" decoding="async"
                            src="@/static/images/HomeComp/ContactSeparatorComp/pattren.png" alt="Right Pattren"
                            class="right-pattren">
                    </div>
                </div>
            </div>
        </div>
        <div class="camaraman-img">
            <img loading="lazy" decoding="async" src="@/static/images/HomeComp/ContactSeparatorComp/camera-man.png"
                alt="Camera Man">
        </div>
    </section>
</template>

<style scoped>
    .banner-box h5,
    .banner-box h2,
    .banner-box p {
        color: #2791bf;
    }

    .banner-box .my-btn {
        color: #2791bf;
        border-color: #2791bf;
    }

    .banner-box .my-btn:before {
        background-color: #2791bf;
    }
</style>