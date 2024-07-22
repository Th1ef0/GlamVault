<script lang="ts">
	import axios from 'axios';
	import { page } from '$app/stores';
	import AddToCartButton from '$lib/components/AddToCartButton.svelte';

	interface Product {
		id: number;
		name: string;
		description: string;
		price: number;
		quantity: number;
		img: string;
	}

	let product: Product | null = null;
	let baseUrl = 'http://localhost:8000';

	$: {
		const pathSegments = $page.url.pathname.split('/');
		const id = pathSegments[pathSegments.length - 1];
		if (id) {
			fetchProduct(id);
		}
	}

	async function fetchProduct(id: string) {
		try {
			const response = await axios.get(`${baseUrl}/products/${id}`);
			product = response.data;
		} catch (error) {
			console.error('Error fetching product:', error);
		}
	}
</script>

<svelte:head>
	<title>Product card</title>
	<meta name="description" content="Product description" />
</svelte:head>

{#if product}
	<div class="product-container">
		<img class="primary-image" src={product.img} alt="" />
		<div class="product-info">
			<h2 class="product-title">{product.name}</h2>
			<div class="divider"></div>

			<p class="product-details gray">Price: {product.price}$</p>

			<p class="product-details gray">Size:</p>

			<div class="w-full flex-row flex justify-center md:justify-start">
				<div class="border-2 w-fit rounded-lg border-black self-center">
					<select class="bg-transparent" name="sizes" id="size-select" autocomplete="off" required>
						<option value="">Select</option>
						<hr />
						<optgroup label="Sizes">
							<option value="small">Small (S)</option>
							<option value="medium">Medium (M)</option>
							<option value="large">Large (L)</option>
							<option value="xlarge">X-Large (XL)</option>
							<option value="xxlarge">XX-Large (XXL)</option>
						</optgroup>
					</select>
				</div>
			</div>

			<div class="divider-mini"></div>
			<p class="product-details big-text">Product Details</p>
			<div>
				<p class="product-details block-inline">{product.description}</p>
			</div>
			<div class="button-no-move">
				<AddToCartButton buttonTitle="Buy now"></AddToCartButton>
			</div>
		</div>
	</div>
{:else}
	<div class="loader-container">
		<div role="status">
			<svg
				aria-hidden="true"
				class="inline w-16 h-16 text-gray-200 animate-spin dark:text-gray-600 fill-black"
				viewBox="0 0 100 101"
				fill="none"
				xmlns="http://www.w3.org/2000/svg"
			>
				<path
					d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z"
					fill="currentColor"
				/>
				<path
					d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z"
					fill="currentFill"
				/>
			</svg>
			<span class="sr-only">Loading...</span>
		</div>
	</div>
{/if}

<style>
	@import url('https://fonts.googleapis.com/css2?family=Julius+Sans+One&family=Krub:ital,wght@0,200;0,300;0,400;0,500;0,600;0,700&display=swap');

	#size-select {
		font-size: 1rem;
		width: 10rem;
		height: 2.5rem;
		border: 0;
		margin-left: -0.3%;
		outline: none;
		margin-bottom: 0;
		border-radius: 0.75rem;
		box-sizing: border-box;
	}

	.loader-container {
		display: flex;
		justify-content: center;
		align-items: center;
		height: 80vh;
	}

	.divider {
		margin-top: 2%;
		min-height: 0.1rem;
		background-color: gray;
		width: 100%;
	}

	.divider-mini {
		margin-top: 3%;
		min-height: 0.03rem;
		background-color: gray;
		width: 100%;
	}

	.primary-image {
		max-width: 100%;
		border-radius: 3%;
		display: block;
		margin: 0 auto;
		border: solid 0.125rem black;
		box-shadow: 0.25rem 0.25rem 0.25rem gray;
	}

	.product-container {
		display: flex;
		flex-direction: column;
		align-items: center;
		margin: 3% 5%;
	}

	.product-title {
		font-family: 'Julius Sans One', sans-serif;
		font-weight: 700;
		font-size: 2rem;
		text-align: center;
		color: black;
		margin-bottom: 1rem;
	}

	.product-info {
		text-align: center;
		width: 100%;
	}

	.product-details {
		margin-bottom: 1rem;
		font-family: 'Krub', sans-serif;
		font-size: 1rem;
		font-weight: 500;
	}

	.big-text {
		margin-top: 1rem;
		font-size: 1.25rem;
		font-weight: 600;
	}

	.block-inline {
		display: inline-block;
	}

	.gray {
		color: #606060;
	}
	.button-no-move {
		justify-content: center;
		align-items: center;
		display: flex;
		flex-direction: row;
	}

	@media (min-width: 768px) {
		.button-no-move {
			display: flex;
			flex-direction: row;
			align-items: start;
			justify-content: start;
		}
		.product-container {
			flex-direction: row;
			align-items: flex-start;
		}

		.primary-image {
			max-width: 30%;
			margin-right: 2%;
		}

		.product-info {
			text-align: left;
			width: 60%;
		}

		.product-title {
			text-align: left;
			font-size: 2.5rem;
		}

		.divider,
		.divider-mini {
			width: 30rem;
		}
	}
</style>
