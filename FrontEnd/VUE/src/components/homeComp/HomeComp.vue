<script>
import FirstSlider from "@/assets/images/HomeComp/HomeComp/slider1.jpg";
import SecondSlider from "@/assets/images/HomeComp/HomeComp/slider2.jpg";
import ThirdSlider from "@/assets/images/HomeComp/HomeComp/slider3.jpg";
export default {
  data: () => ({
    FirstSlider,
    SecondSlider,
    ThirdSlider
  }),
  mounted(){
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
}
</script>

<template>
    <section class="main-slider-section">
        <div class="pogoSlider" id="pogo-slider">
            <div class="pogoSlider-slide" data-transition="fade" data-duration="1000"
                :style="{
                      backgroundImage:
                        'url(\'' + `${FirstSlider}` + '\')',
                    }">
                <!-- Slider Elements -->
                <div class="silder-elements container">
                    <p class="pogoSlider-slide-element slider-para" data-in="slideDown" data-out="slideDown"
                        data-duration="1000" data-delay="500">Photography</p>
                    <h2 class="pogoSlider-slide-element slider-main-title" data-in="slideUp" data-out="slideUp"
                        data-duration="1000" data-delay="500">You need a photographer<br> we need friends. <br></h2>
                    <h3 class="pogoSlider-slide-element" data-in="slideUp" data-out="slideUp" data-duration="1000"
                        data-delay="500">Call us for a free — +88 00 11 61 12</h3>
                    <div class="pogoSlider-slide-element" data-in="slideLeft" data-out="slideUp" data-duration="1000"
                        data-delay="500">
                        <a class="btn btn-primary my-btn" href="#" role="button">Our
                            Protfolio</a>
                    </div>
                </div>
            </div>
            <div class="pogoSlider-slide" data-transition="fade" data-duration="1000"
                :style="{
                      backgroundImage:
                        'url(\'' + `${SecondSlider}` + '\')',
                    }">
                <!-- Slider Elements -->
                <div class="silder-elements container text-right">
                    <p class="pogoSlider-slide-element slider-para" data-in="slideDown" data-out="slideDown"
                        data-duration="1000" data-delay="500">Photography</p>
                    <h2 class="pogoSlider-slide-element slider-main-title" data-in="slideUp" data-out="slideUp"
                        data-duration="1000" data-delay="500">You need a photographer<br> we need friends. <br></h2>
                    <h3 class="pogoSlider-slide-element" data-in="slideUp" data-out="slideUp" data-duration="1000"
                        data-delay="500">Call us for a free — +88 00 11 61 12</h3>
                    <div class="pogoSlider-slide-element" data-in="slideLeft" data-out="slideUp" data-duration="1000"
                        data-delay="500">
                        <a class="btn btn-primary my-btn" href="#" role="button">Our
                            Protfolio</a>
                    </div>
                </div>
            </div>
            <div class="pogoSlider-slide" data-transition="fade" data-duration="1000"
                :style="{
                      backgroundImage:
                        'url(\'' + `${ThirdSlider}` + '\')',
                    }">
                <!-- Slider Elements -->
                <div class="silder-elements container text-center">
                    <p class="pogoSlider-slide-element slider-para" data-in="slideDown" data-out="slideDown"
                        data-duration="1000" data-delay="500">Photography</p>
                    <h2 class="pogoSlider-slide-element slider-main-title" data-in="slideUp" data-out="slideUp"
                        data-duration="1000" data-delay="500">You need a photographer<br> we need friends. <br></h2>
                    <h3 class="pogoSlider-slide-element" data-in="slideUp" data-out="slideUp" data-duration="1000"
                        data-delay="500">Call us for a free — +88 00 11 61 12</h3>
                    <div class="pogoSlider-slide-element" data-in="slideLeft" data-out="slideUp" data-duration="1000"
                        data-delay="500">
                        <a class="btn btn-primary my-btn" href="#" role="button">Our
                            Protfolio</a>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<style>
.silder-elements .my-btn:before {
    background-color: #2791BF;
}
</style>