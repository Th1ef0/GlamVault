<script>
    let black = "image-selected";
    let blue = "image-regular";
    let tan = "image-regular";
    let color = "Black";
    let mainImage = "/assets/products/product_1_black.jpg";
</script>

<div class="product-whole">
    <img class="primary-image" src={mainImage} alt="Product 1" />
    <div class="product-info block-inline">
        <h2 class="product-title">Long Sleeve Shirt</h2>
        <div class="divider" />
        <p class="product-details block-inline gray">Price:</p>
        <p class="product-price block-inline">$19.99</p>
        <p class="product-details gray">Size:</p>
        <select name="sizes" id="size-select" autocomplete="off" required>
            <option value="">Select</option>
            <option value="small">Small (S)</option>
            <option value="medium">Medium (M)</option>
            <option value="large">Large (L)</option>
            <option value="xlarge">X-Large (XL)</option>
            <option value="xxlarge">XX-Large (XXL)</option>
        </select>
        <div>
            <p class="product-details gray block-inline">Color:</p>
            <p class="product-details block-inline">{color}</p>
        </div>
        <div class="image-container">
            <button
                on:click={() => {
                    black = "image-selected";
                    blue = "image-regular";
                    tan = "image-regular";
                    color = "Black";
                    mainImage = "/assets/products/product_1_black.jpg";
                }}
                class="image-button"
            >
                <img
                    src="/assets/products/product_1_black.jpg"
                    alt="Black"
                    class="image-choose {black} "
                />
            </button>
            <button
                on:click={() => {
                    black = "image-regular";
                    blue = "image-selected";
                    tan = "image-regular";
                    color = "Blue";
                    mainImage = "/assets/products/product_1_blue.jpg";
                }}
                class="image-button"
            >
                <img
                    src="/assets/products/product_1_blue.jpg"
                    alt="Blue"
                    class="image-choose {blue} "
                />
            </button>
            <button
                on:click={() => {
                    black = "image-regular";
                    blue = "image-regular";
                    tan = "image-selected";
                    color = "Tan";
                    mainImage = "/assets/products/product_1_tan.jpg";
                }}
                class="image-button"
            >
                <img
                    src="/assets/products/product_1_tan.jpg"
                    alt="Tan"
                    class="image-choose {tan} "
                />
            </button>
        </div>
        <div class="divider-mini" />
        <p class="product-details big-text">Product Details</p>
        <div>
            <p class="product-details block-inline gray">Fabric Type:</p>
            <p class="product-details block-inline">
                95% Polyester, 5% Spandex
            </p>
        </div>
        <div>
            <p class="product-details block-inline gray">Care Instructions:</p>
            <p class="product-details block-inline">Machine Wash</p>
        </div>
        <div>
            <p class="product-details block-inline gray">Origin:</p>
            <p class="product-details block-inline">China</p>
        </div>
        <div>
            <p class="product-details block-inline gray">Closure Type:</p>
            <p class="product-details block-inline">Button</p>
        </div>
    </div>
    <div class="cart-button block-inline">
        <button class="cart-text">
            Add to Cart
        </button>
    </div>
</div>

<style>
    .cart-text {
        font-family: "Julius Sans One", sans-serif;
        font-weight: 500;
        font-size: 1.5rem;
        text-align: center;
        color: white;
        background-color: black;
        padding: 1.75rem;
        border: solid .25rem black;
        border-radius: 1.5rem;
        transition: all .3s;
    }
    .cart-text:hover {
        cursor: pointer;
        background-color: white;
        color: black;
        transition: all .3s;
    }
    .cart-button {
        margin-left: 12%;
        margin-top: 3%;
    }
    .image-button {
        display: block;
        max-width: 5rem;
        background-color: transparent;
        border-color: transparent;
    }
    .image-selected {
        border: solid 0.25rem #00b9ca;
    }
    .image-regular {
        border: solid 0.01rem black;
    }
    .image-container {
        display: flex;
        justify-content: flex-start;
    }
    .image-choose {
        padding-right: 1%;
        border-radius: 10%;
        box-shadow: 0.1rem 0.1rem 0.1rem gray;
        max-width: 100%;
    }
    #size-select {
        font-size: 1rem;
        width: 10rem;
        height: 2.5rem;
        border: 0;
        outline: none;
        margin-bottom: 0;
        border: solid .1rem black;
        border-radius: .75rem;
        box-sizing: border-box;
    }
    .divider {
        margin-top: 2%;
        min-height: 0.1rem;
        background-color: gray;
        width: 30rem;
    }
    .divider-mini {
        margin-top: 3%;
        min-height: 0.03rem;
        background-color: gray;
        width: 30rem;
    }
    .primary-image {
        max-width: 30%;
        border-radius: 3%;
        display: inline-block;
        vertical-align: top;
        border-color: black;
        border: solid 0.125rem;
        box-shadow: 0.25rem 0.25rem 0.25rem gray;
    }
    .product-whole {
        /* background-color: gray; */
        margin-left: 10%;
        margin-top: 3%;
        display: flex;
        align-items: flex-start;
        justify-items: flex-start;
    }
    .product-title {
        font-family: "Julius Sans One", sans-serif;
        font-weight: 700;
        font-size: 2.5rem;
        text-align: left;
        color: black;
        margin-bottom: 0;
    }
    .product-info {
        vertical-align: top;
        margin-left: 2%;
    }
    .product-details {
        margin-bottom: 0%;
        margin-top: 3%;
        font-family: "Krub", sans-serif;
        font-size: 1rem;
        font-style: normal;
        font-weight: 500;
    }
    .big-text {
        margin-top: 5%;
        font-size: 1.25rem;
        font-weight: 600;
    }
    .block-inline {
        display: inline-block;
    }
    .product-price {
        margin-top: 3%;
        margin-bottom: 0%;
        font-family: "Krub", sans-serif;
        font-size: 1.5rem;
        font-style: normal;
        font-weight: 550;
        color: red;
    }
    .gray {
        color: #606060;
    }
</style>
