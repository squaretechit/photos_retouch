<script>
    import { ref } from "vue";
    import { useRoute } from "vue-router";
    import store from "@/store";
    import TheHeaderView from "@/components/TheHeader.vue"
    import SingleServiceComp from "@/components/singleServiceComp/SingleServiceComp.vue";
    import HomeContactSeparatorComp from "@/components/homeComp/HomeContactSeparatorComp.vue";
    import FooterComp from "@/components/FooterComp.vue";
    export default {
        name: "SingleServiceView",
        computed: {
            services(){
                return store.state.services;
            }
        },
        components: {
            TheHeaderView,
            SingleServiceComp,
            HomeContactSeparatorComp,
            FooterComp
        },
        data: () => ({
            ServiceURL: ref(useRoute().params.service_name),
            ServiceName: ref('')
        }),
        beforeRouteEnter(to) {
            console.log(store.state.services_info)
            const NotFound = store.state.services_info.some((service) => service.url === to.params.service_name);
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
            GetServices() {
                const AllServices = store.state.services_info.find((service) => service.url === this.ServiceURL);
                this.ServiceName = AllServices['name'];
                this.SomeMeta();
            },
            SomeMeta() {
                document.title = `Photos Retouch | ${this.ServiceName}`;
                document.querySelector('#MainHeader').classList.add('header-two-area');
            }
        },
        mounted() {
            this.GetServices();
            console.log('After Loaded')
            // console.log(store.state.services_info)
        }
    };
</script>

<template>
    <div>
        <TheHeaderView/>
        <SingleServiceComp />
        <HomeContactSeparatorComp />
        <FooterComp />
    </div>
</template>