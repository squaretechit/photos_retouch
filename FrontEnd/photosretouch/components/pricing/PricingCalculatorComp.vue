<script>
export default {
    data: () => ({
        SelectedServiceName: "Select service",
        CalImage: '',
        inputQuantity: 0,
        fromValue: 0,
        ToValue: 0,
        disabled: true,
        allcalcullatorinfo: []
    }),
    computed: {
        AllServices() { return this.$store.state.services_info }
    },
    methods: {
        async ServiceCalculator() {
            const response = await this.$axios.get('/calculator/');
            this.allcalcullatorinfo = response.data
        },
        SelectedService(e) {
            const TergetValue = e.target.value;
            if (TergetValue !== "Select service") {
                this.inputQuantity = 1;
                this.disabled = false;
                const SelectedTergetService = this.AllServices.find((service) => service.name === TergetValue);
                const SelectedTerget = this.allcalcullatorinfo.find((calculator) => calculator.service === SelectedTergetService['id']);
                this.SelectedServiceName = TergetValue;
                this.CalImage = `${this.$axios.defaults.baseURL}${SelectedTerget['pricing_image']}`;
                this.fromValue = SelectedTerget['price_form']
                this.ToValue = SelectedTerget['price_to']
            } else {
                this.SelectedServiceName = "Select service";
                this.inputQuantity = 0;
                this.disabled = true;
            }
        },
        SelectedQuantity(e) {
            if (this.SelectedServiceName !== "Select service") {
                const SelectedQuantityNumber = e.target.value;
                this.inputQuantity = SelectedQuantityNumber;
                const SelectedTergetService = this.AllServices.find((service) => service.name === this.SelectedServiceName);
                const SelectedTerget = this.allcalcullatorinfo.find((calculator) => calculator.service === SelectedTergetService['id']);
                if (SelectedTerget) {
                    this.fromValue = parseFloat(
                        parseFloat(SelectedTerget['price_form']) *
                        parseFloat(SelectedQuantityNumber)).toFixed(2)
                    this.ToValue = parseFloat(
                        parseFloat(SelectedTerget['price_to']) *
                        parseFloat(SelectedQuantityNumber)).toFixed(2)
                } else if (parseInt(SelectedQuantityNumber) === 1) {
                    this.fromValue = parseFloat(SelectedTerget['price_form']);
                    this.ToValue = parseFloat(SelectedTerget['price_to']);
                } else {
                    this.fromValue = 0;
                    this.ToValue = 0;
                }
            }
        }
    },
    mounted() {
        this.ServiceCalculator();
    }
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
                        <option v-for="service in AllServices" :key="service.id">{{ service.name }}</option>
                    </select>
                    <label for="inputQuantity">Select Quantity</label>
                    <input type="number" :disabled="disabled" @input="SelectedQuantity" class="form-control" min="1"
                        :value="inputQuantity">
                </div>
                <div class="right p-5 col-lg-6 d-flex flex-column justify-content-center">
                    <div v-if="SelectedServiceName === 'Select service'" class="unSelected-container p-5 border h-100">
                        <p class="text-center text-secondary">Select a service and a quantity to calculate your
                            estimate.</p>
                    </div>
                    <div v-else-if="SelectedServiceName !== 'Select service'" class="selected-container">
                        <div class="row px-5 pb-5 justify-content-around images-container">
                            <div class="col-5  shadow-lg img-left"
                                :style="{ backgroundImage: 'url(\'' + `${CalImage}` + '\')', }"></div>
                            <div class="col-5  shadow-lg img-right"
                                :style="{ backgroundImage: 'url(\'' + `${CalImage}` + '\')', }"></div>
                        </div>
                        <div class="px-5 text-container">
                            <p>Service &nbsp; &nbsp; <span class="service-name">{{ SelectedServiceName }}</span> </p>
                            <p>Quantity &nbsp; &nbsp; <span class="service-quantity">{{ inputQuantity }}</span>
                                Images</p>
                            <p class="mt-4 pricing-text">$ <span class="calculator-pricing-text">{{ fromValue }}</span>
                                USD -
                                $<span class="calculator-pricing-text2">{{ ToValue }}</span> USD</p>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </section>
</template>

<style scoped>
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