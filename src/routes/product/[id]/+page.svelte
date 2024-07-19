<script lang="ts">
    import axios from 'axios';
    import {page} from '$app/stores';

    interface Product {
        id: number;
        name: string;
        description: string;
        price: number;
        quantity: number;
    }

    let product: Product | null = null;
    let baseUrl = 'http://localhost:8000';

    $: {
        const pathSegments = $page.url.pathname.split('/');
        const id = pathSegments[pathSegments.length - 1];
        if (id) {
            fetchProduct(id);
        }
    }

    async function fetchProduct(id: string) {
        try {
            const response = await axios.get(`${baseUrl}/products/${id}`);
            product = response.data;
        } catch (error) {
            console.error('Error fetching product:', error);
        }
    }
</script>

{#if product}
    <div class="product-whole">
        <img class="primary-image" src="" alt="Product 1"/>
        <div class="product-info block-inline">
            <h2 class="product-title">{product.name}</h2>
            <div class="divider"/>
            <p class="product-details block-inline gray">Price:{product.price}$</p>
            <p class="product-details gray">Size:</p>
            <select name="sizes" id="size-select" autocomplete="off" required>
                <option value="">Select</option>
                <option value="small">Small (S)</option>
                <option value="medium">Medium (M)</option>
                <option value="large">Large (L)</option>
                <option value="xlarge">X-Large (XL)</option>
                <option value="xxlarge">XX-Large (XXL)</option>
            </select>

            <div class="divider-mini"/>
            <p class="product-details big-text">Product Details</p>
            <div>
                <p class="product-details block-inline">{product.description}</p>
            </div>
        </div>

        <div class="cart-button block-inline">
            <button class="cart-text">
                Add to Cart
            </button>
        </div>
    </div>
{:else}
    <p>Loading...</p>
{/if}

<style>
    /*.cart-text {*/
    /*    font-family: "Julius Sans One", sans-serif;*/
    /*    font-weight: 500;*/
    /*    font-size: 1.5rem;*/
    /*    text-align: center;*/
    /*    color: black;*/
    /*    background-color: white;*/
    /*    padding: 1.75rem;*/
    /*    border: solid .25rem black;*/
    /*    border-radius: 1.5rem;*/
    /*    transition: all .3s;*/
    /*}*/

    /*.cart-text:hover {*/
    /*    cursor: pointer;*/
    /*    background-color: black;*/
    /*    color: white;*/
    /*    transition: all .3s;*/
    /*}*/

    .cart-button {
        margin-left: 12%;
        margin-top: 3%;
    }

    /*.image-button {*/
    /*    display: block;*/
    /*    max-width: 5rem;*/
    /*    background-color: transparent;*/
    /*    border-color: transparent;*/
    /*}*/

    /*.image-selected {*/
    /*    border: solid 0.25rem #00b9ca;*/
    /*}*/

    /*.image-regular {*/
    /*    border: solid 0.01rem black;*/
    /*}*/

    /*.image-container {*/
    /*    display: flex;*/
    /*    justify-content: flex-start;*/
    /*}*/

    /*.image-choose {*/
    /*    padding-right: 1%;*/
    /*    border-radius: 10%;*/
    /*    box-shadow: 0.1rem 0.1rem 0.1rem gray;*/
    /*    max-width: 100%;*/
    /*}*/

    #size-select {
        font-size: 1rem;
        width: 10rem;
        height: 2.5rem;
        border: 0;
        outline: none;
        margin-bottom: 0;
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
        margin-bottom: 0;
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

    /*.product-price {*/
    /*    margin-top: 3%;*/
    /*    margin-bottom: 0%;*/
    /*    font-family: "Krub", sans-serif;*/
    /*    font-size: 1.5rem;*/
    /*    font-style: normal;*/
    /*    font-weight: 550;*/
    /*    color: red;*/
    /*}*/

    .gray {
        color: #606060;
    }
</style>
