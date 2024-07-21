<script>
	import Authorization from '$lib/components/Authorization.svelte';
</script>

<svelte:head>
	<title>Authorization</title>
	<meta name="authorization page" content="authorization field" />
</svelte:head>

<section>
	<div class="main">
		<div class="photo-block">
			<img src="/assets/authorization/hands.png" alt="Hands" />
		</div>

		<div class="authorization-block">
			<Authorization />
		</div>
	</div>
</section>

<style>
	.main {
		display: flex;
		align-items: center;
		justify-content: center;
		height: 75vh;
	}

	.photo-block {
		flex: 1;
		display: flex;
		justify-content: center;
	}

	img {
		margin-left: 100px;
		height: 50em;
	}

	.authorization-block {
		margin-top: 5rem;
		display: flex;
		align-items: center;
		justify-content: center;
		flex: 1;
		width: 100%;
	}

	@media (max-width: 768px) {
		.main {
			flex-direction: row;
		}

		.photo-block {
			display: none;
		}

		.authorization-block {
			max-width: 90%;
		}
	}
</style>
