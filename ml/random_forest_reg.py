import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import seaborn as sns
import matplotlib.pyplot as plt
import pickle

dt = pd.read_csv('winequality-red.csv')

attr_columns = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
                'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
                'pH', 'sulphates', 'alcohol']
target_columns = ['quality']


sns.pairplot(
    dt,
    hue='quality',
    diag_kind='hist')
plt.show()

attributes = dt[attr_columns].to_numpy()
target_values = dt[target_columns].to_numpy().flatten('F')

X_train, X_test, y_train, y_test = train_test_split(attributes, target_values, random_state=42)

forest_model = RandomForestRegressor(
    n_estimators=50,
    random_state=3,
    max_depth=15,
    max_features=3,
)
forest_model.fit(X_train, y_train)


def plot_feature_importances(model):
    n_features = len(attr_columns)
    plt.barh(range(n_features), model.feature_importances_, align='center')
    plt.yticks(np.arange(n_features), attr_columns)
    plt.xlabel('waznosc cechy')
    plt.ylabel('cecha')


plot_feature_importances(forest_model)
plt.gcf().subplots_adjust(bottom=0.15, left=0.25)
plt.show()

pickle.dump(forest_model, open('../../model.pkl', 'wb'))