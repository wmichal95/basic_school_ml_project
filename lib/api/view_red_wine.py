from http import HTTPStatus
from lib.config import CONFIG
import numpy as np


def put(body):
    attrs = np.array([[
        body['fixed_acidity'],
        body['volatile_acidity'],
        body['citric_acid'],
        body['residual_sugar'],
        body['chlorides'],
        body['free_sulfur_dioxide'],
        body['total_sulfur_dioxide'],
        body['density'],
        body['pH'],
        body['sulphates'],
        body['alcohol'],
    ]])

    quality = CONFIG.ML_MODEL.predict(attrs)[0]

    return {'quality': int(quality)}, HTTPStatus.OK
