<div style="display: flex">
    <div class="info-block">
        <div class="user-photo">
            <img src="/assets/account/user.png" alt="User logo">
        </div>

        <div class="inputs-block">
            <input placeholder="Name">
            <input placeholder="Surname">
            <input placeholder="+7(903) 330 30 11">
            <input placeholder="Address">
        </div>

    </div>

    <div class="cart-block">

    </div>
</div>

<style>
    .info-block {
        flex: 1;
        flex-direction: column;
    }

    .user-photo {
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 50px;
    }

    .inputs-block {
        display: flex;
        flex-direction: column;
        gap: 30px;

    }

    input {
        height: 50px;
        font-family: Krub, sans-serif;
        font-size: 20px;
        font-weight: 200;
        text-indent: 10px;
        color: #737373;
        width: 459px;
        border: 1px solid #737373;
        border-radius: 10px;
        margin-left: 50px;
    }

    .cart-block {
        max-width: 1200px;
        margin: 0 auto;
        display: grid;
        gap: 1rem;
        align-items: center;
        justify-items: center;
    }
</style>