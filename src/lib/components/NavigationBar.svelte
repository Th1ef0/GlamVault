<script lang="ts">
	function navigateToURL(link: string) {
		window.location.href = link;
	}
</script>

<div class="button-container">
	<button class="button" on:click={() => navigateToURL('/')}>
		<img src="/assets/homePage/home.png" alt="Home" />
	</button>

	<button class="button" on:click={() => navigateToURL('/authorization')}>
		<img src="/assets/homePage/perm_identity.png" alt="Account" />
	</button>

	<button class="button" on:click={() => navigateToURL('/shoppingList')}>
		<img src="/assets/homePage/article.png" alt="About" />
	</button>

	<button class="button" on:click={() => navigateToURL('/admin')}>
		<img src="/assets/homePage/admin.png" alt="Admin" />
	</button>
</div>

<style>
	button {
		background-color: white;
		border-top-left-radius: 5px;
		border-top-right-radius: 5px;
		border: none;
	}

	.button-container {
		display: flex;
		position: relative;
		background-color: black;
		width: 300px;
		height: 45px;
		align-items: center;
		justify-content: space-around;
		border-radius: 10px;
		/*box-shadow: rgba(0, 0, 0, 0.35) 0 5px 15px,*/
		/*rgba(0, 73, 144, 0.5) 5px 10px 15px;*/
		transition: all 0.5s;
		margin-right: 50px;
	}

	/*.button-container:hover {*/
	/*    width: 400px;*/
	/*    transition: all 0.5s;*/
	/*}*/

	.button {
		outline: 0;
		border: 0;
		width: 30px;
		height: 30px;
		border-radius: 50%;
		background-color: transparent;
		display: flex;
		align-items: center;
		justify-content: center;
		color: #fff;
		transition: all ease-in-out 0.3s;
		cursor: pointer;
	}

	.button:hover {
		transform: translateY(-3px);
	}

	img {
		width: 30px;
		height: 30px;
	}

	@media (max-width: 768px) {
		img {
			width: 20px;
			height: 20px;
		}

		.button-container {
			display: flex;
			position: relative;
			background-color: black;
			width: 150px;
			height: 30px;
			align-items: center;
			justify-content: space-around;
			border-radius: 10px;
			transition: all 0.5s;
			margin-right: 10px;
		}
	}
</style>
