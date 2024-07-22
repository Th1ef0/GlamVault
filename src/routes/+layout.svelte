<script>
	import Header from '$lib/components/Header.svelte';
	import Footer from '$lib/components/Footer.svelte';
	import '../app.css';
</script>

<Header />
<main>
	<slot />
</main>
<Footer />

<style>
	main {
		min-height: 36em;
		padding-top: 3.5em;
		padding-bottom: 60px;
	}
</style>
