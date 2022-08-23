export default {
  ssr: false,
  target: 'static',
  generate: {
    fallback: true
  },
  head: {
    title: 'Photos Retouch',
    meta: [{
        charset: 'utf-8'
      },
      {
        name: 'viewport',
        content: 'width=device-width, initial-scale=1'
      },
      {
        hid: 'description',
        name: 'description',
        content: 'This is the default Descriptions'
      },
      {
        name: 'format-detection',
        content: 'telephone=no'
      }
    ],
    link: [{
        rel: 'icon',
        type: 'image/x-icon',
        href: '/favicon.ico'
      },
      {
        rel: 'canonical',
        hid: 'canonical',
        id: 'canonical',
        href: `https://photosretouch.com/`
      },
      // Twitter
      {
        hid: 'twitter:card',
        name: 'twitter:card',
        content: 'We are the best service provider in Bangladesh.',
      },
      {
        hid: 'twitter:site',
        name: 'twitter:site',
        content: 'We are the best service provider in Bangladesh.'
      },
      {
        hid: 'twitter:url',
        name: 'twitter:url',
        content: '',
      },
      {
        hid: 'twitter:title',
        name: 'twitter:title',
        content: 'Get the best service provider in Bangladesh.',
      },
      {
        hid: 'twitter:description',
        name: 'twitter:description',
        content: 'We are the best service provider in Bangladesh.',
      },
      {
        hid: 'twitter:image',
        name: 'twitter:image',
        content: '',
      },

      // Open Graph
      {
        hid: 'og:site_name',
        property: 'og:site_name',
        content: 'Photos Retouch',
      },
      {
        hid: 'og:type',
        property: 'og:type',
        content: 'We are the best service provider in Bangladesh.'
      },
      {
        hid: 'og:url',
        property: 'og:url',
        content: 'https://photosretouch.com/',
      },
      {
        hid: 'og:title',
        property: 'og:title',
        content: 'We are the best service provider in Bangladesh.',
      },
      {
        hid: 'og:description',
        property: 'og:description',
        content: 'We are the best service provider in Bangladesh.',
      },
      {
        hid: 'og:image',
        property: 'og:image',
        content: '',
      },
      {
        hid: 'og:image:secure_url',
        property: 'og:image:secure_url',
        content: '',
      },
      {
        hid: 'og:image:alt',
        property: 'og:image:alt',
        content: 'We are the best service provider in Bangladesh.',
      },
    ],
    // Global Script
    script: [
      // {src: "", async: true, crossorigin: "anonymous", body: true},
      {
        src: `/js/jquery.min.js`,
        type: "text/javascript",
        body: true
      },
      {
        src: `/js/popper.min.js`,
        type: "text/javascript",
        body: true
      },
      {
        src: `/js/bootstrap.min.js`,
        type: "text/javascript",
        body: true
      },
      {
        src: `/js/stellarnav.min.js`,
        type: "text/javascript",
        body: true
      },
      {
        src: `/js/jarallax.min.js`,
        type: "text/javascript",
        body: true
      },
      {
        src: `/js/owl.carousel.min.js`,
        type: "text/javascript",
        body: true
      },
      {
        src: `/js/froogaloop2.min.js`,
        type: "text/javascript",
        body: true
      },
      {
        src: `/js/html5lightbox.js`,
        type: "text/javascript",
        body: true
      },
      {
        src: `/js/isotope.pkgd.min.js`,
        type: "text/javascript",
        body: true
      },
      {
        src: `/js/jquery.pogo-slider.js`,
        type: "text/javascript",
        body: true
      }
    ],
  },

  // Global CSS:
  css: [
    "@/static/css/fonts.css",
    "@/static/css/bootstrap.min.css",
    "@/static/css/animate.min.css",
    "@/static/css/owl.css",
    "@/static/css/jarallax.css",
    "@/static/css/pogo-slider.css",
    "@/static/css/stellarnav.min.css",
    "@/static/css/style.css",
    "@/static/css/responsive.css"
  ],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/axios
    '@nuxtjs/axios',
    // https://go.nuxtjs.dev/pwa
    '@nuxtjs/pwa',
    '@nuxtjs/sitemap',
    '@nuxtjs/robots',
  ],

  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  // axios: {
  //   // Workaround to avoid enforcing hard-coded localhost:3000: https://github.com/nuxt-community/axios-module/issues/308
  //   baseURL: '/',
  // },
  axios: {
    baseURL: 'https://api.photosretouch.com/',
    timeout: 5000,
    headers: {
      'Content-Type': 'application/json',
      accept: 'application/json',
    }
  },

  robots: {
    UserAgent: '*',
    Allow: '/',
    sitemap: 'https://photosretouch.com/sitemap.xml'
  },

  sitemap: {
    // options
    hostname: 'https://photosretouch.com/',
    "path": "/sitemap.xml",
    "exclude": [],
    "routes": [],
    "cacheTime": 900000,
    "etag": {
      "weak": false
    },
    "gzip": false,
    "trailingSlash": false,
    "defaults": {},
    "pathGzip": "/sitemap.xml"
  },

  // PWA module configuration: https://go.nuxtjs.dev/pwa
  pwa: {
    manifest: {
      lang: 'en'
    }
  },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {}
}


// { <script type="application/ld+json">
// {
//     "@context": "https://schema.org",
//     "@type": "Corporation",
//     "name": "Photos Retouch",
//     "url": "https://www.photosretouch.com/",
//     "logo": "{% static 'img/logo-dark.png' %}",
//     "sameAs": [
//         "https://www.facebook.com/sharif.foysal.9",
//         "https://bd.linkedin.com/in/shoron"
//     ]
// }
// </script>}
