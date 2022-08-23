<script>
  export default {
    name: "SingleService",
    data: () => ({ServiceInfo: ''}),
    computed: {AllServices() { return this.$store.state.services_info}},
    methods: {},
    mounted() {
      setTimeout(() => {
        document.querySelector('#MainHeader').className = "header-area sticky header-two-area";
        document.querySelector('#loader').classList.remove('active');
      }, 1000);
    },
    beforeRouteEnter(to, form, next) {
        next(vm => {
          setTimeout(()=> {
            const exists = vm['AllServices'].some((service) => service.url === to.params.singleservice)
            if (!exists){
              return vm['$nuxt'].error({ statusCode: 404, message: 'Page Not Found' })
            }
          }, 1000)
        });
    },
    created() {
      setTimeout(() => {
        this.ServiceInfo = this.AllServices.find((service) => service.url === this.$route.params.singleservice);
      }, 1000);
    },
    head() {
      return {
        titleTemplate: `Photos Retouch | ${this.ServiceInfo['name']}`
      }
    }
  };

</script>

<template>
  <div>
    <LazySingleserviceSingleService />
    <LazyHomeContactSeparatorComp />
  </div>
</template>
