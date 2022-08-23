<script>
    import { ref } from "vue";
    import { useRoute } from "vue-router";
    import store from "@/store";
    import TheHeaderView from "@/components/TheHeader.vue"
    import SingleBlogComp from "@/components/singleBlogComp/SingleBlogComp.vue"
    import HomeContactSeparatorComp from "@/components/homeComp/HomeContactSeparatorComp.vue";
    import FooterComp from "@/components/FooterComp.vue";
    export default {
        name: "SingleBlogView",
        components: {
            TheHeaderView,
            SingleBlogComp,
            HomeContactSeparatorComp,
            FooterComp
        },
        data: () => ({
            BlogURL: ref(useRoute().params.blog_name),
            BlogName: ref('')
        }),
        beforeRouteEnter(to) {
            const NotFound = store.state.all_blogs_info.find((blog) => blog.url === to.params.blog_name);
            if (!NotFound){
                return {
                    name: "NotFound",
                    params: {pathMatch: to.path.substring(1).split("/")},
                    query: to.query,
                    hash: to.hash,
                }
            }
        },
        methods: {
            GetBlog () {
                const blog = store.state.all_blogs_info.find((blog) => blog.url === this.BlogURL);
                this.BlogName = blog['title'];
                this.SomeMeta();
            },
            SomeMeta() {
                document.title = `Photos Retouch | ${this.BlogName}`;
                document.querySelector('#MainHeader').classList.remove('header-two-area');
            }
        },
        mounted() {
            this.GetBlog();
        }
    };
</script>

<template>
    <div>
        <TheHeaderView />
        <SingleBlogComp/>
        <HomeContactSeparatorComp/>
        <FooterComp/>
    </div>
</template>