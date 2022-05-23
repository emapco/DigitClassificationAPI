<template>
  <b-form method="post"
          enctype=multipart/form-data
          @submit="onUpload($event)"
          ref="form"
  >
    <b-button-group vertical>
      <b-button class="fileButton">
        <label class="custom-file-upload">
          Select file
          <input
              size="60"
              type=file
              accept="image/*"
              name=image
          >
        </label>
      </b-button>
      <b-button type="submit">
        Get Prediction
      </b-button>
    </b-button-group>
  </b-form>
</template>

<script setup lang='ts'>
import {BButton, BButtonGroup, BForm} from "bootstrap-vue-3";
import {uploadImageFile} from '@/api-request'

const emit = defineEmits(['predictionResponse']);

async function onUpload(event: any) {
  const responseText = await uploadImageFile(event.target);
  if (responseText.models) {
    emit('predictionResponse', responseText.models)
  }
}
</script>

<style scoped>
.fileButton {
  padding-inline: 0;
}

input[type="file"] {
  display: none;
}

.custom-file-upload {
  display: inline-block;
  cursor: pointer;
  padding: 0 2rem;
}
</style>