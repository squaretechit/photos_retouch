<script>
  export default {
    data: () => ({
      BaseURL: ''
    }),
    computed: {
        AllClientReviews () {return this.$store.state.client_review_info}
    },
    created() {
        this.BaseURL = this.$axios.defaults.baseURL;
    }
  }
</script>

<template>
  <section class="testimonial-area">
    <div class="container">
      <div class="row">
        <div class="col-lg-12">
          <div class="my-title">
            <h6>Client Says</h6>
            <h2>Explore Our client Review</h2>
          </div>
        </div>
      </div>
      <div class="row justify-content-center">
        <div class="col-lg-9">
          <div class="testimonial-col">
            <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
              <ol class="carousel-indicators">
                <li v-for="(review, index) in AllClientReviews" :key="review.id" :class="{active: review.id === 1}" data-target="#carouselExampleIndicators" :data-slide-to="index"
                :style="{backgroundImage:'url(\'' + `${BaseURL + review.client_picture}` + '\')',}">
                  <p>{{review.client_name}}</p>
                </li>
              </ol>
              <div class="carousel-inner">
                <div v-for="review in AllClientReviews" :key="review.id" :class="{active: review.id === 1, 'carousel-item': true}" >
                  <p v-html="review.review.slice(0,235) + '...'"></p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
  .testimonial-area {
    background: url('@/static/images/HomeComp/TestimonialComp/testimonial.jpeg');
  }

  .testimonial-area .carousel-indicators li {
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
  }
</style>