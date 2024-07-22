<script lang="ts">
	import AddToCartButton from '$lib/components/AddToCartButton.svelte';

	import { onMount } from 'svelte';
	import axios from 'axios';

	interface Product {
		id: number;
		name: string;
		description: string;
		price: number;
		quantity: number;
		img: string;
	}

	let products: Product[] = [];

	let baseUrl = 'http://127.0.0.1:8000';

	onMount(async () => {
		try {
			const response = await axios.get(`${baseUrl}/products/`);
			products = response.data;
		} catch (error) {
			console.error('Error fetching products:', error);
		}
	});
</script>

<svelte:head>
	<title>GlamVault | Catalog</title>
	<meta name="items catalog page" content="catalog clothing items" />
</svelte:head>

<div class="cards">
	{#each products as product}
		<div class="cloth-card">
			<div class="block-media overflow-hidden flex justify-center items-center">
				<a href="/product/{product.id}" class="min-w-full h-auto">
					<img src={product.img} alt={product.name} /></a
				>
			</div>

			<div class="text-block">
				<span>{product.name}</span>
				<span style="color: #737373">{product.price}$</span>
			</div>

			<AddToCartButton buttonTitle="Add to cart" />
		</div>
	{/each}
</div>

<style>
	@import url('https://fonts.googleapis.com/css2?family=Julius+Sans+One&family=Krub:ital,wght@0,200;0,300;0,400;0,500;0,600;0,700;1,200;1,300;1,400;1,500;1,600;1,700&family=Libre+Barcode+128+Text&display=swap');

	@media (min-width: 600px) {
		.cards {
			grid-template-columns: repeat(2, 1fr);
		}
	}

	@media (min-width: 900px) {
		.cards {
			grid-template-columns: repeat(3, 1fr);
		}
	}

	@media (min-width: 1200px) {
		.cards {
			grid-template-columns: repeat(4, 1fr);
		}
	}

	.cards {
		max-width: 1200px;
		margin: 0 auto;
		display: grid;
		align-items: center;
		justify-items: center;
	}

	.text-block {
		font-family: Krub, sans-serif;
		font-size: 20px;
		font-weight: 500;
		display: flex;
		justify-content: space-between;
	}

	span {
		margin: 7px;
	}

	.cloth-card {
		border: none;
		color: black;
		margin: 1rem;
		width: 221px;
		height: 390px;
	}

	.block-media {
		border: 3px solid black;
		box-shadow: 0.5rem 0.5rem 0.5rem rgb(215, 215, 215);
		border-radius: 20px;
		width: 221px;
		height: 225px;
	}
</style>
