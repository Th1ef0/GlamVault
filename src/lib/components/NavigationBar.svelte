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
        outline: 0 !important;
        border: 0 !important;
        width: 20px;
        height: 20px;
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

</style>

<script lang="ts">
  function navigateToURL(link: string){
    window.location.href = link;
  }
</script>

<div class="button-container">
    <button class="button" on:click={() => navigateToURL('/')}>
        <img src="/assets/homePage/home.png" alt="Home">
    </button>

    <button class="button" on:click={() => navigateToURL('/authorization')}>
        <img src="/assets/homePage/perm_identity.png" alt="Account">
    </button>

    <button class="button" on:click={() => navigateToURL('/shoppingCart')}>
        <img src="/assets/homePage/shopping_cart.png" alt="Shopping cart">
    </button>

    <button class="button" on:click={() => navigateToURL('/shoppingList')}>
        <img src="/assets/homePage/article.png" alt="About">
    </button>

    <button class="button" on:click={() => navigateToURL('/product/this-should-be-an-id')}>
        <img src="/assets/homePage/tie.png" alt="Product">
    </button>

    <button class="button" on:click={() => navigateToURL('/admin')}>
        <img src="/assets/homePage/admin.png" alt="Admin">
    </button>
</div>