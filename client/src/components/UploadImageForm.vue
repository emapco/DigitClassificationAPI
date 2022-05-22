<template>
  <form
      method=post
      enctype=multipart/form-data
      @submit.prevent="onUpload($event)"
  >
    <input
        type=file
        accept="image/*"
        name=image
        id="file-input"
    >
    <br><br>
    <input
        type=submit
        value="Get prediction"
    >
  </form>
</template>

<script setup lang='ts'>
import {uploadImageFile} from '@/api-request'

const emit = defineEmits(['predictionResponse']);

async function onUpload(event: any) {
  const responseText = await uploadImageFile(event.target);
  if (responseText.models) {
    emit('predictionResponse', responseText.models)
  }
}
</script>