<script>
  export default {
    methods: {
      MobileMenuChecking() {
        let MainNav = document.querySelector('#main-nav');
        let MainNavUl = document.querySelector('#main-nav ul');
        if (MainNav.classList.contains('mobile')) {
          MainNav.classList.remove('active');
          MainNavUl.style.display = 'none';
        }
      },
      HeaderSticky() {
        // Header Fixed
        $(window).scroll(function () {
          var sticky = $('.sticky'),
            scroll = $(window).scrollTop();
          if (scroll >= 50) sticky.addClass('fixed');
          else sticky.removeClass('fixed');
        });
      },
      NavBarAnimation() {
        // Navbar Animation
        jQuery('#main-nav').stellarNav({
          theme: 'light',
          breakpoint: 1199,
          openingSpeed: 200,
          closingDelay: 50,
          position: 'right',
          sticky: false
        });
      }
    },
    mounted() {
      this.HeaderSticky();
      this.NavBarAnimation();
    }
  }

</script>

<template>
  <!-- Header Start -->
  <header class="header-area sticky" id="MainHeader">
    <div class="container-fluid">
      <div class="row">
        <div class="col-xl-2 col-lg-5 col-8">
          <div class="site-logo">
            <Nuxt-link :to="{name:'index'}">
              <img loading="lazy" decoding="async" src="@/static/images/logo.png" alt="Main Logo" class="logo-1" />
            </Nuxt-link>
            <Nuxt-link :to="{name:'index'}">
              <img loading="lazy" decoding="async" src="@/static/images/logo.png" alt="Main Logo" class="logo-2" />
            </Nuxt-link>
          </div>
        </div>
        <div class="col-xl-7 col-lg-2 col-4">
          <div id="main-nav" class="stellarnav">
            <ul>
              <li @click="MobileMenuChecking" class="current-menu-item menu-item-has-children">
                <Nuxt-link :to="{name:'index'}">Home</Nuxt-link>
              </li>
              <li @click="MobileMenuChecking" class="menu-item-has-children">
                <Nuxt-link :to="{name:'about'}">About</Nuxt-link>
              </li>
              <li @click="MobileMenuChecking" class="menu-item-has-children">
                <Nuxt-link :to="{name: 'service'}">Services</Nuxt-link>
              </li>
              <li @click="MobileMenuChecking" class="menu-item-has-children">
                <Nuxt-link :to="{name: 'pricing'}">Pricing</Nuxt-link>
              </li>
              <li @click="MobileMenuChecking" class="menu-item-has-children">
                <Nuxt-link :to="{name: 'blog'}">Blog</Nuxt-link>
              </li>
              <li @click="MobileMenuChecking" class="menu-item-has-children">
                <Nuxt-link :to="{name: 'contact'}">Contact</Nuxt-link>
              </li>
              <li @click="MobileMenuChecking" class="menu-item-has-children d-lg-none">
                <Nuxt-link :to="{name: 'quote'}">Get a Quote</Nuxt-link>
              </li>
            </ul>
          </div>
        </div>
        <div class="col-xl-3 col-lg-5 col-md-12 dis-none-991">
          <div class="header-social-col">
            <ul>
              <li>
                <a href="#"><i class="fa fa-facebook"></i></a>
              </li>
              <li>
                <a href="#"><i class="fa fa-twitter"></i></a>
              </li>
              <li>
                <a href="#"><i class="fa fa-pinterest-p"></i></a>
              </li>
              <li>
                <a href="#"><i class="fa fa-instagram"></i></a>
              </li>
            </ul>
            <div class="header-btn">
                <Nuxt-link @click="MobileMenuChecking" :to="{name: 'quote'}">Get a Quote</Nuxt-link>
            </div>
          </div>
        </div>
      </div>
    </div>
  </header>
</template>

<style scoped>
  .nuxt-link-exact-active {
    border-bottom: 2px solid #3FEEF7 !important;
    -webkit-transition: all 0.3s ease-in-out;
    -moz-transition: all 0.3s ease-in-out;
    -o-transition: all 0.3s ease-in-out;
    -ms-transition: all 0.3s ease-in-out;
    transition: all 0.3s ease-in-out;
  }

  .site-logo {
    width: 160px;
    padding-top: 0 !important;
  }

  .site-logo a img {
    height: 100%;
    width: 100%;
  }

  .header-btn a:hover {
    background-color: #2791BF !important;
  }

  .header-area {
    min-height: 100px;
    position: fixed;
    right: 0;
    left: 0;
    top: 0;
    z-index: 999999;
    border-bottom: 1px solid #ADACAD;
    -webkit-transition: all 0.3s ease-in-out;
    -moz-transition: all 0.3s ease-in-out;
    -o-transition: all 0.3s ease-in-out;
    -ms-transition: all 0.3s ease-in-out;
    transition: all 0.3s ease-in-out;
  }

</style>
