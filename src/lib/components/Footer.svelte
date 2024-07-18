<script lang="ts">
    import LinkBar from "$lib/components/LinkBar.svelte";

    function navigateToURL(link: string){
        window.location.href = link;
    }
</script>

<div class="footer">
    <div class="flexbox">
        <div class="text-code">
            GlamVault
        </div>

        <button on:click={() => navigateToURL('/about')} class="button">
            ABOUT US
        </button>
    </div>

    <LinkBar />
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Julius+Sans+One&family=Krub:ital,wght@0,200;0,300;0,400;0,500;0,600;0,700;1,200;1,300;1,400;1,500;1,600;1,700&family=Libre+Barcode+128+Text&display=swap');

    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 60px;
        box-shadow: rgba(0, 0, 0, 0.35) 0 5px 30px;
        background: black;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px;
        z-index: 2;
    }

    .flexbox {
        display: flex;
        align-content: center;
        justify-content: center;
    }

    .button {
        font-family: "Krub", sans-serif;
        color: white;
        font-weight: 200;
        font-size: 30px;
        max-height: 50px;
        margin-top: 10px;
        margin-left: 20px;
        border-radius: 15px;
        font-style: normal;
        padding: 5px;
        background: black;
        border: none;
        transition: all ease-in-out 0.3s;
        cursor: pointer;
    }

    .button:hover {
        background: white;
        color: black;
    }

    .text-code {
        font-family: "Libre Barcode 128 Text", system-ui;
        color: white;
        font-weight: 400;
        font-size: 32px;
        margin-left: 20px;
        margin-top: 5px;
        font-style: normal;
        padding: 10px;
    }
</style>
