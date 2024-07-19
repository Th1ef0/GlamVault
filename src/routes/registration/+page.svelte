<script>
    import Registration from "$lib/components/Registration.svelte";
</script>

<section>
    <div class="main">
        <div class="registration-block">
            <Registration />
        </div>
    </div>
</section>

<style>
    .main {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100vh;
    }

    .photo-block {
        flex: 1;
        display: flex;
        justify-content: center;
    }

    img {
        height: auto;
        width: 100%;
        max-width: 400px;
    }

    .registration-block {
        flex: 1;
        display: flex;
        align-items: center;
        justify-content: center;
        width: 100%;
        padding: 20px;
    }

    @media(min-width: 768px) {
        .main {
            flex-direction: row;
        }

        .photo-block {
            max-width: 50%;
        }

        .registration-block {
            max-width: 50%;
        }
    }
</style>
