document.addEventListener("DOMContentLoaded", () => {
    (function ($) {
        "use strict";
        //Bootstrap Carousel
        $('.carousel').carousel({
            pause: "false"
        });
        // project-carousel
        if ($('.project-slider').length) {
            $('.project-slider').owlCarousel({
                loop: true,
                margin: 0,
                dots: false,
                nav: true,
                autoplayHoverPause: false,
                autoplay: true,
                autoplayTimeout: 4000,
                smartSpeed: 800,
                center: false,
                navText: [
                    '<i class="fa fa-arrow-circle-o-left"></i>',
                    '<i class="fa fa-arrow-circle-o-right"></i>'
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
                        items: 1
                    },
                    992: {
                        items: 1
                    },
                    1200: {
                        items: 1
                    }
                }
            })
        }
        // Parallax background
        $('.parallax').jarallax({
            speed: 0.5
        });
    })(window.jQuery);
})