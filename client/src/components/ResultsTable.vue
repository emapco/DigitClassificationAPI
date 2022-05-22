<template>
  <br>
  <br>
  <div v-for="model in models">
    <h3>{{ model.name }} Prediction: {{ model.prediction }}</h3>
    <h3>{{ model.name }} Probabilities per Class</h3>
    <b-table hover :items="[model.probabilities]"/>
  </div>
</template>

<script setup lang="ts">
import {BTable} from "bootstrap-vue-3";

const props = defineProps(['models']);
</script>

<style scoped>
h3 {
  font-size: 1.25rem;
}
</style>