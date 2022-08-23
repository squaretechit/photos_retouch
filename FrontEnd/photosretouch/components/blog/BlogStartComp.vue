<script>
    export default {
        data: () => ({
            BaseURL: '',
            GoTop: false
        }),
        computed: {
            categories () {return this.$store.state.all_categories_info},
            AllBlogs () {return this.$store.state.all_blogs_info}
        },
        methods: {
            CheckBackToTopBtn(){
                if (document.body.scrollTop > 1000 || document.documentElement.scrollTop > 1000) {
                    this.GoTop = true;
                } else {
                    this.GoTop = false;
                }
            },
            BackToTop(){
                document.body.scrollTop = 0;
                document.documentElement.scrollTop = 0;
            }
        },
        mounted () {
            this.BaseURL = this.$axios.defaults.baseURL;
            document.addEventListener('scroll', this.CheckBackToTopBtn);
        }
    }
</script>

<template>
    <div class="blog-area">
        <div class="container">
            <div class="row">
                <div class="col-lg-8">
                    <div v-for="blog in AllBlogs.slice().reverse()" :key="blog.id" class="blog-col">
                        <div class="blog-image">
                            <img loading="lazy" decoding="async" :src="BaseURL + blog.feature_picture">
                        </div>
                        <div class="blog-col-content">
                            <ul>
                                <li><i class="fa fa-user"></i>Admin</li>
                                <span v-for="category in categories" :key="category.id">
                                    <li v-if="category.id === blog.category">
                                        <i class="fa fa-tag"></i> <span>{{ category.name }}</span>
                                    </li>
                                </span>
                                <li><i class="fa fa-clock-o"></i>{{ new Date(blog.date).toDateString() }}</li>
                            </ul>
                            <h2>
                                <router-link :to="{name:'blogs-singleblog', params:{singleblog: blog.url}}">{{ blog.title }}</router-link>
                            </h2>
                            <p v-html="blog.descriptions.slice(0,100) + '...'"></p>
                            <router-link class="btn btn-primary my-btn" :to="{name:'blogs-singleblog', params:{singleblog: blog.url}}">Read More <i class="fa fa-arrow-right"></i></router-link>
                        </div>
                    </div>
                </div>
                <div class="col-lg-4">
                    <div class="sidebar-col">
                        <div class="widget sidebar-search-widget">
                            <form>
                                <div class="input-group">
                                    <span class="input-group-btn">
                                        <button type="submit" class="btn"><i class="fa fa-search"></i></button>
                                    </span>
                                    <input placeholder="Search" class="form-control" name="search-field" type="text">
                                </div>
                            </form>
                        </div>
                        <div class="widget categories-widget">
                            <h4 class="sidebar-title">Blog Categories</h4>
                            <ul>
                                <li v-for="category in categories.slice().reverse()" :key="category.id">
                                    <i class="fa fa-arrow-circle-right"></i>
                                    <a href="#">{{ category.name }}</a>
                                </li>
                            </ul>
                        </div>
                        <div class="widget post-widget">
                            <h4 class="sidebar-title">Latest Post</h4>
                            <div v-for="blog in AllBlogs.slice(0,4).reverse()" :key="blog.id" class="post-item">
                                <img  loading="lazy" decoding="async" :src="BaseURL + blog.feature_picture">
                                <p><a href="#">{{blog.title}}</a></p>
                                <span>{{ new Date(blog.date).toDateString() }}</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div v-if="GoTop" class="back-to-top" @click="BackToTop">
                <button class="btn">
                    <svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%" fill="currentColor" class="bi bi-arrow-up-circle-fill" viewBox="0 0 16 16">
                    <path d="M16 8A8 8 0 1 0 0 8a8 8 0 0 0 16 0zm-7.5 3.5a.5.5 0 0 1-1 0V5.707L5.354 7.854a.5.5 0 1 1-.708-.708l3-3a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1-.708.708L8.5 5.707V11.5z"/>
                    </svg>
                </button>
            </div>
        </div>
    </div>
</template>

<style scoped>
    .blog-image {
        height: 400px;
        width: 100%;
    }
    .blog-image img {
        height: 100%;
        width: 100%;
        object-fit: cover;
    }
    .post-item img {
        height: 70px;
        width: 70px;
        border-radius: 50%;
        object-fit: cover;
    }
    .back-to-top {
        background-color: #2791BF;
        position: fixed;
        right: 1%;
        top: 80%;
        z-index: 1;
        height: 50px;
        width: 50px;
        padding: 5px;
        border-radius: 100%;
        animation: BackToTop infinite ease-in-out;
    }
    @keyframes BackToTop{
        from {
            top: 80%;
        }
        to {
            top: 70%;
        }
    }
    .back-to-top .btn {
        padding: 0;
    }
    .back-to-top .btn:focus {
        box-shadow: none;
    }
    .back-to-top .btn svg {
        color: #fff;
    }
    .back-to-top .btn svg:hover {
        color: #3FEEF7;
    }
</style>