<template>
  <div class="accordian" role="tablist">

    <b-card no-body>
      <b-card-header header-tag="header" role="tab">
        <b-button block v-b-toggle.accordion-1 variant="info">
          API endpoint: POST <code>/api/file</code>
        </b-button>
      </b-card-header>
      <b-collapse id="accordion-1" accordion="my-accordion"
                  role="tabpanel">
        <b-card-body>
          <b-card-text>
            <p>
              Send a request with a <code>&lt;form&gt;</code> marked with
              <code>enctype="multipart/form-data"</code>.
              Within the form, include a <code>&lt;input type=file
              name=image&gt;</code> tag that contains the binary image file. The
              response is encoded in JSON.
            </p>
            <p><u>Python 3</u></p>
            <code>
          <pre>
            {{ filePythonCode }}
          </pre>
            </code>
            <p><u>JavaScript/TypeScript</u></p>
            <code>
          <pre>
            {{ fileJSCode }}
          </pre>
            </code>
          </b-card-text>
        </b-card-body>
      </b-collapse>
    </b-card>

    <b-card no-body>
      <b-card-header header-tag="header" role="tab">
        <b-button block v-b-toggle.accordion-2 variant="info">
          API endpoint: POST <code>/api/data</code>
        </b-button>
      </b-card-header>
      <b-collapse id="accordion-2" accordion="my-accordion"
                  role="tabpanel">
        <b-card-body>
          <b-card-text>
            <p>
              Send a request with a base64 encoded image in the payload data.
              The
              response is encoded in JSON.
            </p>
            <p><u>Python 3</u></p>
            <code>
          <pre>
            {{ dataPythonCode }}
          </pre>
            </code>
            <p><u>JavaScript/TypeScript</u></p>
            <code>
          <pre>
            {{ dataJSCode }}
          </pre>
            </code>
          </b-card-text>
        </b-card-body>
      </b-collapse>
    </b-card>

    <b-card no-body>
      <b-card-header header-tag="header" role="tab">
        <b-button block v-b-toggle.accordion-3 variant="info">
          Example API Response
        </b-button>
      </b-card-header>
      <b-collapse id="accordion-3" accordion="my-accordion"
                  role="tabpanel">
        <b-card-body>
          <b-card-text>
            <code>
          <pre>
            {{ jsonResponse }}
          </pre>
            </code>
          </b-card-text>
        </b-card-body>
      </b-collapse>
    </b-card>
  </div>
</template>

<script setup lang='ts'>
import {ref} from "vue";
import {
  BButton,
  BCard,
  BCardBody,
  BCardHeader,
  BCardText,
  BCollapse
} from "bootstrap-vue-3";

const filePythonCode = ref(`
    import requests

    URL = 'http://127.0.0.1:5000/api/file'
    with open('img.png', 'rb') as file:
        files = {'image': file}
        response = requests.post(URL, files=files)
`)
const fileJSCode = ref(`
  URL = 'http://127.0.0.1:5000/api/file'
  async function uploadFile(form: HTMLFormElement) {
    const data = new FormData(form);
    const response = await fetch(FILE_URL, {
      method: "POST",
      mode: "cors",
      body: data
    });
    return response.json();
  }
`)
const dataPythonCode = ref(`
    import base64
    import requests

    URL = 'http://127.0.0.1:5000/api/data'
    with open(img_path, 'rb') as file:
        b64_img_str = base64.b64encode(file.read())
        response = requests.post(url, data=b64_img_str)
`)
const dataJSCode = ref(`
  URL = 'http://127.0.0.1:5000/api/data'
  async function uploadImageData(b64EncodedImage: string) {
    const response = await fetch(URL, {
      method: "POST",
      mode: "cors",
      body: b64EncodedString
    });
    return response.json();
  }
`)
const jsonResponse = ref(`
  {
    "models": [
      {
        "name": "K Neighbors",
        "prediction": 3,
        "probabilities": {
          "0": 0.0,
          "1": 0.0,
          "2": 0.0,
          "3": 1.0,
          "4": 0.0,
          "5": 0.0,
          "6": 0.0,
          "7": 0.0,
          "8": 0.0,
          "9": 0.0
        }
      },
      {
        "name": "Random Forest",
        "prediction": 3,
        "probabilities": {
          "0": 0.03,
          "1": 0.06,
          "2": 0.11,
          "3": 0.35,
          "4": 0.07,
          "5": 0.18,
          "6": 0.02,
          "7": 0.04,
          "8": 0.07,
          "9": 0.06
        }
      }
    ]
  }
`)
</script>

<style scoped>

</style>