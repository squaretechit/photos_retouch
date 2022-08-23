<script>
    export default {
        name: "SingleBlog",
        data: () => ({BlogInfo: ''}),
        computed: {AllBlogs () {return this.$store.state.all_blogs_info}},
        mounted() {
            setTimeout(()=> {
                document.querySelector('#MainHeader').className = "header-area sticky";
                document.querySelector('#loader').classList.remove('active');
            }, 1000);
        },
        created(){
            setTimeout(()=> {
                this.BlogInfo = this.AllBlogs.find((blog) => blog.url === this.$route.params.singleblog);
            }, 1000);
        },
        head () {
            return {
                titleTemplate: `Photos Retouch | ${this.BlogInfo['title']}`
            }
        },
        beforeRouteEnter(to, form, next) {
            next(vm => {
            setTimeout(()=> {
                const exists = vm['AllBlogs'].some((blog) => blog.url === to.params.singleblog)
                if (!exists){
                return vm['$nuxt'].error({ statusCode: 404, message: 'Page Not Found' })
                }
            }, 500)
            });
        },
    };
</script>

<template>
    <div>
        <LazySingleblogSingleBlog/>
        <LazyHomeContactSeparatorComp />
    </div>
</template>