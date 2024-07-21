<svelte:head>
	<title>Main page</title>
	<meta name="main page of market" content="nav and contacts" />
</svelte:head>

<section>
	<div id="main">
		<img src="/assets/mainpage/style.png" alt="clothes" id="item1" />
		<div id="item2">
			<h1>Welcome To</h1>
			<p>GLAMVAULT</p>
		</div>
	</div>
</section>

<style>
	@import url('https://fonts.googleapis.com/css2?family=Krub:ital,wght@0,200;0,300;0,400;0,500;0,600;0,700&display=swap');

	section {
		display: flex;
		justify-content: center;
		align-items: center;
		height: 70vh;
		margin: 0;
	}

	#main {
		display: flex;
		justify-content: space-between;
		align-items: center;
		width: 90%;
	}

	img {
		max-width: 85vh;
		height: auto;
	}

	#item1 {
		text-align: center;
	}

	#item2 {
		text-align: center;
		padding: 100px 100px;
		border: 4px solid black;
		border-radius: 25px;
		margin: 80px 75px 0;
	}

	h1 {
		font-family: 'Krub', sans-serif;
		font-size: 48px;
		font-style: normal;
		font-weight: 500;
		margin: 0;
	}

	p {
		font-family: 'Julius Sans One', sans-serif;
		font-weight: 400;
		font-size: 64px;
		color: white;
		padding: 30px;
		background: black;
		border-radius: 25px;
		margin: 20px;
	}

	@media (max-width: 768px) {
		section {
			height: 80vh;
		}

		#main {
			flex-direction: column;
			width: 100%;
			height: 100%;
			justify-content: center;
		}

		img {
			display: none;
		}

		#item2 {
			padding: 20px;
			margin: 0;
			width: 90%;
		}

		h1 {
			font-size: 32px;
		}

		p {
			font-size: 32px;
			padding: 15px;
			margin: 10px 0;
		}
	}
</style>
