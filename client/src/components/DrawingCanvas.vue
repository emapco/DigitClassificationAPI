<template>
  <div class="canvas">
    <vue-drawing-canvas
        ref="VueCanvas"
        v-model:image="image"
        :width="canvasWidth"
        :height="canvasWidth"
        :initial-image="null"
        :lineWidth="10"
        saveAs="png"
        :styles="{
            border: 'solid 1px #000',
        }"
    />
  </div>
  <br>
  <b-button-group>
    <b-button @click="onUpload">Get Prediction</b-button>
    <b-button @click.prevent="VueCanvas.reset()">Reset</b-button>
  </b-button-group>
</template>

<script setup lang='ts'>
import {onMounted, ref} from 'vue'
import VueDrawingCanvas from "vue-drawing-canvas";
import {BButton, BButtonGroup} from "bootstrap-vue-3";
import {uploadImageData} from "@/api-request";

const VueCanvas = ref(null);
const image = ref(null);
const canvasWidth = ref('300');
const emit = defineEmits(['predictionResponse']);

async function onUpload() {
  const responseText = await uploadImageData(image.value);
  if (responseText.models) {
    emit('predictionResponse', responseText.models)
  }
}

onMounted(async () => {
  if (window.innerWidth > 1200) {
    canvasWidth.value = '600';
  } else if (window.innerWidth < 600) {
    canvasWidth.value = '300';
  }
});
</script>

<style scoped>
.canvas {
  display: flex;
  justify-content: center;
}
</style>