<script>
import TheHeaderVue from "@/components/TheHeader.vue";
import HomeComp from "@/components/homeComp/HomeComp.vue";
import HomeAboutComp from "@/components/homeComp/HomeAboutComp.vue";
import HomeServiceComp from "@/components/homeComp/HomeServiceComp.vue";
import HomeWeAreStartComp from "@/components/homeComp/HomeWeAreStartComp.vue";
import HomeWorksComp from "@/components/homeComp/HomeWorksComp.vue";
import HomeTestimonialComp from "@/components/homeComp/HomeTestimonialComp.vue";
import HomeContactSeparatorComp from "@/components/homeComp/HomeContactSeparatorComp.vue";
import FooterComp from "@/components/FooterComp.vue";

export default {
  name: "HomeView",
  components: {
    TheHeaderVue,
    HomeComp,
    HomeAboutComp,
    HomeServiceComp,
    HomeWeAreStartComp,
    HomeWorksComp,
    HomeTestimonialComp,
    HomeContactSeparatorComp,
    FooterComp
  },
  mounted() {  
      document.title = "Photos Retouch | Home";
      document.querySelector('#MainHeader').classList.remove('header-two-area');
  }
};
</script>

<template>
  <div>
    <TheHeaderVue />
    <HomeComp />
    <HomeAboutComp />
    <HomeServiceComp />
    <HomeWeAreStartComp />
    <HomeWorksComp />
    <HomeTestimonialComp />
    <HomeContactSeparatorComp />
    <FooterComp />
  </div>
</template>