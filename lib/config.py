import os
from typing import NamedTuple
import pickle


class AppConfig(NamedTuple):
    ENVIRONMENT: str
    ML_MODEL: object


class TestModel:
    def __init__(self, quality):
        self.quality = quality

    def predict(self, *args, **kwargs):
        return [self.quality]


def get_config(environment) -> AppConfig:
    if environment == 'testing':
        return AppConfig(
            ENVIRONMENT='testing',
            ML_MODEL=TestModel(10)
        )
    if environment == 'development':
        return AppConfig(
            ENVIRONMENT='development',
            ML_MODEL=pickle.load(open('model.pkl', 'rb'))
        )
    if environment == 'production':
        return AppConfig(
            ENVIRONMENT='production',
            ML_MODEL=pickle.load(open('model.pkl', 'rb'))
        )

    raise EnvironmentError(f'Unknown enviroment type {environment} in APP_SETTINGS env var')


CONFIG = get_config(os.getenv(
    'APP_SETTINGS',
    'development'
))
