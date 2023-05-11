from flask_testing import TestCase
from app import build_app


class BaseTestCase(TestCase):
    def create_app(self):
        return build_app()

    def setUp(self) -> None:
        super().setUp()

    def tearDown(self) -> None:
        super().tearDown()
