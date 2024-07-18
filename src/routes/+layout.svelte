<script>
import Header from "$lib/components/Header.svelte";
import Footer from "$lib/components/Footer.svelte";
import "../app.css";
</script>

<style>
    main {
        min-height: 36em;
        padding-top: 5em;
    }
</style>

<Header />
<main>
    <slot />
    <div style="min-height: 5rem;" />
</main>
<Footer />
