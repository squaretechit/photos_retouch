<script>
export default {
  name: "Blogs",
  head () {
    return {
      titleTemplate: `Photos Retouch | Blogs`,
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
    <LazyBlogComp />
    <LazyBlogStartComp />
    <LazyHomeContactSeparatorComp />
  </div>
</template>
