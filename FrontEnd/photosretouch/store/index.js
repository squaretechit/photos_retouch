export const state = () => ({
    services_info: [],
    client_review_info: [],
    all_blogs_info: [],
    all_categories_info: [],
})

export const getters = {}

export const mutations = {
  SET_SERVICES: (state, all_services) => {
    state.services_info = all_services
  },
  SET_CLIENT_REVIEW: (state, all_client_review) => {
    state.client_review_info = all_client_review
  },
  SET_ALL_BLOGS: (state, all_blogs) => {
    state.all_blogs_info = all_blogs
  },
  SET_ALL_CATEGORIES: (state, all_categories) => {
    state.all_categories_info = all_categories
  }
}

export const actions = {
  async GetAllService (){
    const response = await this.$axios.get('/service/');
    this.commit('SET_SERVICES', response.data);
  },
  async GetClientReview (){
    const response = await this.$axios.get('/client-reviews/');
    this.commit('SET_CLIENT_REVIEW', response.data);
  },
  async GetAllBlogs (){
    const response = await this.$axios.get('/blogs/');
    this.commit('SET_ALL_BLOGS', response.data);
  },
  async GetAllcategories (){
    const response = await this.$axios.get('/categories/');
    this.commit('SET_ALL_CATEGORIES', response.data);
  }
}
