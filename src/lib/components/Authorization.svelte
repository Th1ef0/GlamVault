<style>
    @import url('https://fonts.googleapis.com/css2?family=Julius+Sans+One&family=Krub:ital,wght@0,200;0,300;0,400;0,500;0,600;0,700;1,200;1,300;1,400;1,500;1,600;1,700&family=Libre+Barcode+128+Text&display=swap');
    .authorization-block {
        height: 23em;
        width: 21em;
        color: white;
        background: black;
        border: none;
        border-radius: 15px;
    }

    .header {
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 20px;
        padding: 10px;
        font-family: "Julius Sans One", sans-serif;
    }

    .input-login {
        border: none;
        border-radius: 20px;
        padding: 5px;
        width: 15em;
        text-indent: 5px;
        margin: 4px;
        font-family: "Krub", sans-serif;
    }

    .input-block {
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .remember-block {
        display: flex;
        align-items: center;
        justify-content: center;
        font-family: "Julius Sans One", sans-serif;
        font-size: 10px;
    }

    .submit-button-block {
        display: flex;
        align-items: center;
        justify-content: center;
        height: 100px;
    }

    .submit-button {
        height: 30px;
        width: 70px;
        background: white;
        color: black;
        border: none;
        border-radius: 15px;
        font-family: Krub, sans-serif;
        font-size: 13px;
    }

    .submit-button:hover {
        cursor: pointer;
    }

    .create-account {
        display: flex;
        align-items: end;
        height: 1px;
        justify-content: center;
        font-family: "Krub", sans-serif;
        gap: 5px
    }

</style>

<script lang="ts">
    function navigateToURL(link: string){
        window.location.href = link;
    }
</script>


<div class="authorization-block">
    <div class="header">
        AUTHORIZATION
    </div>

    <hr style="margin: 0">

    <div class="header" style="padding: 25px; font-size: 24px">
        WELCOME BACK
    </div>

    <div class="input-block">
        <input placeholder="login" class="input-login" type="text">
    </div>

    <div class="input-block">
        <input placeholder="password" class="input-login" type="password">
    </div>

    <div style="display: flex; margin-left: 45px; gap: 10px" >
        <label>
            <input type="checkbox" class="input-box" style="accent-color: black">
        </label>
        <div class="remember-block">
            Remember me
        </div>
    </div>

    <div class="submit-button-block">
        <button class="submit-button">
            Sign in
        </button>
    </div>

    <div class="create-account">
        <div style="color: #A6A6A6; font-size: 10px">
            Don't have an account?
        </div>

        <button on:click={() => navigateToURL('/registration')} style="background: black; border: none; color: white; font-size: 10px">
            Sign up
        </button>

    </div>

</div>