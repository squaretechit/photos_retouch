<script>
    export default {
        data: () => ({
            VEmail: '',
            VErrors: {},
            VSuccessMessage: ''
        }),
        methods: {
            // Send Data To Server
            SubmitFormToServer() {
                this.$axios.post('/email/',{"email": this.VEmail})
                .then(response => {
                    this.VSuccessMessage = response.data['message']
                    this.VEmail = '';
                }).catch(err => console.log(err.message))
            },
            // Check Valid Email
            validEmail(email) {
                let re =
                    /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
                return re.test(email);
            },
            // Submit Subscription Email
            subscriptions() {
                this.VErrors = {};
                if (!this.VEmail) {
                    this.VErrors['Subscription'] = 'Email Required.';
                } else if (!this.validEmail(this.VEmail)) {
                    this.VErrors['Subscription'] = 'Please use a valid Email.';
                }
                if (!this.VErrors['Subscription']) {
                    this.SubmitFormToServer();
                }
                setTimeout(()=>{
                    this.VErrors = {};
                }, 5000);
            }
        },
        mounted() {

        }
    }
</script>

<template>
    <footer class="footer-area footer-black">
        <div class="container">
            <div class="row">
                <div class="col-lg-4 col-md-5">
                    <div class="widget footer-col logo-col">
                        <div class="footer-logo">
                            <img loading="lazy" decoding="async" src="@/static/images/logo.png" alt="Footer Logo">
                        </div>
                        <p>We were founded in 2015 to solve local photography. Now We have an expert photo editing team to continue to provide support to our clients not only locally, but it's also worldwide. </p>
                        <ul>
                            <li><a href="#"><i class="fa fa-pinterest-p"></i></a></li>
                            <li><a href="#"><i class="fa fa-twitter"></i></a></li>
                            <li><a href="#"><i class="fa fa-facebook-f"></i></a></li>
                            <li><a href="#"><i class="fa fa-instagram"></i></a></li>
                        </ul>
                    </div>
                </div>
                <div class="col-lg-6 col-md-5">
                    <div class="widget footer-col subscribe-col">
                        <h4>Get the latest information about Offers & Promotion</h4>
                        <p v-if="VSuccessMessage" class="success-message">{{VSuccessMessage}}</p>
                        <form @submit.prevent="subscriptions" novalidate>
                            <input :class="{subscriptionInputError: VErrors.Subscription}" v-model="VEmail" type="email"
                                class="form-control" placeholder="Email">
                            <p v-if="VErrors.Subscription" class="subscription-error">{{ VErrors.Subscription }}</p>
                            <button class="btn btn-primary my-btn" type="submit">Subscribe</button>
                        </form>
                    </div>
                </div>
                <div class="col-lg-2 col-md-2">
                    <div class="widget footer-col footer-menu">
                        <h5>Quick link</h5>
                        <ul>
                            <li>
                                <router-link :to="{name:'about'}" >About</router-link>
                            </li>
                            <li>
                                <router-link :to="{name:'service'}" >Services</router-link>
                            </li>
                            <li>
                                <router-link :to="{name:'blog'}" >Blogs</router-link>
                            </li>
                            <li>
                                <a href="/sitemap.xml" target="_blank">Sitemap</a>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col-lg-12">
                    <p class="copy-right">&copy; {{ new Date().getFullYear() }} by <a target="blank" class="text-white"
                            href="https:squaretechit.com/">Square Tech IT</a></p>
                </div>
            </div>
        </div>
        <div class="cameraman-two-img">
            <img loading="lazy" decoding="async" src="@/static/images/FooterComp/camera-man-2.png" alt="Camera Man 2">
        </div>
        <div class="cameraman-three-img">
            <img loading="lazy" decoding="async" src="@/static/images/FooterComp/camera-man-3.png" alt="Camera Man 3">
        </div>
    </footer>
</template>

<style scoped>
    .success-message {
        color: green;
        text-align: center;
        margin-bottom: 10px;
    }
    .subscription-error {
        color: red;
    }

    .subscriptionInputError {
        margin-bottom: 0 !important;
    }

    .footer-logo {
        width: 200px;
    }

    .footer-logo img {
        height: 100%;
        width: 100%;
    }

    .footer-area {
        padding: 70px 0 60px;
        background: #F3F3F3;
    }

    .logo-col p {
        color: #3c3746;
        margin-bottom: 45px;
    }

    .logo-col ul li {
        display: inline-block;
        margin-right: 10px;
    }

    .logo-col ul li a i {
        width: 55px;
        height: 55px;
        background: #ffffff;
        text-align: center;
        font-size: 18px;
        color: #ccc9c9;
        line-height: 55px;
        -webkit-border-radius: 50%;
        -moz-border-radius: 50%;
        -ms-border-radius: 50%;
        -o-border-radius: 50%;
        border-radius: 50%;
        -webkit-transition: all 0.3s ease-in-out;
        -moz-transition: all 0.3s ease-in-out;
        -o-transition: all 0.3s ease-in-out;
        -ms-transition: all 0.3s ease-in-out;
        transition: all 0.3s ease-in-out;
    }

    .logo-col ul li a i:hover {
        color: #ffffff;
        background: #3FEEF7;
        -webkit-transition: all 0.3s ease-in-out;
        -moz-transition: all 0.3s ease-in-out;
        -o-transition: all 0.3s ease-in-out;
        -ms-transition: all 0.3s ease-in-out;
        transition: all 0.3s ease-in-out;
    }

    .subscribe-col {
        padding: 0 100px 0 110px;
    }

    .subscribe-col h4 {
        font-size: 20px;
        line-height: 28px;
        font-weight: 500;
        margin-bottom: 30px;
        padding-top: 45px;
    }

    .subscribe-col .form-control {
        height: 65px;
        border: none;
        margin-bottom: 20px;
    }

    .subscribe-col .my-btn {
        background: #3FEEF7;
        color: #ffffff;
    }

    .subscribe-col .my-btn:before {
        background: #2791bf;
    }

    .footer-menu {
        padding-left: 50px;
    }

    .footer-menu h5 {
        margin-top: 45px;
        margin-bottom: 50px;
        font-size: 20px;
        color: #393939;
    }

    .footer-menu ul li a {
        color: #393939;
    }

    .footer-menu ul li a:hover {
        color: #3FEEF7;
    }

    .copy-right {
        margin-top: 10px;
        color: #393939;
    }

    /* Black Footer CSS */

    .footer-black {
        background: #0E0F13;
        padding-top: 100px;
        position: relative;
    }

    .footer-black .logo-col p {
        color: #ffffff;
    }

    .footer-black .logo-col ul li a i {
        background: #161624;
        color: #ffffff;
    }

    .footer-black .logo-col ul li a i:hover {
        background: #2791bf;
    }

    .footer-black .subscribe-col h4 {
        color: #ffffff;
    }

    .footer-black .subscribe-col .form-control {
        background: #13131B;
        color: #ffffff;
    }

    .footer-black .footer-menu h5 {
        color: #ffffff;
    }

    .footer-black .footer-menu ul li a {
        color: #ffffff;
    }

    .footer-black .copy-right {
        color: #ffffff;
    }

    .cameraman-two-img {
        position: absolute;
        left: 200px;
        bottom: 0;
        z-index: 0;
    }

    .cameraman-three-img {
        position: absolute;
        right: 160px;
        bottom: 0;
        z-index: 0;
    }

    @media all and (max-width: 768px) {
        .subscribe-col {
            padding: 0;
        }

        .footer-menu {
            padding-left: 0;
        }
    }
</style>