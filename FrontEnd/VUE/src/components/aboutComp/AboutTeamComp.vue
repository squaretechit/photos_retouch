<script>
import { getAPI, baseURL } from "@/axios-api";
export default {
    data: () => ({
        BaseURL: baseURL,
    }),
    methods: {
        TeamCarousel(){
            if ($('.team-carousel').length){
                $('.team-carousel').owlCarousel({
                    loop: true,
                    margin: 30,
                    dots: true,
                    nav: false,
                    autoplayHoverPause: true,
                    autoplay: true,
                    autoplayTimeout: 4000,
                    smartSpeed: 800,
                    center: true,
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
                            items: 3
                        },
                        1200: {
                            items: 4
                        }
                    }
                })
            }
        },
        GetTeamMembers(){
            getAPI.get('/our-team/')
            .then(response => {
                this.AllTeamMembers = response.data
                for (let i=0; i < response.data.length; i++){
                    document.querySelector('.team-carousel.owl-theme').innerHTML += `
                        <div class="team-col">
                            <img src="${this.BaseURL + response.data[i]['picture']}" alt="${response.data[i]['member_name']}">
                            <h4>${response.data[i]['member_name']}</h4>
                            <p>${response.data[i]['designation']}</p>
                        </div>`;
                }
                this.TeamCarousel();
            })
            .catch(err => console.log(err.message))
        }
    },
    mounted() {
        this.GetTeamMembers();
    }
}
</script>

<template>
    <section class="team-area">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-lg-12">
                    <div class="my-title">
                        <h6>Our Experts</h6>
                        <h2>Explore Our Team</h2>
                    </div>
                </div>
            </div>
            <div class="team-carousel owl-theme"></div>
        </div>
    </section>
</template>

<style>
    .team-area .owl-dots .owl-dot.active span {
        background-color: #3FEEF7;
    }
    .team-area .owl-dots .owl-dot:hover span {
        background-color: #3FEEF7;
    }
</style>