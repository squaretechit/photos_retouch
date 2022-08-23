<script>
import FirstSlider from "@/static/images/HomeComp/HomeComp/slider1.jpg";
import SecondSlider from "@/static/images/HomeComp/HomeComp/slider2.jpg";
import ThirdSlider from "@/static/images/HomeComp/HomeComp/slider3.jpg";
export default {
  data: () => ({
    FirstSlider,
    SecondSlider,
    ThirdSlider
  }),
  methods: {
    PogoSlider(){
        // Pogo Slider
        if ($('#pogo-slider').length > 0) {
            $('#pogo-slider').pogoSlider({
                autoplay: true,
                generateButtons: false,
                autoplayTimeout: 5000,
                displayProgess: true,
                targetWidth: 1920,
                targetHeight: 500,
                responsive: true,
                pauseOnHover: false,
            }).data('plugin_pogoSlider');
        }
    }
  },
  mounted(){ 
    this.PogoSlider();
  }
}
</script>

<template>
    <section class="main-slider-section">
        <div class="pogoSlider" id="pogo-slider">
            <div class="pogoSlider-slide" data-transition="fade" data-duration="1000"
                :style="{backgroundImage:'url(\'' + `${FirstSlider}` + '\')',}">
                <!-- Slider Elements -->
                <div class="silder-elements container">
                    <p class="pogoSlider-slide-element slider-para" data-in="slideDown" data-out="slideDown"
                        data-duration="1000" data-delay="500">Photos Retouch</p>
                    <h2 class="pogoSlider-slide-element slider-main-title" data-in="slideUp" data-out="slideUp"
                        data-duration="1000" data-delay="500">You need a photo editor,<br> we need friends. <br></h2>
                    <h3 class="pogoSlider-slide-element" data-in="slideUp" data-out="slideUp" data-duration="1000"
                        data-delay="500">Call us for a free — +88 01 82 53 24 344</h3>
                    <div class="pogoSlider-slide-element" data-in="slideLeft" data-out="slideUp" data-duration="1000"
                        data-delay="500">
                        <Nuxt-link class="btn btn-primary my-btn" :to="{name: 'service'}">Our Services</Nuxt-link>
                    </div>
                </div>
            </div>
            <div class="pogoSlider-slide" data-transition="fade" data-duration="1000"
                :style="{backgroundImage:'url(\'' + `${SecondSlider}` + '\')',}">
                <!-- Slider Elements -->
                <div class="silder-elements container text-right">
                    <p class="pogoSlider-slide-element slider-para" data-in="slideDown" data-out="slideDown"
                        data-duration="1000" data-delay="500">Photos Retouch</p>
                    <h2 class="pogoSlider-slide-element slider-main-title" data-in="slideUp" data-out="slideUp"
                        data-duration="1000" data-delay="500">To provide the best services,<br> we are here. <br></h2>
                    <h3 class="pogoSlider-slide-element" data-in="slideUp" data-out="slideUp" data-duration="1000"
                        data-delay="500">Call us for a free — +88 01 74 89 15 830</h3>
                    <div class="pogoSlider-slide-element" data-in="slideLeft" data-out="slideUp" data-duration="1000"
                        data-delay="500">
                        <Nuxt-link class="btn btn-primary my-btn":to="{name: 'quote'}">Get a Quote</Nuxt-link>
                    </div>
                </div>
            </div>
            <div class="pogoSlider-slide" data-transition="fade" data-duration="1000"
                :style="{backgroundImage:'url(\'' + `${ThirdSlider}` + '\')',}">
                <!-- Slider Elements -->
                <div class="silder-elements container text-center">
                    <p class="pogoSlider-slide-element slider-para" data-in="slideDown" data-out="slideDown"
                        data-duration="1000" data-delay="500">Photos Retouch</p>
                    <h2 class="pogoSlider-slide-element slider-main-title" data-in="slideUp" data-out="slideUp"
                        data-duration="1000" data-delay="500">Want to know more?<br> We are here. <br></h2>
                    <div class="pogoSlider-slide-element" data-in="slideLeft" data-out="slideUp" data-duration="1000"
                        data-delay="500">
                        <Nuxt-link class="btn btn-primary my-btn" :to="{name: 'contact'}">Contact</Nuxt-link>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<style scoped>
.silder-elements .my-btn:before {
    background-color: #2791BF;
}
</style>