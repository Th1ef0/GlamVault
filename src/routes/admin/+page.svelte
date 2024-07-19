<script lang="ts">
    import axios from "axios";
    import {navigate} from "svelte-routing";

    let name = "";
    let description = "";
    let price = 0.0;

    function getBase64(): Promise<string> {
        return new Promise((resolve, reject) => {
           const reader = new FileReader();
           const input = document.querySelector("#upload") as HTMLInputElement;
           const files = input.files as FileList;
           const file = files[0];
           reader.readAsDataURL(file);
           reader.onload = function () {
             resolve(reader.result as string);
           };
           reader.onerror = function (error) {
             reject(error);
           };
        });
    }

    async function addProduct(img: string) {
        const formData = new FormData();
        formData.append("name", name);
        formData.append("description", description);
        formData.append("price", price.toString());

        await axios.post(
            "http://127.0.0.1:8000/products/new/",
            {
                name: name,
                description: description,
                price: price,
                img: img,
            },
            {
                headers: {
                    'Content-Type': 'application/json'
                }
            }
        )
            .then(function (response) {
                console.log(response);
                navigate('/')
            })
            .catch(function (error) {
                console.log(error);
            })
    }
</script>

<div class="full">
    <p class="title-main">Create a New Product</p>
    <div class="divider"/>
    <form on:submit|preventDefault={() => {getBase64().then(img => {addProduct(img)})}} method="get">
        <div class="rounded-md border border-indigo-500 bg-gray-50 p-4 shadow-md w-36">
            <label for="upload" class="flex flex-col items-center gap-2 cursor-pointer">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 fill-white stroke-indigo-500"
                     viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                    <path stroke-linecap="round" stroke-linejoin="round"
                          d="M9 13h6m-3-3v6m5 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
                </svg>
                <span class="text-gray-600 font-medium">Upload file</span>
            </label>
            <input id="upload" accept="image/*" type="file" class="hidden"/>
        </div>

        <div class="form-main">
            <label>
                Name:
                <input type="text" class="form-element" bind:value={name}/>
            </label>
            <label>
                Price:
                <input type="number" step="0.01" class="form-element" bind:value={price}/>
            </label>
            <label>
                Description:
                <input
                        type="text"
                        class="form-element"
                        bind:value={description}
                />
            </label>
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
