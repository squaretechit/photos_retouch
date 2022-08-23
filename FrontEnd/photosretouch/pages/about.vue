<script>
  export default {
    name: "About",
    head () {
      return {
        titleTemplate: `Photos Retouch | About`
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
    <LazyAboutComp />
    <LazyAboutWeAreStartComp />
    <LazyAboutTwoComp />
    <LazyAboutTeamComp />
    <LazyAboutTestimonialComp />
    <LazyHomeWorksComp />
    <LazyHomeContactSeparatorComp />
  </div>
</template>
