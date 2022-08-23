<script>
    import {ref} from "vue";
    import {useRoute} from "vue-router";
    import store from "@/store";
    import {baseURL,getAPI} from "@/axios-api";
    export default {
        data: () => ({
            BaseUrlImg: baseURL,
            BlogCompleteURL: ref(''),
            BlogURL: ref(useRoute().params.blog_name),
            categories: ref(store.state.all_categories_info),
            CompleteBlogInfo: ref('[]'),
            TotalBolgs: ref(store.state.all_blogs_info),
            TotalComments: ref([]),
            TotalCommentsCount: ref(0),
            PostMonthName: ref(''),
            VName: ref(''),
            VComment: ref(''),
            VEmail: ref(''),
            VErrors: ref({}),
            VSuccessMessage: ref(''),
        }),
        methods: {
            GetBlog() {
                const blog = store.state.all_blogs_info.find((blog) => blog.url === this.BlogURL);
                this.CompleteBlogInfo = blog;
            },
            GetComments() {
                getAPI
                .get('/blogs-comments/')
                .then(response => {
                    const data = response.data;
                    for (let i = 0; i < data.length; i++) {
                        if (data[i]['blog'] == this.CompleteBlogInfo['id']) {
                            this.TotalComments.push(data[i]);
                        }
                        if (data[i]['published'] && data[i]['blog'] == this.CompleteBlogInfo['id']){
                            this.TotalCommentsCount += 1;
                        }
                    }
                })
            },
            GetMonthName(){
                const month = new Date(this.CompleteBlogInfo['date']).getMonth();
                const month_name_list = ["January","February","March","April","May","June","July","August","September","October","November","December"];
                this.PostMonthName = month_name_list[month];
            },
            validEmail(email) {
                let re =
                    /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
                return re.test(email);
            },
            CommentSubmit(){
                this.VErrors = {};
                if (!this.VName) {
                    this.VErrors['name'] = 'Name Required.';
                }
                if (!this.VEmail) {
                    this.VErrors['email'] = 'Email Required.';
                } else if (!this.validEmail(this.VEmail)) {
                    this.VErrors['email'] = 'Please use a valid Email';
                }
                if (!this.VComment) {
                    this.VErrors['comment'] = 'Comment Required.';
                }
                if (!this.VErrors['name'] && !this.VErrors['email'] && !this.VErrors['comment']) {
                    getAPI.post('/blogs-comments/',{
                        'blog': this.CompleteBlogInfo['id'],
                        'name': this.VName,
                        'email': this.VEmail,
                        'comment': this.VComment
                    })
                    .then(response => {
                        this.VSuccessMessage = response.data['message'];
                        this.VFullName = '';
                        this.VEmail = '';
                        this.VPhone = '';
                        this.VComment = '';
                        this.VSendToServer = true;
                    }).catch(err => console.log(err.message))
                }
            }
        },
        mounted() {
            this.GetBlog();
            this.GetComments();
            this.GetMonthName();
            this.BlogCompleteURL = window.location.href;
            console.log(this.CompleteBlogInfo['id'])
        }
    }
</script>

<template>
    <section>
        <div class="page-name-area page-name-two-area overlay-white single-blog-heading">
            <div class="container">
                <div class="row">
                    <div class="col-lg-12">
                        <div class="page-name-col text-center">
                            <h6>Phototos Retouch</h6>
                            <h2>{{CompleteBlogInfo['title']}}</h2>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- Blog Single Start -->
        <div class="blog-area blog-single-area">
            <div class="container">
                <div class="blog-single-col">
                    <div class="blog-col">
                        <div class="blog-col-img">
                            <img :src="`${BaseUrlImg}${CompleteBlogInfo['feature_picture']}`" alt="" class="img-fluid">
                            <div class="my-date">
                                <h2>{{new Date(CompleteBlogInfo['date']).getDate()}}</h2>
                                <p>{{PostMonthName}}</p>
                            </div>
                        </div>
                        <div class="blog-col-content">
                            <ul>
                                <li><i class="fa fa-user"></i>Admin</li>
                                <span v-for="category in categories" :key="category.id">
                                    <li v-if="category.id === CompleteBlogInfo['category']">
                                        <i class="fa fa-tag"></i> <span>{{category.name}}</span>
                                    </li>
                                </span>
                                <li><i class="fa fa-clock-o"></i>{{new Date(CompleteBlogInfo['date']).toUTCString()}}
                                </li>
                            </ul>
                            <h2>{{CompleteBlogInfo['title']}}</h2>
                        </div>
                    </div>
                    <div v-html="CompleteBlogInfo['descriptions']"></div>
                    <div class="share-icns">
                        <ul>
                            <li>Share :</li>
                            <li><a target="_blank" :href="`https://www.facebook.com/share.php?u=${this.BlogCompleteURL}`"><i
                                        class="fa fa-facebook color-1"></i></a></li>
                            <li><a target="_blank"
                                    :href="`https://twitter.com/share?text=&amp;url=${this.BlogCompleteURL}`"><i
                                        class="fa fa-twitter color-3"></i></a></li>
                            <li><a target="_blank"
                                    :href="`http://www.linkedin.com/shareArticle?mini=true&amp;url=${this.BlogCompleteURL}`"><i
                                        class="fa fa-linkedin color-5"></i></a></li>
                        </ul>
                    </div>
                    <div class="blog-comments">
                        <h4>{{TotalCommentsCount}} Comments on this</h4>
                        <template v-for="comments in TotalComments" :key="comments.id">
                            <div v-if="comments.published" class="blog-comment-box p-4 rounded">
                                <ul>
                                    <li>
                                        <h6>{{comments.name}}</h6>
                                    </li>
                                    <li><i class="fa fa-clock-o"></i> {{new Date(comments.date).toDateString()}}</li>
                                </ul>
                                <span v-html="comments.comment"></span>
                            </div>
                        </template>
                    </div>
                    <div class="comment-form mb-5">
                        <h4>Leave a comment</h4>
                        <form @submit.prevent="CommentSubmit">
                            <p v-if="VSuccessMessage" class="text-center comment-success-message mb-5">{{VSuccessMessage}}</p>
                            <div class="row">
                                <div class="col-sm-12">
                                    <textarea v-model="VComment" :class="{'input-errors': VErrors.comment}" class="form-control" placeholder="Your comment"></textarea>
                                    <p v-if="VErrors.comment" class="mt-0 comment-errors">{{VErrors.comment}}</p>
                                </div>
                                <div class="col-sm-6">
                                    <input v-model="VName" :class="{'input-errors': VErrors.name}" class="form-control" type="text" placeholder="Your name">
                                    <p v-if="VErrors.name" class="mt-0 comment-errors">{{VErrors.name}}</p>
                                </div>
                                <div class="col-sm-6">
                                    <input v-model="VEmail" :class="{'input-errors': VErrors.email}" class="form-control" type="mail" placeholder="Your email address">
                                    <p v-if="VErrors.email" class="mt-0 comment-errors">{{VErrors.email}}</p>
                                </div>
                                <div class="col-sm-12">
                                    <button class="btn btn-primary my-btn" type="submit">SUBMIT</button>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>
<style>
    .comment-success-message {
        background-color: #2791BF;
        padding: 5px;
        color: #fff;
    }
    .input-errors{
        margin-bottom: 0!important;
    }
    .comment-errors {
        color: red;
        margin-bottom: 40px;
    }
    .blog-col-img {
        height: 600px;
    }

    .blog-col-img img {
        height: 100%;
        width: 100%;
        object-fit: cover;
    }

    .single-blog-heading {
        background-image: url("@/assets/images/BlogComp/BlogComp/top-bg-4.jpeg");
    }

    .blog-comment-box {
        padding: 0;
    }
</style>