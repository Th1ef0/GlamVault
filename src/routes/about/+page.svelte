<script>
    let aboutText1 = 'Welcome to  '

    let aboutText1_1 = '"GlamVault"'
    let aboutText1_2 = '- your go-to destination for stylish and high-quality clothing.'

    let aboutText2 = 'Our store offers a wide range of trendy and current fashion pieces that will accentuate your individual style. ' +
        'We carefully curate each model to meet the needs of even the most discerning customers.'

    let aboutText3 = 'We strive to offer only the best to our customers, which is why we work with trusted manufacturers and brands. ' +
        'You can expect top-quality materials, excellent craftsmanship, and the latest fashion designs when shopping ' +
        'with us.'

    let aboutText4 = 'We take pride in providing each customer with exceptional service and personalized attention. ' +
        'Our team is always ready to help you find the perfect outfit that enhances your beauty and confidence.'

    let aboutText5 = 'With us, you will always be at the forefront of fashion and style!'
</script>

<style>

    h1 {
        font-family: "Julius Sans One", sans-serif;
        font-weight: 400;
        font-size: 2.5rem;
        text-align: center;
        color: white;
        padding: 1.75rem;
        background: black;
        border-radius: 1.75rem;
        margin: 4% 40% 2%;
    }

    section {
        text-align: center;
        padding: 2%;
        border: .25rem solid black;
        border-radius: 1.5rem;
        margin: 0 15%;

    }

    p {
        font-family: "Krub", sans-serif;
        font-size: 1.25rem;
        font-style: normal;
        font-weight: 500;
    }
    span {
        font-family: "Krub", sans-serif;
        font-size: 1.25rem;
        font-style: normal;
        font-weight: 500;
    }

    .bold-text{
        font-weight: bold;
    }

</style>

<h1>ABOUT US</h1>
<section>
    <span>{aboutText1}</span>
    <span class="bold-text">{aboutText1_1}</span>
    <span>{aboutText1_2}</span>
    <p>{aboutText2}</p>
    <p>{aboutText3}</p>
    <p>{aboutText4}</p>
    <p class="bold-text">{aboutText5}</p>
</section>

