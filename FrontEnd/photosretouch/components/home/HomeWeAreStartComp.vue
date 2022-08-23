<template>
  <section class="we-are-area pb-5">
    <div class="container">
      <div class="row">
        <div class="col-lg-6">
          <div class="we-are-col">
            <h4>We Are</h4>
            <h2>Photos are tricky Wedding Photography</h2>
            <h4>But we'll make them easy for you</h4>
            <p>
              Hey there lovers, studs, babes, dudes (or any other endearing identifiers for, you, lovely people). Welcome to the wild side. We’re Photos Retouch, the wedding photo editing team based in Bangladesh!
            </p>
            <Nuxt-link class="btn btn-primary my-btn" :to="{name: 'quote'}">Get a Quote</Nuxt-link>
          </div>
        </div>
      </div>
    </div>
    <div class="we-are-img mt-5">
      <img loading="lazy" decoding="async" src="@/static/images/HomeComp/WeAreStartComp/we-are.jpg" alt="Banner"
        class="img-fluid" />
    </div>
  </section>
</template>

<style scoped>
  .we-are-area {
    margin-top: 70px;
  }
</style>