# Single Digit Machine Learning Model API
K nearest neighbors classification and random forest classification models were trained using the MNIST digits classification dataset.

The models were implemented in python 3 using the scikit-learn library. In 
particular, the `KNeighborsClassifier` and `RandomForestClassifier` classes were used.

These two models were chosen since they were the best performing (the highest 
scores against the test dataset) out of the four models tested. Afterwards, 
the two models' hyperparameters were fined tuned using the `GridSearchCV` class.

- KNeighborsClassifier optimized hyperparameters
  - algorithm='kd_tree'
  - leaf_size=10
  - n_neighbors=4
  - weights='distance'

- RandomForestClassifier optimized hyperparameters
  -  class_weight='balanced'
  - criterion='gini'
  - max_features='sqrt'
  - n_estimators=700

The application's frontend client codebase (written with Vue.js) is located in 
the `/client` subdirectory. The machine learning model source code is located 
in the `/model` subdirectory. The api codebase is in the root `/` directory.

![client](https://user-images.githubusercontent.com/4152448/169880815-70fb81f2-2902-42c9-a74b-1fde0714e69f.png)


## Start the flask API
In the terminal while in the root project directory run:
```sh
python3 -m flask run
```


## API Documentation

### API endpoint: POST `/api/file`
  Send a request with a `<form>` marked with
  `enctype="multipart/form-data"`.
  Within the form, include a `<input type=file
  name=image>` tag that contains the binary image file. The
  response is encoded in JSON.

#### Python 3
```python
import requests

URL = 'http://127.0.0.1:5000/api/file'
with open('img.png', 'rb') as file:
    files = {'image': file}
    response = requests.post(URL, files=files)
```

#### JavaScript/TypeScript
```javascript
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
```


### API endpoint: POST <code>/api/data</code>
Send a request with a base64 encoded image in the payload data. The response is encoded in JSON.

#### Python 3
```python
import base64
import requests

URL = 'http://127.0.0.1:5000/api/data'
with open('img.png', 'rb') as file:
    b64_img_str = base64.b64encode(file.read())
    response = requests.post(url, data=b64_img_str)
```

#### JavaScript/TypeScript
```javascript
URL = 'http://127.0.0.1:5000/api/data'
async function uploadImageData(b64EncodedImage: string) {
   const response = await fetch(URL, {
     method: "POST",
     mode: "cors",
     body: b64EncodedString
   });
return response.json();
}
```

### Example JSON Response
```json
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
```
