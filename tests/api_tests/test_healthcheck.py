from tests.base import BaseTestCase


class TestHealthcheck(BaseTestCase):
    def test_should_return_200(self):
        response = self._get_healthcheck()

        self.assert200(response)

    def _get_healthcheck(self):
        return self.client.get('/healthcheck')
