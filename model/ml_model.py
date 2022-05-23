import pickle
from itertools import islice

import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import Normalizer
from sklearn.tree import DecisionTreeClassifier


class DigitModel:
    def __init__(self, random_state=None):
        self.random_state = random_state
        self.models = {}

        (x_train, self.y_train), (x_test, self.y_test) = tf.keras.datasets.mnist.load_data(path="mnist.npz")

        # x_train = x_train[:6000]
        # y_train = y_train[:6000]
        self.x_train, self.x_test = self.vect_norm_x_image_data(x_train, x_test)
        # # split our feature, target data into train and test vectors
        # self.x_train, self.x_test, self.y_train, self.y_test \
        #     = train_test_split(x_train_normalized,
        #                        y_train, train_size=0.7,
        #                        random_state=self.random_state)

        self.train_sample_class_proportions = \
            pd.Series(self.y_train).value_counts(normalize=True).round(2)

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

    def print_dataset_info(self):
        print(f'Classes: {np.unique(self.y_train)}')
        print(f"Features' shape: {self.x_train.shape}")
        print(f"Targets' shape:{self.y_train.shape}")
        print(f"min: {self.x_train.min()}, max: {self.x_train.max()}")

    def print_train_test_shape(self):
        print(f"x_train shape: {self.x_train.shape}")
        print(f"x_test shape: {self.x_test.shape}")
        print(f"y_train shape: {self.y_train.shape}")
        print(f"y_test shape: {self.y_test.shape}")
        print(f'Proportion of samples per class in train set:\n'
              f'{self.train_sample_class_proportions}')

    def print_top_models(self, top=2):
        best_models = self.get_best_models(top=top)
        print(f'The top {top} models are: ')
        for index, (model, score) in enumerate(best_models):
            print(f'\t{model}-{round(score, 3)}')

    def print_optimized_models(self):
        # models obtained from create_hyperparameter_tuned_models()
        models = (
            KNeighborsClassifier(
                algorithm='kd_tree',
                leaf_size=10,
                n_jobs=-1,
                n_neighbors=4,
                weights='distance'
            ),
            RandomForestClassifier(
                class_weight='balanced',
                criterion='gini',
                max_features='sqrt',
                n_estimators=700,
                n_jobs=-1,
                random_state=self.random_state,
            ),
        )
        self.create_models(models)
        for model in self.models:
            title = 'K-nearest neighbours algorithm' \
                if isinstance(model, KNeighborsClassifier) \
                else 'Random forest algorithm'
            print(f'{title}')
            print(f'best estimator: {model}')
            print(f'accuracy: {round(self.models[model], 3)}\n')

    def create_models(self, models=None):
        if models is None:
            models = (
                KNeighborsClassifier(
                    n_jobs=-1,
                ),
                DecisionTreeClassifier(
                    random_state=self.random_state,
                ),
                LogisticRegression(
                    solver='liblinear',
                    n_jobs=-1,
                ),
                RandomForestClassifier(
                    random_state=self.random_state,
                    n_jobs=-1
                ),
            )
        for model in models:
            self.fit_predict_eval(model)

    def create_hyperparameter_tuned_models(self):
        kn_param_grid = {
            'n_neighbors': [3, 4, 5, 6, 7, 8, 9],
            'weights': ['uniform', 'distance'],
            'algorithm': ['kd_tree', 'brute', 'ball_tree'],
            'leaf_size': [10, 20, 30, 40, 50, 60],
        }
        rf_param_grid = {
            'n_estimators': [200, 300, 400, 500, 600, 700],
            'max_features': ['sqrt', 'log2'],
            'class_weight': ['balanced', 'balanced_subsample'],
            'criterion': ['gini', 'entropy', 'log_loss'],
        }
        kn_grid_search = GridSearchCV(
            estimator=KNeighborsClassifier(n_jobs=-1),
            param_grid=kn_param_grid,
            scoring='accuracy',
            n_jobs=-1,
        )
        rf_grid_search = GridSearchCV(
            estimator=RandomForestClassifier(
                random_state=self.random_state,
                n_jobs=-1,
            ),
            param_grid=rf_param_grid,
            scoring='accuracy',
            n_jobs=-1,
        )
        for model in (kn_grid_search, rf_grid_search):
            # noinspection PyTypeChecker
            model: GridSearchCV = model.fit(self.x_train, self.y_train)
            score = model.best_estimator_.score(self.x_test, self.y_test)
            self.models[model.best_estimator_] = score
            print(f'best estimator: {model.best_estimator_}')
            print(f'best parameters: {model.best_params_}')
            print(f'accuracy: {round(score, 3)}\n')

    def fit_predict_eval(self, model):
        model = model.fit(self.x_train, self.y_train)
        score = model.score(self.x_test, self.y_test)
        print(f'Model: {model}\nAccuracy: {round(score, 4)}\n')
        self.models[model] = score

    def get_best_models(self, top=1):
        # sort models by decreasing score
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
    # digit_model.create_hyperparameter_tuned_models()

    digit_model.print_optimized_models()
    digit_model.pickle_models()
