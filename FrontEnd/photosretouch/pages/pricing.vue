<script>
export default {
  name: "Pricing",
  head () {
    return {
      titleTemplate: `Photos Retouch | Pricing`,
    }
  },
  mounted() {
    setTimeout(()=> {
      document.querySelector('#MainHeader').className = "header-area sticky header-two-area";
      document.querySelector('#loader').classList.remove('active');
    }, 1000);
  }
};
</script>

<template>
  <div>
    <LazyPricingComp />
    <LazyPricingCalculatorComp />
    <LazyPricingCardsComp />
    <LazyHomeContactSeparatorComp />
  </div>
</template>
