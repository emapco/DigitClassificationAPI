<template>
  <h1>Single Digit Machine Learning Model</h1>
  <p>
    K nearest neighbors classification and random forest classification
    models were trained using the
    <a href="https://keras.io/api/datasets/mnist/">
      MNIST digits classification dataset
    </a>.
  </p>
  <p>
    The models were implemented in python 3 using the
    <a href="https://scikit-learn.org/">
      scikit-learn
    </a>
    library. In particular, the
    <a href="https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html">
      KNeighborsClassifier</a>
    and
    <a href="https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html">
      RandomForestClassifier</a>
    classes were used.
  </p>
  <p>
    These two models were chosen since they were the best performing
    (highest score against the test dataset) out of the four models tested.
    Afterwards, the two models' hyperparameters were fined tuned using the
    <a href="https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html?highlight=gridsearchcv#sklearn.model_selection.GridSearchCV">
      GridSearchCV</a>
    class.
  </p>
  <div class="modelParameters">
    <ul>
      <li>KNeighborsClassifier optimized hyperparameters
        <ul>
          <li>algorithm='kd_tree'</li>
          <li>leaf_size=10</li>
          <li>n_neighbors=4</li>
          <li>weights='distance'</li>
        </ul>
      </li>
    </ul>
    <ul>
      <li>RandomForestClassifier optimized hyperparameters
        <ul>
          <li>class_weight='balanced'</li>
          <li>criterion='entropy'</li>
          <li>max_features='log2'</li>
          <li>n_estimators=600</li>
        </ul>
      </li>
    </ul>
  </div>
  <p>This web application's frontend was created using Vue.js. The backend
    server and api was created with flask.</p>
  <b-button>Source code add link once publish on github</b-button>
  <br><br>
</template>

<script setup lang='ts'>

import {BButton} from "bootstrap-vue-3";</script>

<style scoped>

ul {
  list-style-type: disc;
  #flex: 1 1 auto;
}

.modelParameters {
  margin: auto;
  display: flex;
  flex-flow: row wrap;
}
</style>