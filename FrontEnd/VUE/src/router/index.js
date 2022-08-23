import { createRouter, createWebHistory } from "vue-router";


const routes = [
  { path: "/", name: "home", component: () => import(/* webpackChunkName: "Home" */"../views/HomeView.vue")},
  { path: "/about", name: "about", component: () => import(/* webpackChunkName: "About" */"../views/AboutView.vue")},
  { path: "/service", name: "service", component: () => import(/* webpackChunkName: "Service" */"../views/ServiceView.vue")},
  { path: "/service/:service_name", name: "SingleService", 
    component: () => import(/* webpackChunkName: "SingleService" */"../views/SingleServiceView.vue"),
  },
  { path: "/pricing", name: "pricing", component: () => import(/* webpackChunkName: "Pricing" */"../views/PricingView.vue")},
  { path: "/blog", name: "blog", component: () => import(/* webpackChunkName: "Blog" */"../views/BlogView.vue")},
  { path: "/blog/:blog_name", name: "SingleBlog",
    component: () => import (/* webpackChunkName: "SingleBlog" */"../views/SingleBlogView.vue")},
  { path: "/contact", name: "contact", component: () => import(/* webpackChunkName: "Contact" */"../views/ContactView.vue")},
  { path: "/:pathMatch(.*)*", name: 'NotFound', component: ()=> import(/* webpackChunkName: "NotFound" */'@/views/NotFound.vue')},
  { path: "/sitemap.xml", name: 'sitemap', component: ()=> import(/* webpackChunkName: "Sitemap" */"@/views/Sitemap.vue")}
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
  scrollBehavior (to, from, savedPosition){
    return savedPosition || {top: 0, behavior: 'smooth'}
  }
});

export default router;