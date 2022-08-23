<script>
export default {
  name: "Contact",
  head () {
    return {
      titleTemplate: `Photos Retouch | Contact`,
    }
  },
  mounted() {
      setTimeout(()=> {
        document.querySelector('#MainHeader').className = "header-area sticky";
        document.querySelector('#loader').classList.remove('active');
      }, 1000);
  }
};
</script>

<template>
  <div>
    <LazyContactComp />
    <LazyContactUsStartComp />
    <LazyHomeContactSeparatorComp />
  </div>
</template>
