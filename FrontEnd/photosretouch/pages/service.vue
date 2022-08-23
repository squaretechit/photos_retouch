<script>
export default {
  name: "Service",
  head () {
    return {
      titleTemplate: `Photos Retouch | Services`,
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
    <LazyServiceComp />
    <LazyServiceMainService />
    <LazyHomeContactSeparatorComp />
  </div>
</template>
