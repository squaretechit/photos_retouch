<script>
import BackGroundPic from "@/assets/images/ContactComp/ContactComp/top-bg-4.jpeg";
export default {
  data: () => ({
    BackGroundPic
  })
}
</script>

<template>
    <section class="page-name-area page-name-two-area overlay-white"
    :style="{
        backgroundImage:
        'url(\'' + `${BackGroundPic}` + '\')',
    }">
        <div class="container">
            <div class="row">
                <div class="col-lg-12">
                    <div class="page-name-col text-center">
                        <h6>Photography</h6>
                        <h2>Contact us</h2>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>