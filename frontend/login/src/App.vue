<script setup>
import { RouterLink, RouterView } from "vue-router";
import HelloWorld from "./components/HelloWorld.vue";
import Login from "./components/Login.vue";
import axios from "axios";

const data = async () => {
  try {
    var res = await axios.get("http://127.0.0.1:4000/store");
    console.log("this is res.data: ",res.data[0]['name']);
  } catch (error) {
    console.log(error);
  }
};

data()
</script>


<template>
  <Login />
</template>

<style scoped>

body {
  background-color: #080710;
}
</style>