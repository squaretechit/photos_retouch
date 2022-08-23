<script>
  export default {
    created() {
      this.$store.dispatch('GetAllService');
      this.$store.dispatch('GetClientReview');
      this.$store.dispatch('GetAllBlogs');
      this.$store.dispatch('GetAllcategories');
    }
  }

</script>
<template>
  <div>
    <div class="d-flex justify-content-center">
      <div id="loader" class="active">
        <img src="@/static/images/preloader.gif" alt="Loader">
      </div>
    </div>
    <LazyTheHeader />
    <nuxt />
    <LazyTheFooter />
  </div>
</template>

<style scoped>
  #loader {
    position: fixed;
    top: 40%;
    z-index: 9999;
    display: none;
  }
  #loader.active {
    display: block;
  }
</style>
