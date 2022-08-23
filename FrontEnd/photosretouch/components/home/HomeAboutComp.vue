<template>
  <section class="about-area">
    <div class="container">
      <div class="row">
        <div class="col-lg-9">
          <div class="about-col">
            <img loading="lazy" decoding="async" src="@/static/images/HomeComp/AboutComp/1.jpg" alt="Banner"
              class="img-fluid" />
            <div class="about-box">
              <h5>Take time for yourself</h5>
              <h2>Hello! We are Photos Retouch, The best Photo Editor</h2>
              <p>To create the greatest quality's aerial imagery that offers peoples a unique and inspiring perspective of theirs world.</p>
              <!-- <a  href="#" role="button">About us</a> -->
                <Nuxt-link class="btn btn-primary my-btn" :to="{name:'about'}">About us</Nuxt-link>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
  .about-box h5,
  .about-box h2,
  .about-box p {
    color: #2791bf;
  }

  .about-box .my-btn {
    color: #2791bf;
    border-color:#2791bf;
  }
  .about-box .my-btn:before {
    background-color: #2791bf;
  }
</style>