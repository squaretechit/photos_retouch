<script>
    export default {
        methods: {
            SlideAfterBefore() {
                const container = document.querySelectorAll('.compration-container');
                const container2 = document.querySelectorAll('.comparisonSliderInput');
                for (let i = 0; i < container.length; i++) {
                    container2[i].addEventListener('input', (e) => {
                        container[i].style.setProperty('--position', `${e.target.value}%`);
                    })
                }
            }
        },
        mounted() {
            this.SlideAfterBefore();
        }
    }
</script>
<template>
    <!-- carousel start -->
    <section class="single-service-carousel-section">
        <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
            <ol class="carousel-indicators">
                <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
                <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
                <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
                <li data-target="#carouselExampleIndicators" data-slide-to="3"></li>
                <li data-target="#carouselExampleIndicators" data-slide-to="4"></li>
            </ol>
            <div class="carousel-inner">
                <div class="carousel-item active">
                    <img src="@/assets/images/SingleServiceComp/SingleServiceComp/service-carousel-img.jpg"
                        class="d-block w-100" alt="...">
                </div>
                <div class="carousel-item">
                    <img src="@/assets/images/SingleServiceComp/SingleServiceComp/service-carousel-img2.jpg"
                        class="d-block w-100" alt="...">
                </div>
                <div class="carousel-item">
                    <img src="@/assets/images/SingleServiceComp/SingleServiceComp/service-carousel-img3.jpg"
                        class="d-block w-100" alt="...">
                </div>
                <div class="carousel-item">
                    <img src="@/assets/images/SingleServiceComp/SingleServiceComp/service-carousel-img4.jpg"
                        class="d-block w-100" alt="...">
                </div>
                <div class="carousel-item">
                    <img src="@/assets/images/SingleServiceComp/SingleServiceComp/service-carousel-img5.jpg"
                        class="d-block w-100" alt="...">
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
        <div class="container">
            <h1 class="text-center">{{ $route.params.service_name }} Single Service</h1>
        </div>
    </section>
    <!-- carousel end -->
    <!--body retouching services section start -->
    <section class="single-service-body-retouching-services-section">
        <div class="container inner-section d-flex flex-column justify-content-center align-items-center">
            <h2 class="my-4 custom-heading">Body Retouching Services</h2>
            <p class="services-description">FixThePhoto is a professional body retouching service that offers online
                body reshaping and slimming,
                cellulite removal, skin smoothing, breast enlargement, and more. We guarantee natural results and a
                perfect body on photos fast and at an affordable price.
            </p>
            <div class="my-4 btns-wrapper">
                <button class="btn btn-primary my-btn">Try for Free</button>
                <button class="btn btn-primary my-btn ml-3">Get a Quote</button>
            </div>
            <h3 class="mb-4 custom-heading">Body Retouching Services We Provide:</h3>
            <div class="row img-comparison-slider-container">
                <div class="col-lg-6 pr-4">
                    <li>Body slimming - from $6 per photo</li>
                    <p class="mb-3">No matter what body form you have, we can use advanced body editing techniques to
                        make
                        any body slimmer without overphotoshopping. You can indicate what part of your body we should
                        pay special attention to and which one requires less body slimming.</p>
                    <main>
                        <div class="compration-container">
                            <div class="image-container">
                                <img class="image-before slider-image"
                                    src="@/assets/images/SingleServiceComp/ServiceDescriptionComp/comparison-slider-img1.jpg"
                                    alt="color photo" />
                                <img class="image-after slider-image"
                                    src="@/assets/images/SingleServiceComp/ServiceDescriptionComp/comparison-slider-img1b.jpg"
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
                <div class="col-lg-6 pl-4">
                    <li>Body slimming - from $6 per photo</li>
                    <p class="mb-3">No matter what body form you have, we can use advanced body editing techniques to
                        make
                        any body slimmer without overphotoshopping. You can indicate what part of your body we should
                        pay special attention to and which one requires less body slimming.</p>
                    <main>
                        <div class="compration-container">
                            <div class="image-container">
                                <img class="image-before slider-image"
                                    src="@/assets/images/SingleServiceComp/ServiceDescriptionComp/comparison-slider2-img1b.jpg"
                                    alt="color photo" />
                                <img class="image-after slider-image"
                                    src="@/assets/images/SingleServiceComp/ServiceDescriptionComp/comparison-slider2-img1b.jpg"
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
    </section>
    <!--body retouching services section end -->
    <!-- how does it work section start  -->
    <section class="how-it-work-section">
        <div class="container px-lg-5">
            <h3 class="mt-4 mb-5 text-center custom-heading">How Does It Work</h3>
            <div class=" row">
                <div class="pb-3 col-md-3 col-sm-6 text-center">


                    <p class="mt-3">Upload body retouching photos</p>
                </div>
                <div class="pb-3 col-md-3 col-sm-6 text-center">


                    <p class="mt-3">Write recommendation</p>
                </div>
                <div class="pb-3 col-md-3 col-sm-6 text-center">


                    <p class="mt-3">Submit for revision if necessary</p>
                </div>
                <div class="pb-3 col-md-3 col-sm-6 text-center">


                    <p class="mt-3">Get your photos back</p>
                </div>
            </div>
            <div class="my-4 text-center btns-wrapper">
                <button class="btn btn-primary my-btn">Try for Free</button>
                <button class="btn btn-primary my-btn ml-3">Get a Quote</button>
            </div>
            <p>Photographers face many problems with body retouching. Typically, we receive two types of orders – 75%
                ask to
                enhance to body’s curves, 25% want us to enlarge breasts or add muscles. Our retouchers provide
                high-quality
                retouching of all problematic zones of your model’s body.
                <br>
                <br>
                If you need to make a body slimmer, FixThePhoto retouchers will reshape body curves, use body countering
                techniques, apply plastic surgery effect, make a thin waist, skinny face, remove cellulite and double
                chin,
                elongate the legs, reducing blemishes and shadows, and use the Dodge and Burn effect.</p>
        </div>
    </section>
    <!-- how does it work section end -->
    <!-- pricing table section start  -->
    <section class="single-services-pricing-table-section">
        <div class="container px-5">
            <h3 class="my-4 mb-5 text-center custom-heading">Body Reshaping Photo Editor Service Prices</h3>
            <div class=" pricing-table-cards-wrapper">
                <div class="p-0 pricing-card card">
                    <div class="card-body p-0">
                        <div class="pricing-card-top">
                            <h3 class="card-title custom-heading">Pro Level</h3>
                            <div class="d-flex justify-content-between light-box-images-container">
                                <div class=" light-box-img"><img src="/images/singleService/pricingCardThumb1.jpg"
                                        alt=""></div>
                                <div class=" light-box-img"><img src="/images/singleService/pricingCardThumb2.jpg"
                                        alt=""></div>
                                <div class=" light-box-img"><img src="/images/singleService/pricingCardThumb3.jpg"
                                        alt=""></div>
                            </div>
                            <h3 class="mt-3 mb-0 card-pricing-text custom-heading">$6.00</h3>
                            <p class="">per image</p>
                        </div>
                        <button class="mb-3 w-100 view-examples-btn ">View Examples</button>
                        <p class="text-center">Services applied:</p>
                        <ul class="mb-3 pricing-card-list">
                            <li>Get Rid of the Red Eyesg</li>
                            <li>Pimples, Scars, Face Blemishes Removal</li>
                            <li>Airbrush Face Skin</li>
                            <li>Color Correction</li>
                            <li>Crop/Resize Photos</li>
                            <li>Basic Backdrop Enhancement</li>
                            <li>Stray Hair Fixing</li>
                            <li>Slight Widen One Color Background</li>
                            <li>Small Items Removal</li>
                            <li>Remove Face Wrinkles</li>
                            <li>Light Body Liquifing</li>
                            <li>Clipping Path for Simple Objects on White/Black/Transparent Backdrop (No retouching)
                            </li>
                        </ul>
                    </div>
                    <div class="card-footer p-0">
                        <button class="w-100">Order Now</button>
                    </div>
                </div>
                <div class="p-0 pricing-card card">
                    <div class="card-body p-0">
                        <div class="pricing-card-top">
                            <h3 class="card-title custom-heading">High End Level</h3>
                            <div class="d-flex justify-content-between light-box-images-container">
                                <div class=" light-box-img"><img src="/images/singleService/pricingCardThumb1.jpg"
                                        alt=""></div>
                                <div class=" light-box-img"><img src="/images/singleService/pricingCardThumb2.jpg"
                                        alt=""></div>
                                <div class=" light-box-img"><img src="/images/singleService/pricingCardThumb3.jpg"
                                        alt=""></div>
                            </div>
                            <h3 class="mt-3 mb-0 card-pricing-text custom-heading">$ 12.00</h3>
                            <p class="">per image</p>
                        </div>
                        <button class="mb-3 w-100 view-examples-btn ">View Examples</button>
                        <p class="text-center">Services applied:</p>
                        <ul class="mb-3 pricing-card-list">
                            <li>Get Rid of the Red Eyesg</li>
                            <li>Pimples, Scars, Face Blemishes Removal</li>
                            <li>Airbrush Face Skin</li>
                            <li>Color Correction</li>
                            <li>Crop/Resize Photos</li>
                            <li>Basic Backdrop Enhancement</li>
                            <li>Stray Hair Fixing</li>
                            <li>Slight Widen One Color Background</li>
                            <li>Small Items Removal</li>
                            <li>Remove Face Wrinkles</li>
                            <li>Light Body Liquifing</li>
                            <li>Clipping Path for Simple Objects on White/Black/Transparent Backdrop (No retouching)
                            </li>
                        </ul>
                    </div>
                    <div class="card-footer p-0">
                        <button class="w-100">Order Now</button>
                    </div>
                </div>
                <div class="p-0 pricing-card card">
                    <div class="card-body p-0">
                        <div class="pricing-card-top">
                            <h3 class="card-title custom-heading">Extra Level</h3>
                            <div class="d-flex justify-content-between light-box-images-container">
                                <div class=" light-box-img"><img src="/images/singleService/pricingCardThumb1.jpg"
                                        alt=""></div>
                                <div class=" light-box-img"><img src="/images/singleService/pricingCardThumb2.jpg"
                                        alt=""></div>
                                <div class=" light-box-img"><img src="/images/singleService/pricingCardThumb3.jpg"
                                        alt=""></div>
                            </div>
                            <h3 class="mt-3 mb-0 card-pricing-text custom-heading">$ 12.00</h3>
                            <p class="">per image</p>
                        </div>
                        <button class="mb-3 w-100 view-examples-btn ">View Examples</button>
                        <p class="text-center">Services applied:</p>
                        <ul class="mb-3 pricing-card-list">
                            <li>Get Rid of the Red Eyesg</li>
                            <li>Pimples, Scars, Face Blemishes Removal</li>
                            <li>Airbrush Face Skin</li>
                            <li>Color Correction</li>
                            <li>Crop/Resize Photos</li>
                            <li>Basic Backdrop Enhancement</li>
                            <li>Stray Hair Fixing</li>
                            <li>Slight Widen One Color Background</li>
                            <li>Small Items Removal</li>
                            <li>Remove Face Wrinkles</li>
                            <li>Light Body Liquifing</li>
                            <li>Clipping Path for Simple Objects on White/Black/Transparent Backdrop (No retouching)
                            </li>
                        </ul>
                    </div>
                    <div class="card-footer p-0">
                        <button class="w-100">Order Now</button>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <!-- pricing table section end  -->

    <!-- bulk services section start -->
    <section class="bulk-services-section">
        <div class="container px-5 border-bottom">
            <h3 class="my-4 custom-heading text-center">Bulk Services for Permanent Customers</h3>
            <div class="row">
                <div class="col-lg-6 row">
                    <div class="col-lg-5 col-sm-6 text-center img-container">
                        <svg width="150" height="150" version="1.1" id="Слой_1" xmlns="http://www.w3.org/2000/svg"
                            xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 751.3 407"
                            style="enable-background:new 0 0 751.3 407;" xml:space="preserve">
                            <g>
                                <g>
                                    <path class="st0" d="M462.4,176.9h-11.9v-76.3c0-6.3,0.2-12.4,0.6-18c-1,1-2.2,2.1-3.4,3.2c-1.3,1.1-7.1,5.9-17.4,14.3l-6.4-8.3
                  l28.3-21.9h10.3V176.9z" />
                                    <path class="st0" d="M536.6,111.5c11.3,0,20.2,2.8,26.6,8.4c6.5,5.6,9.7,13.2,9.7,23c0,11.1-3.5,19.8-10.6,26.1
                  c-7.1,6.3-16.8,9.4-29.2,9.4c-12.1,0-21.3-1.9-27.6-5.8v-11.7c3.4,2.2,7.7,3.9,12.7,5.2c5.1,1.2,10.1,1.9,15,1.9
                  c8.6,0,15.3-2,20-6.1c4.8-4.1,7.1-9.9,7.1-17.6c0-14.9-9.2-22.4-27.5-22.4c-4.6,0-10.8,0.7-18.6,2.1l-6.3-4l4-50.1h53.2V81h-42.8
                  l-2.7,32.2C525.5,112,531.1,111.5,536.6,111.5z" />
                                    <path class="st0" d="M632.9,101.7c0,11.1-1.9,19.5-5.6,25.2c-3.7,5.7-9.2,8.5-16.4,8.5c-6.8,0-12.1-2.9-15.9-8.7
                  c-3.8-5.8-5.7-14.2-5.7-25c0-11.1,1.8-19.4,5.5-25c3.6-5.6,9-8.4,16.1-8.4c7.1,0,12.5,2.9,16.3,8.7C631,82.8,632.9,91,632.9,101.7
                  z M599.3,101.7c0,8.3,0.9,14.5,2.7,18.7c1.8,4.2,4.7,6.2,8.8,6.2c8,0,12-8.3,12-24.9c0-16.5-4-24.8-12-24.8c-4.1,0-7,2.1-8.8,6.2
                  C600.2,87.2,599.3,93.4,599.3,101.7z M678.5,69.8l-59.4,107.1h-10.8l59.4-107.1H678.5z M697.4,144.6c0,11.1-1.9,19.5-5.6,25.2
                  c-3.7,5.7-9.2,8.5-16.4,8.5c-6.9,0-12.3-2.9-16-8.7c-3.7-5.8-5.6-14.1-5.6-25c0-11.1,1.8-19.4,5.5-25c3.6-5.6,9-8.4,16.2-8.4
                  c6.9,0,12.3,2.9,16.2,8.6C695.5,125.5,697.4,133.8,697.4,144.6z M663.8,144.6c0,8.3,0.9,14.6,2.7,18.7c1.8,4.1,4.8,6.2,8.9,6.2
                  s7.1-2,9.1-6.1c2-4.1,2.9-10.3,2.9-18.8c0-8.3-1-14.5-2.9-18.6c-2-4-5-6-9.1-6s-7.1,2-8.9,6C664.7,130.1,663.8,136.3,663.8,144.6z
                  " />
                                </g>
                                <g>
                                    <path class="st0" d="M526.5,261.2c0,18.9-4.8,33.7-14.3,44.5c-9.5,10.8-22.8,16.2-39.8,16.2c-17.3,0-30.7-5.3-40.2-15.9
                  c-9.4-10.6-14.1-25.6-14.1-44.9c0-19.2,4.7-34,14.2-44.6c9.5-10.6,22.9-15.8,40.3-15.8c16.9,0,30.1,5.4,39.6,16.1
                  C521.7,227.5,526.5,242.3,526.5,261.2z M432.6,261.2c0,16,3.4,28.1,10.2,36.3c6.8,8.2,16.7,12.4,29.6,12.4
                  c13.1,0,22.9-4.1,29.6-12.3c6.7-8.2,10-20.3,10-36.3c0-15.8-3.3-27.9-10-36.1c-6.6-8.2-16.4-12.3-29.4-12.3
                  c-13.1,0-23,4.1-29.8,12.4C436,233.5,432.6,245.5,432.6,261.2z" />
                                    <path class="st0"
                                        d="M566.5,320.2h-13.7V202.5h65.7v12.2h-52v43.1h48.8v12.2h-48.8V320.2z" />
                                    <path class="st0"
                                        d="M651.6,320.2h-13.7V202.5h65.7v12.2h-52v43.1h48.8v12.2h-48.8V320.2z" />
                                </g>
                            </g>
                            <path class="st0"
                                d="M256.4,98.2l3.4,8.4h-67.1l3.4-8.4H256.4 M257.6,87.3h-62.5c-3.7,0-7.1,2.3-8.5,5.7l-4.8,11.8
              c-2.5,6.1,2,12.7,8.5,12.7h72.2c6.5,0,11-6.6,8.5-12.7L266.1,93C264.7,89.6,261.3,87.3,257.6,87.3L257.6,87.3z" />
                            <path class="st0"
                                d="M322,147.1c3.1,0,5.6,2.5,5.6,5.6s-2.5,5.6-5.6,5.6c-3.1,0-5.6-2.5-5.6-5.6S318.9,147.1,322,147.1 M322,136.2
              c-9.1,0-16.5,7.4-16.5,16.5s7.4,16.5,16.5,16.5c9.1,0,16.5-7.4,16.5-16.5S331.1,136.2,322,136.2L322,136.2z" />
                            <path class="st0"
                                d="M329.7,188.3H314c-3,0-5.5-2.4-5.5-5.5s2.4-5.5,5.5-5.5h15.7c3,0,5.5,2.4,5.5,5.5S332.7,188.3,329.7,188.3z" />
                            <path class="st0" d="M307.9,252.1l-9.8-6.7c-1.3,3.5-2.9,6.8-4.7,10l8.4,5.7c1.4,1,1.9,2.4,2,3.1c0.1,0.7,0.2,2.2-0.8,3.6
              c-0.9,1.3-2.4,2.1-4,2.1c-0.7,0-1.7-0.1-2.7-0.9l-8.1-5.5c-2.1,3-4.5,5.8-7,8.5l8.8,6.1c2.7,1.9,5.8,2.8,8.9,2.8c5,0,10-2.4,13-6.9
              C317,266.9,315.1,257.1,307.9,252.1z" />
                            <path class="st0" d="M220.9,143.6c19.2,0,37.3,7.5,50.8,21.1c13.6,13.6,21.1,31.6,21.1,50.8s-7.5,37.3-21.1,50.8
              c-13.6,13.6-31.6,21.1-50.8,21.1c-19.2,0-37.3-7.5-50.8-21.1c-13.6-13.6-21.1-31.6-21.1-50.8s7.5-37.3,21.1-50.8
              C183.6,151,201.6,143.6,220.9,143.6 M220.9,132.7c-45.7,0-82.8,37.1-82.8,82.8s37.1,82.8,82.8,82.8c45.7,0,82.8-37.1,82.8-82.8
              S266.6,132.7,220.9,132.7L220.9,132.7z" />
                            <path class="st0" d="M333.2,117.5h-35.9l-13.1-33.3c-2.8-9.4-9.4-15.5-16.8-15.5h-83c-7.4,0-14,6.1-16.8,15.5l-12.8,33.3h-24.7
              c0-0.1,0-0.1,0-0.2v-11.6c0-5.6-4.5-10.1-10.1-10.1H82.4c-5.6,0-10.1,4.5-10.1,10.1v11.6c0,0.1,0,0.1,0,0.2h-3.1
              c-12.5,0-22.7,10.2-22.7,22.7v2.4v12.3v130v12.3v3.2c0,12.5,10.2,22.7,22.7,22.7H221c3,0,5.5-2.4,5.5-5.5s-2.4-5.5-5.5-5.5H69.2
              c-6.5,0-11.8-5.3-11.8-11.8v-2.1H96h9.5H149c10.5,0,19.2-7.4,21.4-17.2c-3.7-2.9-7.2-6-10.4-9.5v4.8c0,6.1-4.9,11-11,11h-43.4V152.4
              H149c4.9,0,9,3.2,10.4,7.5c2.6-2.8,5.3-5.5,8.3-8c-3.9-6.3-10.8-10.5-18.7-10.5H57.4v-1.3c0-6.5,5.3-11.8,11.8-11.8h85.6h7.5l2.7-7
              l12.8-33.3l0.2-0.4l0.1-0.4c1.5-5,4.4-7.7,6.3-7.7h83c1.9,0,4.8,2.7,6.3,7.7l0.1,0.4l0.2,0.4l13.1,33.3l2.7,6.9h7.4h35.9
              c6.5,0,11.8,5.3,11.8,11.8v160.2c0,6.5-5.3,11.8-11.8,11.8h-83.8v0c-2.9,0.2-5.1,2.5-5.1,5.4s2.3,5.3,5.1,5.4v0h83.8
              c12.5,0,22.7-10.2,22.7-22.7V140.2C355.9,127.7,345.7,117.5,333.2,117.5z M96,152.4v134.9H57.4V152.4H96z M119.2,116.5H83.2v-10
              h35.9V116.5z" />
                            <path class="st0"
                                d="M281.1,197.6c-0.4-2.6-2.7-4.6-5.4-4.6c-3,0-5.5,2.5-5.5,5.5c0,0.7,0.1,1.5,0.4,2.1l0,0
              c1.3,4.6,2.1,9.5,2.1,14.5c0,28.8-23.4,52.2-52.2,52.2c-28.8,0-52.2-23.4-52.2-52.2c0-28.8,23.4-52.2,52.2-52.2
              c16.7,0,31.6,7.9,41.1,20.1c0.9,1.6,2.7,2.8,4.8,2.8c3,0,5.5-2.5,5.5-5.5c0-1.1-0.3-2-0.8-2.9l0,0C259.6,162,241.2,152,220.5,152
              c-34.8,0-63.1,28.2-63.1,63.1c0,34.8,28.2,63.1,63.1,63.1s63.1-28.2,63.1-63.1C283.6,208.4,283,203.4,281.1,197.6z" />
                        </svg>

                    </div>
                    <div class="col-lg-7 col-sm-6 d-flex align-items-center text-container">
                        <p>Discount for all body retouching services during a month who orders from total cost is more
                            than $300.00 US per 1 order.</p>
                    </div>
                </div>
                <div class="col-lg-6 row">
                    <div class="col-lg-5 col-sm-6 text-center img-container">
                        <svg width="150" height="150" version="1.1" id="Слой_1" xmlns="http://www.w3.org/2000/svg"
                            xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 751.3 407"
                            style="enable-background:new 0 0 751.3 407;" xml:space="preserve">
                            <g>
                                <g>
                                    <path class="st0" d="M483.8,95c0,6.8-1.9,12.4-5.8,16.8c-3.8,4.3-9.3,7.3-16.3,8.7v0.6c8.6,1.1,15,3.8,19.1,8.2
                  c4.1,4.4,6.2,10.2,6.2,17.3c0,10.2-3.5,18.1-10.6,23.5c-7.1,5.5-17.1,8.2-30.2,8.2c-5.7,0-10.9-0.4-15.6-1.3
                  c-4.7-0.9-9.3-2.4-13.7-4.5V161c4.6,2.3,9.6,4,14.8,5.2c5.2,1.2,10.2,1.8,14.9,1.8c18.5,0,27.8-7.3,27.8-21.8
                  c0-13-10.2-19.5-30.6-19.5h-10.5v-10.5H444c8.3,0,15-1.8,19.8-5.5c4.9-3.7,7.3-8.8,7.3-15.3c0-5.2-1.8-9.3-5.4-12.3
                  c-3.6-3-8.5-4.5-14.6-4.5c-4.7,0-9.1,0.6-13.3,1.9c-4.2,1.3-8.9,3.6-14.2,7l-6.2-8.2c4.4-3.5,9.5-6.2,15.2-8.2
                  c5.7-2,11.8-3,18.1-3c10.4,0,18.5,2.4,24.2,7.1C480.9,80.1,483.8,86.7,483.8,95z" />
                                    <path class="st0" d="M574.1,123.2c0,18.5-2.9,32.3-8.8,41.5c-5.8,9.1-14.8,13.7-26.8,13.7c-11.5,0-20.3-4.7-26.3-14
                  c-6-9.3-9-23.1-9-41.1c0-18.7,2.9-32.5,8.7-41.5c5.8-9,14.7-13.5,26.6-13.5c11.6,0,20.4,4.7,26.5,14.1
                  C571.1,91.7,574.1,105.3,574.1,123.2z M515.6,123.2c0,15.6,1.8,26.9,5.5,34s9.5,10.7,17.5,10.7c8.1,0,14-3.6,17.6-10.8
                  c3.6-7.2,5.5-18.5,5.5-33.9s-1.8-26.6-5.5-33.8c-3.6-7.2-9.5-10.7-17.6-10.7c-8,0-13.8,3.5-17.5,10.6
                  C517.4,96.3,515.6,107.6,515.6,123.2z" />
                                    <path class="st0" d="M632.9,101.7c0,11.1-1.9,19.5-5.6,25.2c-3.7,5.7-9.2,8.5-16.4,8.5c-6.8,0-12.1-2.9-15.9-8.7
                  c-3.8-5.8-5.7-14.2-5.7-25c0-11.1,1.8-19.4,5.5-25c3.6-5.6,9-8.4,16.1-8.4c7.1,0,12.5,2.9,16.3,8.7C631,82.8,632.9,91,632.9,101.7
                  z M599.3,101.7c0,8.3,0.9,14.5,2.7,18.7c1.8,4.2,4.7,6.2,8.8,6.2c8,0,12-8.3,12-24.9c0-16.5-4-24.8-12-24.8c-4.1,0-7,2.1-8.8,6.2
                  C600.2,87.2,599.3,93.4,599.3,101.7z M678.5,69.8l-59.4,107.1h-10.8l59.4-107.1H678.5z M697.4,144.6c0,11.1-1.9,19.5-5.6,25.2
                  c-3.7,5.7-9.2,8.5-16.4,8.5c-6.9,0-12.3-2.9-16-8.7c-3.7-5.8-5.6-14.1-5.6-25c0-11.1,1.8-19.4,5.5-25c3.6-5.6,9-8.4,16.2-8.4
                  c6.9,0,12.3,2.9,16.2,8.6C695.5,125.5,697.4,133.8,697.4,144.6z M663.8,144.6c0,8.3,0.9,14.6,2.7,18.7c1.8,4.1,4.8,6.2,8.9,6.2
                  s7.1-2,9.1-6.1c2-4.1,2.9-10.3,2.9-18.8c0-8.3-1-14.5-2.9-18.6c-2-4-5-6-9.1-6s-7.1,2-8.9,6C664.7,130.1,663.8,136.3,663.8,144.6z
                  " />
                                </g>
                                <g>
                                    <path class="st0" d="M526.5,261.2c0,18.9-4.8,33.7-14.3,44.5c-9.5,10.8-22.8,16.2-39.8,16.2c-17.3,0-30.7-5.3-40.2-15.9
                  c-9.4-10.6-14.1-25.6-14.1-44.9c0-19.2,4.7-34,14.2-44.6c9.5-10.6,22.9-15.8,40.3-15.8c16.9,0,30.1,5.4,39.6,16.1
                  C521.7,227.5,526.5,242.3,526.5,261.2z M432.6,261.2c0,16,3.4,28.1,10.2,36.3c6.8,8.2,16.7,12.4,29.6,12.4
                  c13.1,0,22.9-4.1,29.6-12.3c6.7-8.2,10-20.3,10-36.3c0-15.8-3.3-27.9-10-36.1c-6.6-8.2-16.4-12.3-29.4-12.3
                  c-13.1,0-23,4.1-29.8,12.4C436,233.5,432.6,245.5,432.6,261.2z" />
                                    <path class="st0"
                                        d="M566.5,320.2h-13.7V202.5h65.7v12.2h-52v43.1h48.8v12.2h-48.8V320.2z" />
                                    <path class="st0"
                                        d="M651.6,320.2h-13.7V202.5h65.7v12.2h-52v43.1h48.8v12.2h-48.8V320.2z" />
                                </g>
                            </g>
                            <path class="st0"
                                d="M256.4,98.2l3.4,8.4h-67.1l3.4-8.4H256.4 M257.6,87.3h-62.5c-3.7,0-7.1,2.3-8.5,5.7l-4.8,11.8
              c-2.5,6.1,2,12.7,8.5,12.7h72.2c6.5,0,11-6.6,8.5-12.7L266.1,93C264.7,89.6,261.3,87.3,257.6,87.3L257.6,87.3z" />
                            <path class="st0"
                                d="M322,147.1c3.1,0,5.6,2.5,5.6,5.6s-2.5,5.6-5.6,5.6c-3.1,0-5.6-2.5-5.6-5.6S318.9,147.1,322,147.1 M322,136.2
              c-9.1,0-16.5,7.4-16.5,16.5s7.4,16.5,16.5,16.5c9.1,0,16.5-7.4,16.5-16.5S331.1,136.2,322,136.2L322,136.2z" />
                            <path class="st0"
                                d="M329.7,188.3H314c-3,0-5.5-2.4-5.5-5.5s2.4-5.5,5.5-5.5h15.7c3,0,5.5,2.4,5.5,5.5S332.7,188.3,329.7,188.3z" />
                            <path class="st0" d="M307.9,252.1l-9.8-6.7c-1.3,3.5-2.9,6.8-4.7,10l8.4,5.7c1.4,1,1.9,2.4,2,3.1c0.1,0.7,0.2,2.2-0.8,3.6
              c-0.9,1.3-2.4,2.1-4,2.1c-0.7,0-1.7-0.1-2.7-0.9l-8.1-5.5c-2.1,3-4.5,5.8-7,8.5l8.8,6.1c2.7,1.9,5.8,2.8,8.9,2.8c5,0,10-2.4,13-6.9
              C317,266.9,315.1,257.1,307.9,252.1z" />
                            <path class="st0" d="M220.9,143.6c19.2,0,37.3,7.5,50.8,21.1c13.6,13.6,21.1,31.6,21.1,50.8s-7.5,37.3-21.1,50.8
              c-13.6,13.6-31.6,21.1-50.8,21.1c-19.2,0-37.3-7.5-50.8-21.1c-13.6-13.6-21.1-31.6-21.1-50.8s7.5-37.3,21.1-50.8
              C183.6,151,201.6,143.6,220.9,143.6 M220.9,132.7c-45.7,0-82.8,37.1-82.8,82.8s37.1,82.8,82.8,82.8c45.7,0,82.8-37.1,82.8-82.8
              S266.6,132.7,220.9,132.7L220.9,132.7z" />
                            <path class="st0" d="M333.2,117.5h-35.9l-13.1-33.3c-2.8-9.4-9.4-15.5-16.8-15.5h-83c-7.4,0-14,6.1-16.8,15.5l-12.8,33.3h-24.7
              c0-0.1,0-0.1,0-0.2v-11.6c0-5.6-4.5-10.1-10.1-10.1H82.4c-5.6,0-10.1,4.5-10.1,10.1v11.6c0,0.1,0,0.1,0,0.2h-3.1
              c-12.5,0-22.7,10.2-22.7,22.7v2.4v12.3v130v12.3v3.2c0,12.5,10.2,22.7,22.7,22.7H221c3,0,5.5-2.4,5.5-5.5s-2.4-5.5-5.5-5.5H69.2
              c-6.5,0-11.8-5.3-11.8-11.8v-2.1H96h9.5H149c10.5,0,19.2-7.4,21.4-17.2c-3.7-2.9-7.2-6-10.4-9.5v4.8c0,6.1-4.9,11-11,11h-43.4V152.4
              H149c4.9,0,9,3.2,10.4,7.5c2.6-2.8,5.3-5.5,8.3-8c-3.9-6.3-10.8-10.5-18.7-10.5H57.4v-1.3c0-6.5,5.3-11.8,11.8-11.8h85.6h7.5l2.7-7
              l12.8-33.3l0.2-0.4l0.1-0.4c1.5-5,4.4-7.7,6.3-7.7h83c1.9,0,4.8,2.7,6.3,7.7l0.1,0.4l0.2,0.4l13.1,33.3l2.7,6.9h7.4h35.9
              c6.5,0,11.8,5.3,11.8,11.8v160.2c0,6.5-5.3,11.8-11.8,11.8h-83.8v0c-2.9,0.2-5.1,2.5-5.1,5.4s2.3,5.3,5.1,5.4v0h83.8
              c12.5,0,22.7-10.2,22.7-22.7V140.2C355.9,127.7,345.7,117.5,333.2,117.5z M96,152.4v134.9H57.4V152.4H96z M119.2,116.5H83.2v-10
              h35.9V116.5z" />
                            <path class="st0"
                                d="M281.1,197.6c-0.4-2.6-2.7-4.6-5.4-4.6c-3,0-5.5,2.5-5.5,5.5c0,0.7,0.1,1.5,0.4,2.1l0,0
              c1.3,4.6,2.1,9.5,2.1,14.5c0,28.8-23.4,52.2-52.2,52.2c-28.8,0-52.2-23.4-52.2-52.2c0-28.8,23.4-52.2,52.2-52.2
              c16.7,0,31.6,7.9,41.1,20.1c0.9,1.6,2.7,2.8,4.8,2.8c3,0,5.5-2.5,5.5-5.5c0-1.1-0.3-2-0.8-2.9l0,0C259.6,162,241.2,152,220.5,152
              c-34.8,0-63.1,28.2-63.1,63.1c0,34.8,28.2,63.1,63.1,63.1s63.1-28.2,63.1-63.1C283.6,208.4,283,203.4,281.1,197.6z" />
                        </svg>
                    </div>
                    <div class="col-lg-7 col-sm-6 d-flex align-items-center text-container">
                        <p>Discount for all body retouching services during a month who orders from total cost is more
                            than $300.00 US per 1 order.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <!-- bulk services section end -->

    <!-- pro body editing section start -->
    <section class="pro-body-editing-section">
        <div class="container">
            <h1 class="my-4 custom-heading text-center">Professional Body Editing</h1>
            <div class="row">
                <div class="col-lg-5 col-md-5 comparison-slider-container">
                    <div class="comparison-slider">
                        <div class="image-container">

                            <img loading="lazy" decoding="async" class="image-before slider-image"
                                src="images/singleService/comparison-slider2-img1.jpg" alt="color photo" /> <img
                                loading="lazy" decoding="async" class="correctionImg"
                                src="images/singleService/comparison-slider2-imgCorrection.jpg" alt="" />
                            <img loading="lazy" decoding="async" class="image-after slider-image"
                                src="images/singleService/comparison-slider2-img1b.jpg" alt="black and white" />
                        </div>
                        <input type="range" min="0" max="100" value="50" aria-label="Percentage of before photo shown"
                            class="comparisonSliderInput" />
                        <div class="slider-line" aria-hidden="true"></div>
                        <div class="slider-button" aria-hidden="true">
                            <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor"
                                viewBox="0 0 256 256">
                                <rect width="256" height="256" fill="none"></rect>
                                <line x1="128" y1="40" x2="128" y2="216" fill="none" stroke="currentColor"
                                    stroke-linecap="round" stroke-linejoin="round" stroke-width="16"></line>
                                <line x1="96" y1="128" x2="16" y2="128" fill="none" stroke="currentColor"
                                    stroke-linecap="round" stroke-linejoin="round" stroke-width="16"></line>
                                <polyline points="48 160 16 128 48 96" fill="none" stroke="currentColor"
                                    stroke-linecap="round" stroke-linejoin="round" stroke-width="16"></polyline>
                                <line x1="160" y1="128" x2="240" y2="128" fill="none" stroke="currentColor"
                                    stroke-linecap="round" stroke-linejoin="round" stroke-width="16"></line>
                                <polyline points="208 96 240 128 208 160" fill="none" stroke="currentColor"
                                    stroke-linecap="round" stroke-linejoin="round" stroke-width="16"></polyline>
                            </svg>
                        </div>
                    </div>
                    <button class="w-100">TRY FOR FREE</button>
                </div>
                <div class="col-lg-7 col-md-7 pt-lg-0  pt-md-0 pt-3 details-container">
                    <p>Body retouching is a sensitive topic as the line between a realistic body and overphotoshopped
                        images is very blurred. FixThePhoto retouchers always make realistic retouching when they are
                        asked to enlarge breasts or elongate legs. We don’t use any auto perfect body photo editor but
                        fully rely on the Photoshop toolset and perform all adjustments manually.

                        Our task is to slightly enhance the body parts captured by a photographer, without making an
                        unnatural look.</p>
                    <h5>Level: High End</h5>
                    <h5>Price: $12</h5>
                    <p>Body photo editing applied:</p>
                    <ul class="">
                        <li>Body slimming</li>
                        <li>Body shape editing with Liquify Tool</li>
                        <li>Dodge & Burn</li>
                        <li>Color correction</li>
                        <li>Cellulite removal</li>
                        <li>Clothes photo retouching</li>
                        <li>Fingers/Nails correction</li>
                    </ul>
                </div>
            </div>
        </div>

    </section>
    <!-- pro body editing section end -->

    <section class="single-services-gallery-section">
        <div class="">
            <h3 class="my-4 text-center custom-heading">Body Retouching Examples in Full Size</h3>
            <div class="gallery">
                <img src="/images/singleService/galleryImg.jpg" alt="">
                <img src="/images/singleService/galleryImg2.jpg" alt="">
                <img src="/images/singleService/galleryImg3.jpg" alt="">
                <img src="/images/singleService/galleryImg4.jpg" alt="">
                <img src="/images/singleService/galleryImg5.jpg" alt="">
                <img src="/images/singleService/galleryImg6.jpg" alt="">
                <img src="/images/singleService/galleryImg5.jpg" alt="">
                <img src="/images/singleService/galleryImg6.jpg" alt="">
                <img src="/images/singleService/galleryImg7.jpg" alt="">
                <img src="/images/singleService/galleryImg8.jpg" alt="">
                <img src="/images/singleService/galleryImg5.jpg" alt="">
                <img src="/images/singleService/galleryImg6.jpg" alt="">
            </div>
        </div>
    </section>
</template>

<style>
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