<link rel="stylesheet" href="index.css">
<script setup lang="ts">
import {RouterView} from 'vue-router'
import TheAppNav from '@/components/TheAppNav.vue'
import TheModelDescription from "@/components/TheModelDescription.vue";
</script>

<template>
  <the-model-description />
  <the-app-nav>
    <RouterView/>
  </the-app-nav>
</template>

<style>
#app {
  max-width: 1280px !important;
  padding: 2rem;
  margin: auto;
}
</style>










