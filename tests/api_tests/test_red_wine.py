from tests.base import BaseTestCase
import json


class TestPutWinePredict(BaseTestCase):

    def test_should_return_wine_quality(self):
        response = self._put_red_wine(dict(
            fixed_acidity=4.6,
            volatile_acidity=0.12,
            citric_acid=0,
            residual_sugar=0.9,
            chlorides=0.012,
            free_sulfur_dioxide=1,
            total_sulfur_dioxide=6,
            density=0.99,
            pH=2.74,
            sulphates=0.33,
            alcohol=8.5,
        ))

        self.assert200(response)
        self.assertDictEqual(response.json, {'quality': 10})

    def _put_red_wine(self, data):
        return self.client.put(
            '/wine_predict',
            content_type='application/json',
            data=json.dumps(data)
        )
