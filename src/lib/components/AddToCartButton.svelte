<button>
    <div class="text">
        Add to cart
    </div>
</button>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Julius+Sans+One&family=Krub:ital,wght@0,200;0,300;0,400;0,500;0,600;0,700;1,200;1,300;1,400;1,500;1,600;1,700&family=Libre+Barcode+128+Text&display=swap');

    button {
        font-family: Krub, sans-serif;
        font-size: 20px;
        font-weight: 500;
        border: 2px solid black;
        border-radius: 15px;
        background: white;
        width: 221px;
        height: 38px;
        cursor: pointer;

        outline: 3px #181717 solid;
        outline-offset: -3px;
        transition: 400ms;
    }

    button:hover {
        background-color: black;
    }

    button:hover .text {
        color: white;
        transition: 400ms;
    }

</style>