import { createStore } from "vuex";
import { getAPI } from "@/axios-api";


export default createStore({
  state: {
    services_info: [],
    client_review_info: [],
    all_blogs_info: [],
    all_categories_info: []
  },
  getters: {},
  mutations: {
    SetServices(state, all_services) {
      state.services_info = all_services
    },
    SetClientReview(state, all_client_review) {
      state.client_review_info = all_client_review
    },
    SetAllBlogs(state, all_blogs) {
      state.all_blogs_info = all_blogs
    },
    SetAllcategories(state, all_categories) {
      state.all_categories_info = all_categories
    }
  },
  actions: {
    async GetAllService (){
      const response = await getAPI.get('/service/');
      this.commit('SetServices', response.data);
    },
    async GetClientReview (){
      const response = await getAPI.get('/client-reviews/');
      this.commit('SetClientReview', response.data);
    },
    async GetAllBlogs (){
      const response = await getAPI.get('/blogs/');
      this.commit('SetAllBlogs', response.data);
    },
    async GetAllcategories (){
      const response = await getAPI.get('/categories/');
      this.commit('SetAllcategories', response.data);
    }
  },
  modules: {},
});
