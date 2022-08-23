<script>
    import { baseURL } from "@/axios-api";
    import store from "@/store";
    import TestimonialBg from "@/assets/images/AboutComp/AboutTestimonialComp/testimonial-bg.png";
    import QuotationBg from "@/assets/images/AboutComp/AboutTestimonialComp/quotation.png";
    export default {
        data: ()=>({
            TestimonialBg: TestimonialBg,
            QuotationBg: QuotationBg
        }),
        methods: {
            StartTestimoniaCarousel(){
                if ($('.testimonial-carousel').length) {
                    $('.testimonial-carousel').owlCarousel({
                        loop: true,
                        margin: 30,
                        dots: true,
                        nav: false,
                        autoplayHoverPause: false,
                        autoplay: true,
                        autoplayTimeout: 4000,
                        smartSpeed: 800,
                        center: false,
                        navText: [
                            '<i class="fa fa-long-arrow-down"></i>',
                            '<i class="fa fa-long-arrow-up"></i>'
                        ],
                        responsive: {
                            0: {
                                items: 1,
                                center: false
                            },
                            480: {
                                items: 1,
                                center: false
                            },
                            600: {
                                items: 1,
                                center: false
                            },
                            768: {
                                items: 2
                            },
                            992: {
                                items: 2
                            },
                            1200: {
                                items: 2
                            }
                        }
                    })
                }
            },
            GetTestimonial() {
                const Testimonials = store.state.client_review_info;
                for (let i=0; i < Testimonials.length; i++){
                    document.querySelector('.testimonial-carousel').innerHTML += `
                        <div class="testimonial-item">
                            <p>${Testimonials[i]['review']}</p>
                            <div class="testimonial-two-img">
                                <img src="${baseURL+Testimonials[i]['client_picture']}" alt="">
                                <span>${Testimonials[i]['client_name']}</span>
                            </div>
                            <img class="testimonial-pattrn" src="${this.TestimonialBg}" alt="Testimonial Background">
                            <img class="quotation-img" src="${this.QuotationBg}" alt="Quotation Background">
                        </div>`;
                }
                this.StartTestimoniaCarousel();
            }
        },
        mounted() {this.GetTestimonial();}
    }
</script>

<template>
    <section class="testimonial-two-area">
        <div class="container">
            <div class="row">
                <div class="col-lg-12">
                    <div class="testimonial-two-col">
                        <div class="testimonial-carousel">
                            <!-- <div class="testimonial-item">
                                <p>“ The images you captured were precise, natural and beautiful. We spent so much time
                                    with our guests due to the fact that you knew exactly the </p>
                                <div class="testimonial-two-img">
                                    <img src="@/assets/images/AboutComp/AboutTestimonialComp/testimonial-1.png" alt="">
                                    <span>Marri Alen</span>
                                </div>
                                <img class="testimonial-pattrn"
                                    src="@/assets/images/AboutComp/AboutTestimonialComp/testimonial-bg.png" alt="">
                                <img class="quotation-img"
                                    src="@/assets/images/AboutComp/AboutTestimonialComp/quotation.png" alt="">
                            </div> -->
                            <!-- <div class="testimonial-item">
                                <p>“ The images you captured were precise, natural and beautiful. We spent so much time
                                    with our guests due to the fact that you knew exactly the </p>
                                <div class="testimonial-two-img">
                                    <img src="@/assets/images/AboutComp/AboutTestimonialComp/testimonial-2.png" alt="">
                                    <span>Sharp Mard</span>
                                </div>
                                <img class="testimonial-pattrn"
                                    src="@/assets/images/AboutComp/AboutTestimonialComp/testimonial-bg.png" alt="">
                                <img class="quotation-img"
                                    src="@/assets/images/AboutComp/AboutTestimonialComp/quotation.png" alt="">
                            </div>
                            <div class="testimonial-item">
                                <p>“ The images you captured were precise, natural and beautiful. We spent so much time
                                    with our guests due to the fact that you knew exactly the </p>
                                <div class="testimonial-two-img">
                                    <img src="@/assets/images/AboutComp/AboutTestimonialComp/testimonial-1.png" alt="">
                                    <span>Marri Alen</span>
                                </div>
                                <img class="testimonial-pattrn"
                                    src="@/assets/images/AboutComp/AboutTestimonialComp/testimonial-bg.png" alt="">
                                <img class="quotation-img"
                                    src="@/assets/images/AboutComp/AboutTestimonialComp/quotation.png" alt="">
                            </div>
                            <div class="testimonial-item">
                                <p>“ The images you captured were precise, natural and beautiful. We spent so much time
                                    with our guests due to the fact that you knew exactly the </p>
                                <div class="testimonial-two-img">
                                    <img src="@/assets/images/AboutComp/AboutTestimonialComp/testimonial-2.png" alt="">
                                    <span>Sharp Mard</span>
                                </div>
                                <img class="testimonial-pattrn"
                                    src="@/assets/images/AboutComp/AboutTestimonialComp/testimonial-bg.png" alt="">
                                <img class="quotation-img"
                                    src="@/assets/images/AboutComp/AboutTestimonialComp/quotation.png" alt="">
                            </div>
                            <div class="testimonial-item">
                                <p>“ The images you captured were precise, natural and beautiful. We spent so much time
                                    with our guests due to the fact that you knew exactly the </p>
                                <div class="testimonial-two-img">
                                    <img src="@/assets/images/AboutComp/AboutTestimonialComp/testimonial-1.png" alt="">
                                    <span>Marri Alen</span>
                                </div>
                                <img class="testimonial-pattrn"
                                    src="@/assets/images/AboutComp/AboutTestimonialComp/testimonial-bg.png" alt="">
                                <img class="quotation-img"
                                    src="@/assets/images/AboutComp/AboutTestimonialComp/quotation.png" alt="">
                            </div>
                            <div class="testimonial-item">
                                <p>“ The images you captured were precise, natural and beautiful. We spent so much time
                                    with our guests due to the fact that you knew exactly the </p>
                                <div class="testimonial-two-img">
                                    <img src="@/assets/images/AboutComp/AboutTestimonialComp/testimonial-2.png" alt="">
                                    <span>Sharp Mard</span>
                                </div>
                                <img class="testimonial-pattrn"
                                    src="@/assets/images/AboutComp/AboutTestimonialComp/testimonial-bg.png" alt="">
                                <img class="quotation-img"
                                    src="@/assets/images/AboutComp/AboutTestimonialComp/quotation.png" alt="">
                            </div>
                            <div class="testimonial-item">
                                <p>“ The images you captured were precise, natural and beautiful. We spent so much time
                                    with our guests due to the fact that you knew exactly the </p>
                                <div class="testimonial-two-img">
                                    <img src="@/assets/images/AboutComp/AboutTestimonialComp/testimonial-1.png" alt="">
                                    <span>Marri Alen</span>
                                </div>
                                <img class="testimonial-pattrn"
                                    src="@/assets/images/AboutComp/AboutTestimonialComp/testimonial-bg.png" alt="">
                                <img class="quotation-img"
                                    src="@/assets/images/AboutComp/AboutTestimonialComp/quotation.png" alt="">
                            </div>
                            <div class="testimonial-item">
                                <p>“ The images you captured were precise, natural and beautiful. We spent so much time
                                    with our guests due to the fact that you knew exactly the </p>
                                <div class="testimonial-two-img">
                                    <img src="@/assets/images/AboutComp/AboutTestimonialComp/testimonial-2.png" alt="">
                                    <span>Sharp Mard</span>
                                </div>
                                <img class="testimonial-pattrn"
                                    src="@/assets/images/AboutComp/AboutTestimonialComp/testimonial-bg.png" alt="">
                                <img class="quotation-img"
                                    src="@/assets/images/AboutComp/AboutTestimonialComp/quotation.png" alt="">
                            </div> -->
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>