<script>
    import TheHeaderView from "@/components/TheHeader.vue"
    import PricingComp from "@/components/pricingComp/PricingComp.vue";
    import PricingCalculatorComp from '@/components/pricingComp/PricingCalculatorComp.vue';
    import PricingCardsComp from "@/components/pricingComp/PricingCardsComp.vue";
    import HomeContactSeparatorComp from "@/components/homeComp/HomeContactSeparatorComp.vue";
    import FooterComp from "@/components/FooterComp.vue";
    export default {
        name: "PricingView",
        components: {
            TheHeaderView,
            PricingComp,
            PricingCalculatorComp,
            PricingCardsComp,
            HomeContactSeparatorComp,
            FooterComp
        },
        mounted() {
            document.title = "Photos Retouch | Pricing";
            document.querySelector('#MainHeader').classList.add('header-two-area');
        }
    };
</script>

<template>
    <div>
        <TheHeaderView/>
        <PricingComp />
        <PricingCalculatorComp />
        <PricingCardsComp />
        <HomeContactSeparatorComp />
        <FooterComp />
    </div>
</template>