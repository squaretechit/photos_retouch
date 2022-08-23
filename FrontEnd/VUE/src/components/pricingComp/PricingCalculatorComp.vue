<script>
    import ClippingPathServicesImg from "@/assets/images/PricingComp/PricingCalculatorComp/calculator-img1.png";
    import ColorVariantsImg from "@/assets/images/PricingComp/PricingCalculatorComp/calculator-img2.png";
    import DropShadowServicesImg from "@/assets/images/PricingComp/PricingCalculatorComp/calculator-img3.png";
    import GhostMannequinServicesImg from "@/assets/images/PricingComp/PricingCalculatorComp/calculator-img4.png";
    import ImageMaskingServicesImg from "@/assets/images/PricingComp/PricingCalculatorComp/calculator-img5.png";
    import JewelryPhotoEditingServicesImg from "@/assets/images/PricingComp/PricingCalculatorComp/calculator-img6.png";
    import PhotoRetouchingServicesImg from "@/assets/images/PricingComp/PricingCalculatorComp/calculator-img7.png";
    import ProductPhotoEditingServicesImg from "@/assets/images/PricingComp/PricingCalculatorComp/calculator-img8.png";
    import RealEstatePhotoEdtingServicesImg from "@/assets/images/PricingComp/PricingCalculatorComp/calculator-img9.png";
    export default {
        data: () => ({
            SelectedServiceName: "Select service",
            CalImageLeft: "",
            CalImageRight: "",
            fromValue: 0,
            ToValue: 0
        }),
        methods: {
            SelectedService (e){
                const TergetValue = e.target.value;
                if (TergetValue === "Clipping Path Services") {
                    this.SelectedServiceName = TergetValue;
                    this.CalImageLeft = ClippingPathServicesImg;
                    this.CalImageRight = ClippingPathServicesImg;
                } else if (TergetValue === "Color Variants") {
                    this.SelectedServiceName = TergetValue;
                    this.CalImageLeft = ColorVariantsImg;
                    this.CalImageRight = ColorVariantsImg;
                } else if (TergetValue === "Drop Shadow Services") {
                    this.SelectedServiceName = TergetValue;
                    this.CalImageLeft = DropShadowServicesImg;
                    this.CalImageRight = DropShadowServicesImg;
                } else if (TergetValue === "Ghost Mannequin Services") {
                    this.SelectedServiceName = TergetValue;
                    this.CalImageLeft = GhostMannequinServicesImg;
                    this.CalImageRight = GhostMannequinServicesImg;
                } else if (TergetValue === "Image Masking Services") {
                    this.SelectedServiceName = TergetValue;
                    this.CalImageLeft = ImageMaskingServicesImg;
                    this.CalImageRight = ImageMaskingServicesImg;
                } else if (TergetValue === "Jewelry Photo Editing Services") {
                    this.SelectedServiceName = TergetValue;
                    this.CalImageLeft = JewelryPhotoEditingServicesImg;
                    this.CalImageRight = JewelryPhotoEditingServicesImg;
                } else if (TergetValue === "Photo Retouching Services") {
                    this.SelectedServiceName = TergetValue;
                    this.CalImageLeft = PhotoRetouchingServicesImg;
                    this.CalImageRight = PhotoRetouchingServicesImg;
                } else if (TergetValue === "Product Photo-editing Services") {
                    this.SelectedServiceName = TergetValue;
                    this.CalImageLeft = ProductPhotoEditingServicesImg;
                    this.CalImageRight = ProductPhotoEditingServicesImg;
                } else if (TergetValue === "Real Estate Photo Edting Services(HDR)") {
                    this.SelectedServiceName = TergetValue;
                    this.CalImageLeft = RealEstatePhotoEdtingServicesImg;
                    this.CalImageRight = RealEstatePhotoEdtingServicesImg;
                } else if (TergetValue === "Select service") {
                    this.SelectedServiceName = TergetValue;
                }
            },
            SelectedQuantity (e){
                let SelectedQuantityNumber = e.target.value;
                let clippingPathServicesFrom = 0.39,
                    clippingPathServicesTo = 10.00,
                    colorVariantsFrom = 1.00,
                    colorVariantsTo = 5.00,
                    dropShadowServicesFrom = 0.25,
                    dropShadowServicesTo = 4.00,
                    ghostMannequinServicesFrom = 1.00,
                    ghostMannequinServicesTo = 5.00,
                    imageMaskingServicesFrom = 1.00,
                    imageMaskingServicesTo = 10.00,
                    jewelryPhotoEditingServicesFrom = 5.00,
                    jewelryPhotoEditingServicesTo = 30.00,
                    photoRetouchingServicesFrom = 1.00,
                    photoRetouchingServicesTo = 15.00,
                    productPhotoEditingServicesFrom = 0.39,
                    productPhotoEditingServicesTo = 5.00,
                    realEstatePhotoEdtingServicesFrom = 1.00,
                    realEstatePhotoEdtingServicesTo = 50.00;
                if (this.SelectedServiceName === "Clipping Path Services") {
                    this.fromValue = parseFloat(clippingPathServicesFrom * SelectedQuantityNumber).toFixed(2)
                    this.ToValue = parseFloat(clippingPathServicesTo * SelectedQuantityNumber).toFixed(2)
                } else if (this.SelectedServiceName === "Color Variants") {
                    this.fromValue = parseFloat(colorVariantsFrom * SelectedQuantityNumber).toFixed(2)
                    this.ToValue = parseFloat(colorVariantsTo * SelectedQuantityNumber).toFixed(2)
                } else if (this.SelectedServiceName === "Drop Shadow Services") {
                    this.fromValue = parseFloat(dropShadowServicesFrom * SelectedQuantityNumber).toFixed(2)
                    this.ToValue = parseFloat(dropShadowServicesTo * SelectedQuantityNumber).toFixed(2)
                } else if (this.SelectedServiceName === "Ghost Mannequin Services") {
                    this.fromValue = parseFloat(ghostMannequinServicesFrom * SelectedQuantityNumber).toFixed(2)
                    this.ToValue = parseFloat(ghostMannequinServicesTo * SelectedQuantityNumber).toFixed(2)
                } else if (this.SelectedServiceName === "Image Masking Services") {
                    this.fromValue = parseFloat(imageMaskingServicesFrom * SelectedQuantityNumber).toFixed(2)
                    this.ToValue = parseFloat(imageMaskingServicesTo * SelectedQuantityNumber).toFixed(2)
                } else if (this.SelectedServiceName === "Jewelry Photo Editing Services") {
                    this.fromValue = parseFloat(jewelryPhotoEditingServicesFrom * SelectedQuantityNumber).toFixed(2)
                    this.ToValue = parseFloat(jewelryPhotoEditingServicesTo * SelectedQuantityNumber).toFixed(2)
                } else if (this.SelectedServiceName === "Photo Retouching Services") {
                    this.fromValue = parseFloat(photoRetouchingServicesFrom * SelectedQuantityNumber).toFixed(2)
                    this.ToValue = parseFloat(photoRetouchingServicesTo * SelectedQuantityNumber).toFixed(2)
                } else if (this.SelectedServiceName === "Product Photo-editing Services") {
                    this.fromValue = parseFloat(productPhotoEditingServicesFrom * SelectedQuantityNumber).toFixed(2)
                    this.ToValue = parseFloat(productPhotoEditingServicesTo * SelectedQuantityNumber).toFixed(2)
                } else if (this.SelectedServiceName === "Real Estate Photo Edting Services(HDR)") {
                    this.fromValue = parseFloat(realEstatePhotoEdtingServicesFrom * SelectedQuantityNumber).toFixed(2)
                    this.ToValue = parseFloat(realEstatePhotoEdtingServicesTo * SelectedQuantityNumber).toFixed(2)
                } else if (this.SelectedServiceName === "Select service") {
                    this.fromValue = 0;
                    this.ToValue = 0;
                }
            }
        },
    }
</script>
<template>
    <section class="calculator-section">
        <div class="container">
            <div class="row shadow-lg border rounded-lg inner-container ">
                <div class="left p-5 col-lg-6 d-flex flex-column justify-content-center border-right">
                    <h3 class="calculator-title">Calculate Your Estimate</h3>
                    <label for="inputSelect">Select service</label>
                    <select id="inputSelect" @change="SelectedService" class="mb-3 form-control">
                        <option selected>Select service</option>
                        <option>Clipping Path Services</option>
                        <option>Color Variants</option>
                        <option>Drop Shadow Services</option>
                        <option>Ghost Mannequin Services</option>
                        <option>Image Masking Services</option>
                        <option>Jewelry Photo Editing Services</option>
                        <option>Photo Retouching Services</option>
                        <option>Product Photo-editing Services</option>
                        <option>Real Estate Photo Edting Services(HDR)</option>
                    </select>
                    <label for="inputQuantity">Select Quantity</label>
                    <input type="number" @input="SelectedQuantity" class="form-control" id="inputQuantity" min="0" placeholder="0">
                </div>
                <div class="right p-5 col-lg-6 d-flex flex-column justify-content-center">
                    <div v-if="SelectedServiceName === 'Select service'" class="unSelected-container p-5 border h-100">
                        <p class="text-center text-secondary">Select a service and a quantity to calculate your
                            estimate.</p>
                    </div>
                    <div v-else-if="SelectedServiceName != 'Select service'" class="selected-container">
                        <div class="row px-5 pb-5 justify-content-around images-container">
                            <div class="col-5  shadow-lg img-left"
                            :style="{backgroundImage:'url(\'' + `${CalImageLeft}` + '\')',}"></div>
                            <div class="col-5  shadow-lg img-right"
                            :style="{backgroundImage:'url(\'' + `${CalImageRight}` + '\')',}"></div>
                        </div>
                        <div class="px-5 text-container">
                            <p>Service &nbsp; &nbsp; <span class="service-name">{{SelectedServiceName}}</span> </p>
                            <p>Quantity &nbsp; &nbsp; <span class="service-quantity">1</span> Images</p>
                            <p class="mt-4 pricing-text">$ <span class="calculator-pricing-text">{{fromValue}}</span> USD -
                                $<span class="calculator-pricing-text2">{{ToValue}}</span> USD</p>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </section>
</template>

<style>
    .calculator-section {
        padding: 100px 0;
    }

    .text-separator {
        width: 4rem;
        height: 0.25rem;
        background-color: #3FEEF7;
    }

    .calculator-title {
        color: #3FEEF7;
        font-size: 1.25em;
    }

    .calculator-section .pricing-text {
        color: #3FEEF7;
        font-size: 1.25em;
        font-weight: 600;
    }

    .calculator-section .inner-container {
        margin-left: 100px;
        margin-right: 100px;
    }

    .calculator-section .images-container .img-left {
        background-position: 0;
        padding: 0;
        background-size: auto 112%;
        border-radius: 0.375em;
    }

    .calculator-section .images-container .img-left::after {
        content: "";
        display: block;
        padding-bottom: 100%;
    }

    .calculator-section .images-container .img-right {
        background-position: 100%;
        padding: 0;
        background-size: auto 112%;
        border-radius: 0.375em;
    }

    .calculator-section .images-container .img-right::after {
        content: "";
        display: block;
        padding-bottom: 100%;
    }

    @media only screen and (max-width:991px) {
        .calculator-section .inner-container .right {
            padding-top: 0 !important;
        }

        .calculator-section .inner-container .left {
            padding-bottom: 0 !important;
        }
    }

    @media only screen and (max-width:767px) {
        .calculator-section .inner-container {
            margin: 0 !important;
        }

        .calculator-section .inner-container .images-container {
            padding-left: 0 !important;
            padding-right: 0 !important;
            padding-bottom: 20px !important;
        }

        .calculator-section .inner-container .text-container {
            padding: 0 !important;
        }
    }
</style>