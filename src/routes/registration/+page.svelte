<script>
	import Registration from '$lib/components/Registration.svelte';
</script>

<svelte:head>
	<title>Registration</title>
	<meta name="registration page" content="registration field" />
</svelte:head>

<section>
	<div class="main">
		<div class="registration-block">
			<Registration />
		</div>
	</div>
</section>

<style>
	.main {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		height: 75vh;
		margin-top: 2rem;
	}

	.registration-block {
		flex: 1;
		display: flex;
		align-items: center;
		justify-content: center;
		width: 100%;
		padding: 20px;
	}

	@media (min-width: 768px) {
		.main {
			flex-direction: row;
		}

		.registration-block {
			max-width: 50%;
		}
	}
</style>
