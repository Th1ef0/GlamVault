<script lang="ts">
    import axios from "axios";
    import { navigate } from "svelte-routing";
    import MainButton from "$lib/components/MainButton.svelte";
    import { createClient } from '@supabase/supabase-js'

    
    const supabase = createClient('https://agkxhhrlhamiyvutsgnb.supabase.co',
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFna3hoaHJsaGFtaXl2dXRzZ25iIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjE1NjI1NzQsImV4cCI6MjAzNzEzODU3NH0.nHUiErQULQlJJOCgMJjpT09BH-BJhY9LaC_T9t2jdLA')

    let name: string;
    let description: string;
    let price: number;
    let selected: File;
    let photo_flag = false;
    let error_text = "";

    const link = "https://agkxhhrlhamiyvutsgnb.supabase.co/storage/v1/object/public/images/"

    async function addProduct(img: File) {
        const formData = new FormData();
        formData.append("name", name);
        formData.append("description", description);
        formData.append("price", price.toString());

        const { data, error } = await supabase.storage.from('images').upload(`gv_${name}.png`, img);
        if (error) {
            error_text = "Error while uploading image."
            console.log(error);
            return;
        }
        else {
            error_text = "";
            console.log("Success! =D")
        }

        await axios
            .post(
                "http://127.0.0.1:8000/products/new/",
                {
                    name: name,
                    description: description,
                    price: price,
                    img: link + `gv_${name}.png`,
                },
                {
                    headers: {
                        "Content-Type": "application/json",
                    },
                },
            )
            .then(function (response) {
                console.log(response);
                navigate("/");
            })
            .catch(function (error) {
                error_text = "Error while adding product"
                console.log(error);
            });
        console.log("Here")
    }
</script>

<svelte:head>
	<title>Product addition</title>
	<meta name="product addition page" content="product addition field" />
</svelte:head>

<div class="ml-60">
    <p class="title-main">Create a New Product</p>
    <div class="divider" />
    <form
        on:submit|preventDefault={() => {
            error_text = "";
            addProduct(selected);
        }}
        method="get"
        class="form-container"
    >
        {#if photo_flag}
        <div class="flex flex-col">
            <label for="upload" class="flex flex-col items-center gap-2 cursor-pointer
                rounded-md border-4 border-black bg-gray-50 p-4 shadow-md h-[30rem] w-96 mt-8 justify-center
                transition-all duration-300 hover:shadow-2xl hover:transition-all hover:duration-300">
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="h-10 w-10 fill-white stroke-[#202020]"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                    stroke-width="2">
                    <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        d="M9 13h6m-3-3v6m5 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
                </svg>
                <span class="text-gray-600 text-2xl font-medium font-Krub">Photo added successfully</span>
                <input
                    id="upload"
                    accept=".png, .jpg"
                    type="file"
                    class="hidden"
                    on:change={(event) => {
                        if (!event.target) { return; }
                        const file = event.target.files[0];
                        selected = file;
                    }}
                />
            </label>
            <p>File: {selected.name}</p>
        </div>
        {:else}
            <label
                for="upload" class="flex flex-col items-center gap-2 cursor-pointer
                rounded-md border-2 border-black bg-gray-50 p-4 shadow-md h-[30rem] w-96 mt-8 justify-center
                transition-all duration-300 hover:shadow-2xl hover:transition-all hover:duration-300">
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="h-10 w-10 fill-white stroke-[#202020]"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                    stroke-width="2">
                    <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        d="M9 13h6m-3-3v6m5 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
                </svg>
                <span class="text-gray-600 font-medium font-Krub">Add a photo</span>
                <input
                    id="upload"
                    accept=".png, .jpg"
                    type="file"
                    class="hidden"
                    on:change={(event) => {
                        const file = event.target.files[0];
                        selected = file;
                        photo_flag = true;
                    }}
                />
            </label>
        {/if}

        <div class="form-main">
            <input
                type="text"
                class=" bg-gray-50 border-2 border-black rounded-lg font-Krub text-xl h-14 w-96 pl-4
            transition-all duration-300 hover:shadow-2xl hover:transition-all hover:duration-300"
                bind:value={name}
                placeholder="Enter product name"
            />
            <input
                type="number"
                step="0.01"
                bind:value={price}
                placeholder="Enter price of the product"
                class="bg-gray-50 mt-6 border-2 border-black rounded-md pl-4 font-Krub text-base h-10 w-72
            transition-all duration-300 hover:shadow-2xl hover:transition-all hover:duration-300"
            />
            <div>
                <textarea
                    bind:value={description}
                    placeholder="Enter description for the product"
                    class="bg-gray-50 border-2 border-black rounded-lg mt-16 w-[30rem] h-72 pl-4 pt-4 placeholder:align-top
                font-Krub text-base transition-all duration-300 hover:shadow-2xl hover:transition-all hover:duration-300"
                />
            </div>
        </div>
        <div class="flex flex-col">
            <div class="mt-4">
                <MainButton />
            </div>
            <div class="text-red-600">
                {error_text}
            </div>
        </div>
    </form>
</div>

<style>
    .form-container {
        display: flex;
        flex-direction: row;
    }

    .form-main {
        display: flex;
        flex-direction: column;
        margin-top: 2rem;
        margin-left: 8rem;
    }

    .divider {
        margin-top: 2%;
        min-height: 0.1rem;
        background-color: gray;
        width: 60rem;
    }

    .title-main {
        font-family: "Julius Sans One", sans-serif;
        font-weight: 700;
        font-size: 2.5rem;
        text-align: left;
        color: black;
        margin-bottom: 0;
        margin-top: 3rem;
        margin-left: 1rem;
    }
</style>
