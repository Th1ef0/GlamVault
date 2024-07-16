<script>
    let inCart = false;
    let quantity = 0;

    function addToCart() {
        quantity = 1;
    }

    function increment() {
        quantity += 1;
    }

    function decrement() {
        quantity -= 1;
    }
</script>

{#if quantity}
    <div class="quantity-control">
        <button class="button-decrement" on:click={decrement}>-</button>
        <div>{quantity}</div>
        <button class="button-increment" on:click={increment}>+</button>
    </div>
{:else}
    <button class="add-to-cart" on:click={addToCart}>
        Add to cart
    </button>
{/if}

<style>
    @import url('https://fonts.googleapis.com/css2?family=Julius+Sans+One&family=Krub:ital,wght@0,200;0,300;0,400;0,500;0,600;0,700;1,200;1,300;1,400;1,500;1,600;1,700&family=Libre+Barcode+128+Text&display=swap');

    .add-to-cart {
        font-family: Krub, sans-serif;
        font-size: 20px;
        font-weight: 500;
        border: 2px solid black;
        border-radius: 15px;
        background: white;
        width: 221px;
        height: 38px;
        cursor: pointer;
        transition: 400ms;
    }

    .add-to-cart:hover {
        background-color: black;
        color: white;
        transition: 400ms;
    }

    button:disabled {
        background-color: black;
    }

    .quantity-control {
        display: flex;
        align-items: center;
        justify-items: center;
        border-radius: 15px;
        font-family: Krub, sans-serif;
        font-size: 20px;
        font-weight: 500;
        background-color: black;
        color: white;
        width: 221px;
        height: 38px;
    }

    .button-increment {
        flex: 1;
        width: 12px;
        height: 26px;
        font-size: 20px;
        border: none;
        background: transparent;
        color: white;
    }

    .button-decrement {
        font-size: 20px;
        flex: 1;
        border: none;
        width: 12px;
        height: 26px;
        background: transparent;
        color: white;
    }
    .quantity-control div {
        flex: 1;
        text-align: center;
    }


</style>