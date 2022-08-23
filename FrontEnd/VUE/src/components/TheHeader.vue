<script>
  export default {
    methods: {
      HomeOrNotInLoad(){
        // Home Or Not
        const MainHeader = document.querySelector('#MainHeader');
        if (window.location.pathname == '/' || window.location.pathname == '/contact' ||
          window.location.pathname == '/service' || window.location.pathname == '/blog') {
          MainHeader.classList.remove('header-two-area');
        } else {
          MainHeader.classList.add('header-two-area');
        }
      },
      MobileMenuChecking(){
        let MainNav = document.querySelector('#main-nav');
        let MainNavUl = document.querySelector('#main-nav ul');
        if (MainNav.classList.contains('mobile')) {
          MainNav.classList.remove('active');
          MainNavUl.style.display = 'none';
        }
      },
      HeaderSticky(){
        // Header Fixed
        $(window).scroll(function () {
          var sticky = $('.sticky'),
            scroll = $(window).scrollTop();
          if (scroll >= 50) sticky.addClass('fixed');
          else sticky.removeClass('fixed');
        });
      },
      NavBarAnimation(){
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
      this.HomeOrNotInLoad();
      this.HeaderSticky();
      this.NavBarAnimation();
    },
    created(){
      this.$store.dispatch('GetAllService');
      this.$store.dispatch('GetClientReview');
      this.$store.dispatch('GetAllBlogs');
      this.$store.dispatch('GetAllcategories');
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
            <router-link :to="{name:'home'}">
              <img loading="lazy" decoding="async" src="@/assets/images/logo.png" alt="Main Logo" class="logo-1" />
            </router-link>
            <router-link :to="{name:'home'}">
              <img loading="lazy" decoding="async" src="@/assets/images/logo.png" alt="Main Logo" class="logo-2" />
            </router-link>
          </div>
        </div>
        <div class="col-xl-7 col-lg-2 col-4">
          <div id="main-nav" class="stellarnav">
            <ul>
              <li class="current-menu-item menu-item-has-children">
                <router-link @click="MobileMenuChecking" :to="{name:'home'}">Home</router-link>
              </li>
              <li class="menu-item-has-children">
                <router-link @click="MobileMenuChecking" :to="{name:'about'}">About</router-link>
              </li>
              <li class="menu-item-has-children">
                <router-link @click="MobileMenuChecking" :to="{name: 'service'}">Services</router-link>
              </li>
              <li class="menu-item-has-children">
                <router-link @click="MobileMenuChecking" :to="{name: 'pricing'}">Pricing</router-link>
              </li>
              <li class="menu-item-has-children">
                <router-link @click="MobileMenuChecking" :to="{name: 'blog'}">Blog</router-link>
              </li>
              <li class="menu-item-has-children">
                <router-link @click="MobileMenuChecking" :to="{name: 'contact'}">Contact</router-link>
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
              <a class="#" href="#">Get A Quote</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </header>
</template>

<style>
  @import "https://fonts.googleapis.com/css?family=Livvic:400,500,600,700&display=swap";
  @import "https://fonts.googleapis.com/css?family=Muli:400,600&display=swap";
  @import "https://fonts.googleapis.com/css?family=Josefin+Sans:300,400,600&display=swap";
  @import "https://fonts.googleapis.com/css?family=ZCOOL+XiaoWei&display=swap";
  @import "@/assets/css/bootstrap.min.css";
  @import "@/assets/css/font-awesome.min.css";
  @import "@/assets/css/animate.min.css";
  @import "@/assets/css/owl.css";
  @import "@/assets/css/jarallax.css";
  @import "@/assets/css/pogo-slider.css";
  @import "@/assets/css/stellarnav.min.css";
  @import "@/assets/css/style.css";
  @import "@/assets/css/responsive.css";

  .router-link-exact-active {
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