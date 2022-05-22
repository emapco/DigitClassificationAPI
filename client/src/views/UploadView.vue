<template>
  <upload-image-button
      @prediction-response="predictionUpdate"/>
  <results-table :models="models"/>
</template>

<script setup lang='ts'>
import {ref} from "vue";
import UploadImageButton from '@/components/UploadImageForm.vue';
import ResultsTable from '@/components/ResultsTable.vue';

const models = ref([])

function predictionUpdate(predictions: any) {
  models.value = predictions
}
</script>
