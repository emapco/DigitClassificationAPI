<template>
  <drawing-canvas
      @prediction-response="predictionUpdate"/>
  <results-table :models="models"/>
</template>

<script setup lang='ts'>
import {ref} from "vue";
import DrawingCanvas from '@/components/DrawingCanvas.vue'
import ResultsTable from '@/components/ResultsTable.vue';

const models = ref([])

function predictionUpdate(predictions: any) {
  models.value = predictions
}
</script>
