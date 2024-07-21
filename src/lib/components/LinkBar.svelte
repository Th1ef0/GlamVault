<div class="button-container">
	<button class="button">
		<a href="tel:+79170472451">
			<img src="/assets/footer/call.png" alt="Call" />
		</a>
	</button>

	<button class="button">
		<a href="https://github.com/Th1ef0/GlamVault/tree/main">
			<img src="/assets/footer/github.png" alt="GitHub" />
		</a>
	</button>

	<button class="button">
		<a href="https://www.instagram.com/instagram">
			<img src="/assets/footer/instagram.png" alt="Instagram" />
		</a>
	</button>

	<button class="button">
		<img src="/assets/footer/telegram.png" alt="Telegram" />
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
		width: 340px;
		height: 45px;
		align-items: center;
		justify-content: space-around;
		border-radius: 10px;
		transition: all 0.5s;
		margin-right: 50px;
	}

	.button {
		outline: 0 !important;
		border: 0 !important;
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
			height: 25px;
			align-items: center;
			justify-content: space-around;
			border-radius: 10px;
			transition: all 0.5s;
			margin-right: 10px;
		}
	}
</style>
