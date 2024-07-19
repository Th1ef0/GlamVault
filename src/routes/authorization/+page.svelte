<script>
    import Authorization from "$lib/components/Authorization.svelte";
</script>

<section>
    <div class="main">
        <div class="photo-block">
            <img src="/assets/authorization/hands.png" alt="Hands" >
        </div>

        <div class="authorization-block">
            <Authorization />
        </div>
    </div>
</section>

<style>
    .main {
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .photo-block {
        flex: 1;
        display: flex;
        justify-content: center;
    }

    img {
        margin-left: 100px;
        height: 50em;
    }

    .authorization-block {
        display: flex;
        align-items: center;
        justify-content: center;
        flex: 1;
        width: 100%;
    }

    @media(min-width: 768px) {
        .main {
            flex-direction: row;
        }

        .photo-block {
            max-width: 50%;
        }

        .authorization-block {
            max-width: 50%;
        }
    }
</style>
