<script>
  export default {
    props: ['error'],
    mounted() {
      setTimeout(() => {
        document.querySelector('#MainHeader').className = "header-area sticky header-two-area";
        document.querySelector('#loader').classList.remove('active');
      }, 1000);
    },
    head() {
      return {
        titleTemplate: `Photos Retouch | ${this.error.statusCode} error`
      }
    }
  }

</script>
<template>
    <section class="page_404">
        <div class="container">
            <div class="four_zero_four_bg">
                <h1 class="text-center">{{error.statusCode}}</h1>
            </div>
            <div class="contant_box_404">
                <h1 class="h2 text-center">An error occurred. {{error.message}}.</h1>
                <p class="text-center">Something Wrong!! Please contact with admin!</p>
            </div>
        </div>
    </section>
</template>

<style scoped>

  .page_404 {
    padding: 200px 0;
    background: #fff;
  }

  .page_404 img {
    width: 100%;
  }

  .four_zero_four_bg {
    background-image: url('https://cdn.dribbble.com/users/285475/screenshots/2083086/dribbble_1.gif');
    height: 400px;
    background-position: center;
  }
  .four_zero_four_bg h1 {
    font-size: 80px;
  }

  .four_zero_four_bg h3 {
    font-size: 80px;
  }


</style>
