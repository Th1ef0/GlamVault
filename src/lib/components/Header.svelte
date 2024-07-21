<script>
    import NavigationBar from "$lib/components/NavigationBar.svelte";
</script>

<div class="header">
    <a href="/" class="text-white font-Julius font-normal text-3xl ml-6 transition-all duration-300
    hover:translate-y-[-0.125rem] hover:transition-all hover:duration-300">
        GlamVault
    </a>

 <NavigationBar />
</div>

<style>
 @import url('https://fonts.googleapis.com/css2?family=Julius+Sans+One&family=Krub:ital,wght@0,200;0,300;0,400;0,500;0,600;0,700;1,200;1,300;1,400;1,500;1,600;1,700&family=Libre+Barcode+128+Text&display=swap');

    .header {
     width: 100%;
     height: 60px;
     position: fixed;
     top: 0;
     left: 0;
     box-shadow: rgba(0, 0, 0, 0.35) 0 5px 30px;
     background: black;
     display: flex;
     justify-content: space-between;
     align-items: center;
     padding: 10px;
     z-index: 2;
    }

    .text {
     font-family: "Julius Sans One", sans-serif;
     color: white;
     font-weight: 400;
     font-size: 32px;
     margin-left: 20px;
     font-style: normal;
     padding: 10px;
    }
</style>