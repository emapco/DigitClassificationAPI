import pickle
from itertools import islice

import numpy as np
import tensorflow as tf
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import Normalizer
from sklearn.tree import DecisionTreeClassifier


class DigitModel:
    def __init__(self, random_state=None, jobs=-1):
        self.random_state: int | None = random_state
        self.jobs: int = jobs
        self.models: dict = {}

        (x_train, y_train), _ = tf.keras.datasets.mnist.load_data(path="mnist.npz")
        x_train = x_train[:24000]
        y_train = y_train[:24000]

        x_train_normalized, = self.vect_norm_x_image_data(x_train, )
        # split our feature and target data into train and test array
        self.x_train, self.x_test, self.y_train, self.y_test \
            = train_test_split(x_train_normalized,
                               y_train, train_size=0.7,
                               random_state=self.random_state)

    @staticmethod
    def vect_norm_x_image_data(*args):
        norm_vect_data = []
        for index, arg in enumerate(args):
            # vectorize image data by reshaping the axes
            vectorized_shape = (arg.shape[0], arg.shape[1] * arg.shape[2])
            vect_arg = np.array(arg).reshape(vectorized_shape)
            # improve performance by normalizing data
            norm_vect_data.append(Normalizer().transform(vect_arg))
        return norm_vect_data

    def create_optimized_models(self):
        # models obtained from create_hyperparameter_tuned_models()
        models = (
            KNeighborsClassifier(
                algorithm='kd_tree',
                leaf_size=10,
                n_jobs=self.jobs,
                n_neighbors=4,
                weights='distance'
            ),
            RandomForestClassifier(
                class_weight='balanced',
                criterion='gini',
                max_features='sqrt',
                n_estimators=700,
                n_jobs=self.jobs,
                random_state=self.random_state,
            ),
        )
        self.create_models(models)

    def create_models(self, models=None):
        if models is None:
            models = (
                KNeighborsClassifier(
                    n_jobs=self.jobs,
                ),
                DecisionTreeClassifier(
                    random_state=self.random_state,
                ),
                LogisticRegression(
                    solver='liblinear',
                    n_jobs=self.jobs,
                ),
                RandomForestClassifier(
                    random_state=self.random_state,
                    n_jobs=self.jobs
                ),
            )
        for model in models:
            self.fit_predict_eval(model)

    def create_hyperparameter_tuned_models(self):
        kn_param_grid = {
            'n_neighbors': [4, 5, 6, 7, 8],
            'weights': ['uniform', 'distance'],
            'algorithm': ['kd_tree', 'auto'],
            'leaf_size': [6, 7, 8, 9, 10],
        }
        rf_param_grid = {
            'n_estimators': [600, 700, 800, 900, 1000],
            'max_features': ['sqrt', 'log2'],
            'class_weight': ['balanced', 'balanced_subsample'],
            'criterion': ['gini', 'entropy', 'log_loss'],
        }
        kn_grid_search: GridSearchCV = GridSearchCV(
            estimator=KNeighborsClassifier(n_jobs=self.jobs),
            param_grid=kn_param_grid,
            scoring="accuracy",
            n_jobs=self.jobs,
        )
        rf_grid_search = GridSearchCV(
            estimator=RandomForestClassifier(
                random_state=self.random_state,
                n_jobs=self.jobs,
            ),
            param_grid=rf_param_grid,
            scoring='accuracy',
            n_jobs=self.jobs,
        )
        for clf in (kn_grid_search, rf_grid_search):
            print('Created GridSearchCV.\nNow searching and fitting...\n')
            # noinspection PyTypeChecker
            clf: GridSearchCV = clf.fit(self.x_train, self.y_train)
            score = clf.best_estimator_.score(self.x_test, self.y_test)
            self.models[clf.best_estimator_] = score  # add best estimator to models dict
            print(f'Best estimator: {clf.best_estimator_}')
            print(f'Best parameters: {clf.best_params_}')
            print(f'Accuracy: {round(score, 4)}\n')

    def fit_predict_eval(self, model):
        model = model.fit(self.x_train, self.y_train)
        score = model.score(self.x_test, self.y_test)
        self.models[model] = score
        print(f'Model: {model}\nAccuracy: {round(score, 4)}\n')

    def print_top_models(self, top=2):
        best_models = self.get_top_models(top=top)
        print(f'The top {top} models are: ')
        for index, (model, score) in enumerate(best_models):
            print(f'\t{model}-{round(score, 3)}')

    def get_top_models(self, top=1):
        # sort models by decreasing score/accuracy
        self.models = {k: v for k, v in
                       sorted(self.models.items(),
                              key=lambda item: item[1],
                              reverse=True)}
        return islice(self.models.items(), top)

    def pickle_models(self):
        num = 0
        for model in self.models.keys():
            with open(f'digit_{num}_model.dat', 'wb') as file:
                pickle.dump(model, file)
                num += 1


if __name__ == '__main__':
    digit_model = DigitModel()
    digit_model.create_hyperparameter_tuned_models()
    # digit_model.print_optimized_models()
    digit_model.pickle_models()
