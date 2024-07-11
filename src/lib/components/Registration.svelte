<style>
    @import url('https://fonts.googleapis.com/css2?family=Julius+Sans+One&family=Krub:ital,wght@0,200;0,300;0,400;0,500;0,600;0,700;1,200;1,300;1,400;1,500;1,600;1,700&family=Libre+Barcode+128+Text&display=swap');
    .authorization-block {
        height: 21em;
        width: 19em;
        color: white;
        background: black;
        border: none;
        border-radius: 15px;
    }

    .header {
        display: flex;
        justify-content: center;
        align-items: end;
        font-size: 22px;
        padding: 15px;
        font-family: "Julius Sans One", sans-serif;
    }

    .input-login {
        border: none;
        border-radius: 20px;
        padding: 5px;
        width: 15em;
        margin: 4px;
        font-family: "Krub", sans-serif;
    }

    .input-block {
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .submit-button-block {
        display: flex;
        align-items: center;
        justify-content: center;
        height: 40px;
    }

    .submit-button {
        height: 30px;
        width: 70px;
        background: white;
        border: none;
        border-radius: 15px;
        font-family: Krub, sans-serif;
        font-size: 13px;
    }

    .create-account {
        display: flex;
        align-items: end;
        height: 20px;
        justify-content: center;
        font-family: "Krub", sans-serif;
    }

</style>

<script lang="ts">
    function navigateToURL(link: string){
        window.location.href = link;
    }
</script>


<div class="authorization-block">
    <div class="header">
        REGISTRATION
    </div>

    <hr style="margin: 0">

    <div class="header" style="padding: 10px; font-size: 24px; margin-top: 10px">
        TELL ABOUT YOU
    </div>

    <div class="input-block">
        <input placeholder="name" class="input-login" type="text">
    </div>

    <div class="input-block">
        <input placeholder="surname" class="input-login" type="password">
    </div>

    <div class="input-block">
        <input placeholder="login" class="input-login" type="password">
    </div>

    <div class="input-block">
        <input placeholder="password" class="input-login" type="password">
    </div>

    <div class="submit-button-block">
        <button class="submit-button">
            Sign up
        </button>
    </div>

    <div class="create-account">
        <div style="color: #A6A6A6; font-size: 10px">
            Already have an account?
        </div>

        <button on:click={() => navigateToURL('/authorization')} style="background: black; border: none; color: white; font-size: 10px">
            Sign in
        </button>

    </div>

</div>