<svelte:head>
	<title>About us</title>
	<meta name="description" content="Info about our company" />
</svelte:head>

<h1>ABOUT US</h1>
<section>
	<span>Welcome to </span>
	<span class="bold-text">"GlamVault"</span>
	<span>- your go-to destination for stylish and high-quality clothing.</span>
	<p>
		Our store offers a wide range of trendy and current fashion pieces that will accentuate your
		individual style. We carefully curate each model to meet the needs of even the most discerning
		customers.
	</p>
	<p>
		We strive to offer only the best to our customers, which is why we work with trusted
		manufacturers and brands. You can expect top-quality materials, excellent craftsmanship, and the
		latest fashion designs when shopping with us.
	</p>
	<p>
		We take pride in providing each customer with exceptional service and personalized attention.
		Our team is always ready to help you find the perfect outfit that enhances your beauty and
		confidence.
	</p>
	<p class="bold-text">With us, you will always be at the forefront of fashion and style!</p>
</section>

<style>
	@import url('https://fonts.googleapis.com/css2?family=Julius+Sans+One&family=Krub:ital,wght@0,200;0,300;0,400;0,500;0,600;0,700;1,200;1,300;1,400;1,500;1,600;1,700&display=swap');

	h1 {
		font-family: 'Julius Sans One', sans-serif;
		font-weight: 400;
		font-size: 2.5rem;
		text-align: center;
		color: white;
		padding: 1.75rem;
		background: black;
		border-radius: 1.75rem;
		margin: 4% auto 2%;
		max-width: 80%;
	}

	section {
		text-align: center;
		padding: 2%;
		border: 0.25rem solid black;
		border-radius: 1.5rem;
		margin: 0 10%;
		background: #f9f9f9;
	}

	p,
	span {
		font-family: 'Krub', sans-serif;
		font-size: 1.25rem;
		font-style: normal;
		font-weight: 500;
		color: #333;
	}

	.bold-text {
		font-weight: bold;
	}

	@media (max-width: 768px) {
		h1 {
			font-size: 2rem;
			padding: 1.25rem;
			margin: 4% auto 2%;
		}

		section {
			padding: 4%;
			margin: 0 5%;
		}

		p,
		span {
			font-size: 1rem;
		}
	}

	@media (max-width: 480px) {
		h1 {
			font-size: 1.75rem;
			padding: 1rem;
			margin: 4% auto 2%;
		}

		section {
			padding: 5%;
			margin: 0 3%;
		}

		p,
		span {
			font-size: 0.875rem;
		}
	}
</style>
