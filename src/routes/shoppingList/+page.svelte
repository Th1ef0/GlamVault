<script>
    import AddToCartButton from "$lib/components/AddToCartButton.svelte";
</script>

<div class="cards">
    <div class="cloth-card">
        <div class="block-media"></div>

        <div class="text-block">
            <span>T-Shirt</span>
            <span style="color: #737373">205$</span>
        </div>

        <AddToCartButton />
    </div>

    <div class="cloth-card">
        <div class="block-media"></div>

        <div class="text-block">
            <span>T-Shirt</span>
            <span style="color: #737373">205$</span>
        </div>

        <AddToCartButton />
    </div>

    <div class="cloth-card">
        <div class="block-media"></div>

        <div class="text-block">
            <span>T-Shirt</span>
            <span style="color: #737373">205$</span>
        </div>

        <AddToCartButton />
    </div>

    <div class="cloth-card">
        <div class="block-media"></div>

        <div class="text-block">
            <span>T-Shirt</span>
            <span style="color: #737373">205$</span>
        </div>

        <AddToCartButton />
    </div>

    <div class="cloth-card">
        <div class="block-media"></div>

        <div class="text-block">
            <span>T-Shirt</span>
            <span style="color: #737373">205$</span>
        </div>

        <AddToCartButton />
    </div>

    <div class="cloth-card">
        <div class="block-media"></div>

        <div class="text-block">
            <span>T-Shirt</span>
            <span style="color: #737373">205$</span>
        </div>

        <AddToCartButton />
    </div>

    <div class="cloth-card">
        <div class="block-media"></div>

        <div class="text-block">
            <span>T-Shirt</span>
            <span style="color: #737373">205$</span>
        </div>

        <AddToCartButton />
    </div>

    <div class="cloth-card">
        <div class="block-media"></div>

        <div class="text-block">
            <span>T-Shirt</span>
            <span style="color: #737373">205$</span>
        </div>

        <AddToCartButton />
    </div>
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Julius+Sans+One&family=Krub:ital,wght@0,200;0,300;0,400;0,500;0,600;0,700;1,200;1,300;1,400;1,500;1,600;1,700&family=Libre+Barcode+128+Text&display=swap');

    @media (min-width: 600px) {
        .cards { grid-template-columns: repeat(2, 1fr); }
    }

    @media (min-width: 900px) {
        .cards { grid-template-columns: repeat(3, 1fr); }
    }

    @media (min-width: 1200px) {
        .cards { grid-template-columns: repeat(4, 1fr); }
    }

    .cards {
        max-width: 1200px;
        margin: 0 auto;
        display: grid;
        gap: 1rem;
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
        padding: 1rem;
        width: 221px;
        height: 331px;
    }

    .block-media {
        border: 3px solid black;
        box-shadow: 0.5rem 0.5rem 0.5rem rgb(215, 215, 215);
        border-radius: 20px;
        width: 221px;
        height: 253px;
    }

</style>