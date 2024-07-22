<script lang="ts">
	function navigateToURL(link: string) {
		window.location.href = link;
	}
</script>

<div class="registration-block">
	<div class="header">REGISTRATION</div>

	<hr style="margin: 0" />

	<div class="header" style="padding: 10px; font-size: 24px; margin-top: 10px">TELL ABOUT YOU</div>

	<div class="input-block">
		<input placeholder="name" class="input-login" type="text" />
	</div>

	<div class="input-block">
		<input placeholder="surname" class="input-login" type="text" />
	</div>

	<div class="input-block">
		<input placeholder="login" class="input-login" type="text" />
	</div>

	<div class="input-block">
		<input placeholder="password" class="input-login" type="password" />
	</div>

	<div class="submit-button-block">
		<button class="submit-button"> Sign up </button>
	</div>

	<div class="create-account">
		<div style="color: #A6A6A6; font-size: 14px">Already have an account?</div>

		<button on:click={() => navigateToURL('/authorization')}> Sign in </button>
	</div>
</div>

<style>
	@import url('https://fonts.googleapis.com/css2?family=Julius+Sans+One&family=Krub:ital,wght@0,200;0,300;0,400;0,500;0,600;0,700;1,200;1,300;1,400;1,500;1,600;1,700&family=Libre+Barcode+128+Text&display=swap');

	.registration-block {
		width: 90%;
		max-width: 450px;
		color: white;
		background: black;
		border: none;
		border-radius: 15px;
		padding: 20px;
		box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
		font-family: 'Krub', sans-serif;
	}

	.header {
		text-align: center;
		font-size: 20px;
		padding: 10px;
		font-family: 'Julius Sans One', sans-serif;
	}

	.input-login {
		border: none;
		border-radius: 20px;
		padding: 10px;
		width: 100%;
		margin: 5px 0;
		font-family: 'Krub', sans-serif;
		box-sizing: border-box;
	}

	.input-block {
		margin: 10px 0;
		display: flex;
		justify-content: center;
	}

	.submit-button-block {
		display: flex;
		justify-content: center;
		margin-top: 20px;
	}

	.submit-button {
		padding: 10px 20px;
		background: white;
		color: black;
		border: none;
		border-radius: 15px;
		font-family: 'Krub', sans-serif;
		font-size: 16px;
	}

	.submit-button:hover {
		cursor: pointer;
		background-color: #e0e0e0;
	}

	.create-account {
		display: flex;
		justify-content: center;
		align-items: center;
		margin-top: 20px;
		font-family: 'Krub', sans-serif;
		gap: 5px;
	}

	.create-account button {
		background: black;
		border: none;
		color: white;
		font-size: 14px;
	}

	@media (min-width: 768px) {
		.registration-block {
			padding: 30px;
		}

		.header {
			font-size: 24px;
		}

		.input-login {
			padding: 12px;
		}

		.submit-button {
			padding: 12px 24px;
			font-size: 18px;
		}

		.create-account button {
			font-size: 16px;
		}
	}
</style>
