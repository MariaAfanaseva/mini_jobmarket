<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<style>
  *{
    font: 300 17px 'Open Sans', sans-serif;
  }

  body {
    margin: 0;
    background-color: rgba(238, 238, 238, 0.38)
  }

   @media screen and (max-width: 768px) {
     *{
       font-size: 12px;
     }
   }
</style>
