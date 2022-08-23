<script>
    import { ref } from "vue";
    import { baseURL } from "@/axios-api";
    import store from "@/store";
    export default {
        data: () => ({
            BaseURL: baseURL,
            AllServices: ref(store.state.services_info)
        })
    }
</script>

<template>
    <section class="py-5 pricing-cards-section">
        <div class="container">
            <div class="card-deck pricing-cards-wrapper">
                <div v-for="service in AllServices" :key="service.id" class="pricing-card pb-2 card">
                    <div class="card-body">
                        <div class="price-card-header">
                            <h5 class="card-title">{{service.name}}</h5>
                            <h3 class="card-pricing-text">$0.29-$10<span>/per image</span></h3>
                        </div>
                        <hr>
                        <ul>
                            <li><i class="fa fa-check-circle" aria-hidden="true"></i> Basic Clipping</li>
                            <li><i class="fa fa-check-circle" aria-hidden="true"></i> Compound Clipping Path</li>
                            <li><i class="fa fa-check-circle" aria-hidden="true"></i> Complex Path</li>
                            <li><i class="fa fa-check-circle" aria-hidden="true"></i> 3 Step quality control</li>
                        </ul>
                    </div>
                    <div class="card-footer">
                        <a href="#">Get your quotes
                            <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"
                                stroke-width="2" class="w-4 h-4 ml-auto" viewBox="0 0 24 24">
                                <path d="M5 12h14M12 5l7 7-7 7"></path>
                            </svg>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<style>
    .pricing-cards-section .pricing-cards-wrapper {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 20px;
        justify-content: center;

    }

    .pricing-cards-section .pricing-card {
        border-radius: 0.5rem;
        border: 1px solid #cbd5e0;
        margin: 0;
    }

    .pricing-cards-section .pricing-card:hover {
        border-color: #3FEEF7;
    }

    .price-card-header {
        min-height: 125px;
    }

    .pricing-cards-section .pricing-card .card-body .card-title {
        font-size: 14px;
        color: #4a5568;
    }

    .pricing-cards-section .pricing-card .card-body .card-pricing-text {
        font-size: 24px;
        color: #1a202c;
    }

    .pricing-cards-section .pricing-card .card-body .card-pricing-text span {
        font-size: 16px;
        color: #a0aec0;
        text-transform: none;
    }

    .pricing-cards-section .pricing-card .card-body ul {
        padding-left: 0;
    }

    .pricing-cards-section .pricing-card .card-body ul li {
        list-style: none;
        font-size: 16px;
        color: #718096;
        font-weight: 600;
    }

    .pricing-cards-section .pricing-card .card-body ul li i {
        color: #3FEEF7;
    }

    .pricing-cards-section .pricing-card .card-footer {
        background-color: transparent;
        border: none;
    }

    .pricing-cards-section .pricing-card .card-footer a {
        color: white;
        border: none;
        padding: 8px 16px;
        width: 100%;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-radius: 50px;
        font-size: 16px;
        background-image: linear-gradient(90deg, #2791BF, #3FEEF7);
    }

    .pricing-cards-section .pricing-card .card-footer a svg {
        width: 16px;
    }

    @media only screen and (max-width:1199px) {
        .pricing-cards-section .pricing-cards-wrapper {
            grid-template-columns: repeat(3, 1fr) !important;
        }
    }

    @media only screen and (max-width:991px) {
        .pricing-cards-section .pricing-cards-wrapper {
            grid-template-columns: repeat(2, 1fr) !important;
        }
    }

    @media only screen and (max-width:575px) {
        .pricing-cards-section .pricing-cards-wrapper {
            grid-template-columns: repeat(1, 1fr) !important;
        }
    }
</style>