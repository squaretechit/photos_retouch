<script>
  export default {
    name: "GetQuote",
    head () {
      return {
        titleTemplate: `Photos Retouch | Get Quote`,
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
    <LazyTheQuote />
    <LazyHomeContactSeparatorComp />
  </div>
</template>
