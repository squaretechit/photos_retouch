<script>
import TheHeaderVue from '@/components/TheHeader.vue';
import AboutComp from '@/components/aboutComp/AboutComp.vue';
import AboutWeAreStartComp from '@/components/aboutComp/AboutWeAreStartComp.vue';
import AboutTwoComp from '@/components/aboutComp/AboutTwoComp.vue'
import AboutTeamComp from '@/components/aboutComp/AboutTeamComp.vue';
import AboutTestimonialComp from '@/components/aboutComp/AboutTestimonialComp.vue';
import HomeWorksComp from "@/components/homeComp/HomeWorksComp.vue";
import HomeContactSeparatorComp from "@/components/homeComp/HomeContactSeparatorComp.vue";
import FooterComp from "@/components/FooterComp.vue";
export default {
  name: "AboutView",
  components: {
    TheHeaderVue,
    AboutComp,
    AboutWeAreStartComp,
    AboutTwoComp,
    AboutTeamComp,
    AboutTestimonialComp,
    HomeWorksComp,
    HomeContactSeparatorComp,
    FooterComp
  },
  mounted() {  
      document.title = "Photos Retouch | About";
      document.querySelector('#MainHeader').classList.add('header-two-area');
  }
};
</script>

<template>
  <div>
    <TheHeaderVue />
    <AboutComp />
    <AboutWeAreStartComp />
    <AboutTwoComp />
    <AboutTeamComp />
    <AboutTestimonialComp />
    <HomeWorksComp />
    <HomeContactSeparatorComp />
    <FooterComp />
  </div>
</template>