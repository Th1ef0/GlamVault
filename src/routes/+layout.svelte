<script>
import Header from "$lib/components/Header.svelte";
import Footer from "$lib/components/Footer.svelte";
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
</main>
<Footer />
