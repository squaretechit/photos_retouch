<script>
    import TestimonialBg from "@/static/images/AboutComp/AboutTestimonialComp/testimonial-bg.png";
    import QuotationBg from "@/static/images/AboutComp/AboutTestimonialComp/quotation.png";
    export default {
        data: ()=>({
            TestimonialBg: TestimonialBg,
            QuotationBg: QuotationBg,
            BaseURL: ''
        }),
        computed: {
            Testimonials () {return this.$store.state.client_review_info}
        },
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
                const Testimonials = this.Testimonials;
                for (let i=0; i < Testimonials.length; i++){
                    document.querySelector('.testimonial-carousel').innerHTML += `
                        <div class="testimonial-item">
                            <p>${Testimonials[i]['review']}</p>
                            <div class="testimonial-two-img">
                                <img src="${this.BaseURL+Testimonials[i]['client_picture']}" alt="">
                                <span>${Testimonials[i]['client_name']}</span>
                            </div>
                            <img class="testimonial-pattrn" src="${this.TestimonialBg}" alt="Testimonial Background">
                            <img class="quotation-img" src="${this.QuotationBg}" alt="Quotation Background">
                        </div>`;
                }
                this.StartTestimoniaCarousel();
            }
        },
        mounted() {
            this.BaseURL = this.$axios.defaults.baseURL;
            this.GetTestimonial();
        }
    }
</script>

<template>
    <section class="testimonial-two-area">
        <div class="container">
            <div class="row mb-5">
                <div class="col-lg-12">
                    <div class="testimonial-two-col">
                        <div class="testimonial-carousel"></div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>