<script>
    export default {
        data: () => ({
            baseURL: '',
            service: [],
            allsliders: [],
            allportfolio: [],
            allgallery: [],
        }),
        computed: {
            currentservice () {
                const service = this.$store.state.services_info.find((service) => service.url === this.$route.params.singleservice);
                this.service = service;
                return service;
                }
        },
        methods: {
            SlideAfterBefore() {
                const container = document.querySelectorAll('.compration-container');
                const container2 = document.querySelectorAll('.comparisonSliderInput');
                for (let i = 0; i < container.length; i++) {
                    container2[i].addEventListener('input', (e) => {
                        container[i].style.setProperty('--position', `${e.target.value}%`);
                    })
                }
            },
            async GetAllSlider(){
                const response = await this.$axios.get('/service-sliders/');
                const allSliders = response.data;
                for (let i=0; i < allSliders.length; i++){
                    if (this.currentservice.id === allSliders[i].service){
                        this.allsliders.push(allSliders[i]);
                    }
                }
            },
            async GetPortfolio(){
                const response = await this.$axios.get('/service-portfolio/');
                const allportfolios = response.data;
                for (let i=0; i < allportfolios.length; i++){
                    if (this.currentservice.id === allportfolios[i].service){
                        this.allportfolio.push(allportfolios[i]);
                    }
                }
            },
            async GetGallery(){
                const response = await this.$axios.get('/service-gallery/');
                const allportfolios = response.data;
                for (let i=0; i < allportfolios.length; i++){
                    if (this.currentservice.id === allportfolios[i].service){
                        this.allgallery.push(allportfolios[i]);
                    }
                }
            },
        },
        mounted() {
            setTimeout(()=>{
                this.baseURL = this.$axios.defaults.baseURL;
                this.GetAllSlider();
                this.GetPortfolio();
                this.GetGallery();
            }, 1000);
            setTimeout(()=>{
                this.SlideAfterBefore();
            }, 3000);
        }
    }
</script>
<template>
    <div>
        <!-- carousel start -->
        <div class="single-service-carousel-section">
            <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
                <ol class="carousel-indicators">
                    <li data-target="#carouselExampleIndicators"
                    v-for="(slider, index) in allsliders" 
                    :key="slider.id" 
                    :data-slide-to="index"
                    :class="{active : index == 0}"></li>
                </ol>
                <div class="carousel-inner">
                    <div v-for="(slider, index) in allsliders"
                    :key="slider.id"
                    class="carousel-item"
                    :class="{active : index == 0}">
                        <img :src="baseURL+slider.slider_image" class="d-block w-100" alt="...">
                    </div>
                </div>
                <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
                    <span class="" aria-hidden="true"><i class="fa fa-angle-left" aria-hidden="true"></i></span>
                    <span class="sr-only">Previous</span>
                </a>
                <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
                    <span class="" aria-hidden="true"><i class="fa fa-angle-right" aria-hidden="true"></i></span>
                    <span class="sr-only">Next</span>
                </a>
            </div>
        </div>
        <!--body retouching services section start -->
        <div class="single-service-body-retouching-services-section">
            <div class="container inner-section d-flex flex-column justify-content-center align-items-center">
                <h2 class="my-4 custom-heading">{{service.name}}</h2>
                <span v-html="service.description"></span>
                <div class="my-4 btns-wrapper">
                    <Nuxt-link class="btn btn-primary my-btn" :to="{name:'contact'}">Try for Free</Nuxt-link>
                    <Nuxt-link class="btn btn-primary my-btn ml-3" :to="{name:'quote'}">Get a Quote</Nuxt-link>
                </div>
                <h3 class="mb-4 custom-heading">{{service.name}} We Provide:</h3>
                <div class="row img-comparison-slider-container">
                    <div class="col-lg-6 pr-4" v-for="portfolio in allportfolio" :key="portfolio.id">
                        <li>{{portfolio.title}}</li>
                        <p class="mb-3">{{portfolio.description}}</p>
                        <main>
                            <div class="compration-container">
                                <div class="image-container">
                                    <img class="image-before slider-image"
                                        :src="`${baseURL}${portfolio.before_image}`"
                                        alt="color photo" />
                                    <img class="image-after slider-image"
                                        :src="`${baseURL}${portfolio.after_image}`"
                                        alt="black and white" />
                                </div>
                                <!-- step="10" -->
                                <input type="range" min="0" max="100" value="50"
                                    aria-label="Percentage of before photo shown" class="slider comparisonSliderInput" />
                                <div class="slider-line" aria-hidden="true"></div>
                                <div class="slider-button" aria-hidden="true">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                                        class="bi bi-code" viewBox="0 0 16 16">
                                        <path
                                            d="M5.854 4.854a.5.5 0 1 0-.708-.708l-3.5 3.5a.5.5 0 0 0 0 .708l3.5 3.5a.5.5 0 0 0 .708-.708L2.707 8l3.147-3.146zm4.292 0a.5.5 0 0 1 .708-.708l3.5 3.5a.5.5 0 0 1 0 .708l-3.5 3.5a.5.5 0 0 1-.708-.708L13.293 8l-3.147-3.146z" />
                                    </svg>
                                </div>
                            </div>
                        </main>
                    </div>
                </div>
            </div>
        </div>
        <LazyHomeWorksComp />
        <!-- pro body editing section end -->
        <div class="single-services-gallery-section">
            <div class="py-5">
                <h3 class="my-4 text-center custom-heading">Body Retouching Examples in Full Size</h3>
                <div class="gallery">
                    <img v-for="gallery in allgallery" :key="gallery.id"
                    :src="`${baseURL}${gallery.image}`" 
                    alt="">
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
    /* carousel */
    .single-service-carousel-section {
        padding-top: 100px;
    }

    .single-service-carousel-section .carousel-indicators {
        gap: 8px;
    }

    .single-service-carousel-section .carousel-indicators li {
        background-color: transparent;
        width: 10px;
        height: 10px;
        border: 1px solid white;
        border-radius: 50%;
    }

    .single-service-carousel-section .carousel-indicators .active {
        background-color: white;
    }

    .single-service-carousel-section .carousel-control-prev,
    .single-service-carousel-section .carousel-control-next {
        width: 5%;
    }

    .single-service-carousel-section .carousel-control-prev span,
    .single-service-carousel-section .carousel-control-next span {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 35px;
        height: 35px;
        background-color: rgb(255, 255, 255);
        border-radius: 50%;
    }

    .single-service-carousel-section .carousel-control-prev span i,
    .single-service-carousel-section .carousel-control-next span i {
        font-size: 25px;
        color: black;
    }

    /* comparison slider css */
    .single-service-body-retouching-services-section .img-comparison-slider-container li {
        font-size: 16px;
        font-weight: 700;
    }

    .custom-heading {
        font-size: 28px;
        font-weight: 400;
    }

    .image-container img {
        display: block;
        max-width: 100%;
    }

    main {
        display: grid;
        place-items: center;
    }

    .compration-container {
        display: grid;
        place-content: center;
        position: relative;
        overflow: hidden;
        border-radius: 1rem;
        --position: 50%;
    }

    .image-container {
        max-width: 800px;
        max-height: 90vh;
    }

    .slider-image {
        width: 100%;
        height: 100%;
        object-fit: cover;
        object-position: left;
    }

    .image-before {
        position: absolute;
        inset: 0;
        width: var(--position);
    }

    .slider {
        position: absolute;
        inset: 0;
        cursor: pointer;
        opacity: 0;
        /* for Firefox */
        width: 100%;
        height: 100%;
    }

    .slider:focus-visible~.slider-button {
        outline: 5px solid black;
        outline-offset: 3px;
    }

    .slider-line {
        position: absolute;
        inset: 0;
        width: .2rem;
        height: 100%;
        background-color: #fff;
        left: var(--position);
        transform: translateX(-50%);
        pointer-events: none;
    }

    .slider-button {
        position: absolute;
        background-color: #fff;
        color: black;
        padding: .5rem;
        border-radius: 100vw;
        display: grid;
        place-items: center;
        top: 50%;
        left: var(--position);
        transform: translate(-50%, -50%);
        pointer-events: none;
        box-shadow: 1px 1px 1px hsl(0, 50%, 2%, .5);
    }

    /* how does it works section css */
    .single-service-body-retouching-services-section .btns-wrapper button,
    .how-it-work-section .btns-wrapper button {
        outline: none;
        font-size: 18px;
        padding: 10px 25px;
        border: 2px solid #ffb231;
    }

    .single-service-body-retouching-services-section .btns-wrapper .btn-1,
    .how-it-work-section .btns-wrapper .btn-1 {
        background-color: #ffb231;
    }

    .single-service-body-retouching-services-section .btns-wrapper .btn-2,
    .how-it-work-section .btns-wrapper .btn-2 {
        background-color: transparent;
        margin-left: 15px;
        transition: 0.3s;
    }

    .single-service-body-retouching-services-section .btns-wrapper .btn-2:hover,
    .how-it-work-section .btns-wrapper .btn-2:hover {
        background-color: #ffb231;
        color: white;
    }


    /* single services pricing table css */

    .single-services-pricing-table-section .pricing-table-cards-wrapper {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        justify-content: center;
        align-items: center;
        gap: 20px;
    }

    .single-services-pricing-table-section .pricing-card {
        border-radius: 0;
        border-top: 5px solid #c4c4c4;
        border-left: 0;
        border-right: 0;
        padding: 15px 20px 0;
        background-color: #f5f5f5;
    }

    .single-services-pricing-table-section .pricing-card .pricing-card-top {
        padding: 20px;
        text-align: center;
    }

    .single-services-pricing-table-section .pricing-card .pricing-card-list {
        padding: 10px 20px;
    }

    .single-services-pricing-table-section .pricing-card .pricing-card-list li {
        color: #4a1717;
        font-size: 16px;
    }

    .single-services-pricing-table-section .pricing-card .pricing-card-list li::before {
        content: "\2022";
        color: #666666;
        margin-right: 20px;
    }

    .single-services-pricing-table-section .pricing-card .view-examples-btn {
        background-color: #b6b6b6;
        display: block;
        padding: 10px 0;
        border: none;
        outline: none;
        text-decoration: none;
        color: #444;
        font-size: 18px;
        transition: .2s ease-in-out;
    }

    .single-services-pricing-table-section .pricing-card .view-examples-btn:hover {
        background-color: #f5a112;
        text-decoration: none;
        color: #fff;
    }

    .single-services-pricing-table-section .pricing-card .card-footer button {
        background-color: #ffb231;
        border: 2px solid #ffb231;
        font-size: 18px;
        position: relative;
        vertical-align: middle;
        padding: 10px 25px;
        transition: .2s ease-in-out;
        outline: 0;

    }

    .single-services-pricing-table-section .pricing-card .card-footer button:hover {
        background-color: #f5a112;
        border: 2px solid #f5a112;
        text-decoration: none;
    }

    /* pro body editing section css */
    .pro-body-editing-section .image-container {
        max-width: 100%;
        max-height: 90vh;
    }

    .pro-body-editing-section .image-container .correctionImg {
        position: absolute;
        object-fit: cover;
        opacity: 0;
    }

    .pro-body-editing-section .comparison-slider:hover .image-container .correctionImg {
        opacity: 1;
    }

    .pro-body-editing-section .comparison-slider:active .image-container .correctionImg {
        opacity: 0;
    }

    .pro-body-editing-section .comparison-slider-container button {
        background-color: #ffb231;
        border: 2px solid #ffb231;
        font-size: 18px;
        position: relative;
        vertical-align: middle;
        padding: 10px 25px;
        transition: .2s ease-in-out;
        outline: 0;
    }

    .pro-body-editing-section .comparison-slider-container button:hover {
        background-color: #f5a112;
        border: 2px solid #f5a112;
        text-decoration: none;
    }

    .pro-body-editing-section .details-container ul li::before {
        content: "\2022";
        color: #666666;
        margin-right: 20px;
    }

    /* single services gallery css */

    .single-services-gallery-section .gallery {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        align-items: center;
        gap: 20px;
    }
</style>