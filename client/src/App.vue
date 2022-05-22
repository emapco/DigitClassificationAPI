<link rel="stylesheet" href="assets/base.css">
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
  padding: 2rem;
}
</style>










