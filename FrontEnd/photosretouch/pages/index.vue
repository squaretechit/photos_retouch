<script>
export default {
  name: "Home",
  head () {
    return {
      titleTemplate: `Photos Retouch | Home`,
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
    <LazyHomeComp />
    <LazyHomeAboutComp />
    <LazyHomeServiceComp />
    <LazyHomeWeAreStartComp />
    <LazyHomeTestimonialComp />
    <LazyHomeWorksComp />
    <LazyHomeContactSeparatorComp />
  </div>
</template>
