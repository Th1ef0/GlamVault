<script lang="ts">
    import axios from "axios";
    import { onMount } from "svelte";
    import { navigate } from "svelte-routing";

    let name = "";
    let description = "";
    let price = 0.0;
    // let image = new Blob();

    async function addProduct() {
        const formData = new FormData();
        formData.append("name", name);
        formData.append("description", description);
        formData.append("price", price.toString());
        // formData.append('image', image);

        const res = await axios.post(
            "http://127.0.0.1:8000/products/new/",
            {
                name: name,
                description: description,
                price: price,
            },
            {
                headers: {
                    'Content-Type': 'application/json'
                }
            }
        )
        .then(function (response) {
            console.log(response);
            navigate('/shoppingList')
        })
        .catch(function (error) {
            console.log(error);
        })
    }

    // function handleImageUpload(event: Event) {
    //     const target = event.target as HTMLInputElement;
    //     if (target.files) {
    //         let image_data = target.files[0];
    //         image = new Blob([image_data], {
    //             type: "image/png",
    //         });
    //     }
    // }
</script>

<div class="full">
    <p class="title-main">Create a New Product</p>
    <div class="divider" />
    <p class="title-secondary">Information about a Product:</p>
    <form on:submit|preventDefault={addProduct} method="get">
        <div class="form-main">
            <label>
                Name:
                <input type="text" class="form-element" bind:value={name} />
            </label>
            <label>
                Price:
                <input type="number" step="0.01" class="form-element" bind:value={price} />
            </label>
            <label>
                Description:
                <input
                    type="text"
                    class="form-element"
                    bind:value={description}
                />
            </label>
            <!-- <label>
                Image:
                <input
                    type="file"
                    accept="image/*"
                    on:change={handleImageUpload}
                    class="form-element"
                />
            </label> -->
            <button type="submit" class="form-button">Add product</button>
        </div>
    </form>
</div>

<style>
    /* Поменять на новый невероятный компонент, чтобы был reusable и были ПРОПС */
    .form-button {
        margin-top: 1%;
        width: 10rem;
        height: 1.75rem;
    }
    .form-main {
        display: flex;
        flex-direction: column;
    }
    .form-element {
        margin-top: 1%;
        width: 20rem;
        height: 1.5rem;
        font-size: 1.25rem;
    }
    .title-secondary {
        margin-bottom: 0%;
        margin-top: 3%;
        font-family: "Krub", sans-serif;
        font-size: 1.25rem;
        font-style: normal;
        font-weight: 600;
    }
    .divider {
        margin-top: 2%;
        min-height: 0.1rem;
        background-color: gray;
        width: 40rem;
    }
    .title-main {
        font-family: "Julius Sans One", sans-serif;
        font-weight: 700;
        font-size: 2.5rem;
        text-align: left;
        color: black;
        margin-bottom: 0;
        margin-left: 1rem;
    }
    .full {
        margin-left: 15%;
    }
</style>
