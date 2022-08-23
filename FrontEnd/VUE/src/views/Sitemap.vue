<script>
    export default {
        name: "SitemapView",
        mounted() {
            document.title = window.location.origin;
                document.close();
                document.open();
            document.write(`
            <?xml version=”1.0” encoding=”UTF-8”>
            <urlset xmlns=”http://www.sitemaps.org/schemas/sitemap/0.9” xmlns:xhtml=”http:www.w3.org/1999/xhtml”>
            <url>
                <loc>https://www.example.com</loc>
                <lastmod>2017-10-06</lastmod>
                <changefreq>weekly</changefreq>
                <priority>0.9</priority>
                <xhtml:link rel=”alternate” hreflang=”en” href=”https://www.example.com”/>
                <xhtml:link rel=”alternate” hreflang=”fr” href=”https://www.example.com/fr”/>
            </url>
            `);
        }
    };
</script>

<template>
</template>

<style>
</style>