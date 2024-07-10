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

<div class="button-container">
    <button class="button">
        <img src="/assets/footer/call.png" alt="Call">
    </button>

    <button class="button">
        <img src="/assets/footer/github.png" alt="GitHub">
    </button>

    <button class="button">
        <img src="/assets/footer/instagram.png" alt="Instagram">
    </button>

    <button class="button">
        <img src="/assets/footer/telegram.png" alt="Telegram">
    </button>
</div>