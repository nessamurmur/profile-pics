from hypothesis import given, assume
from importer import pic_importer
import hypothesis.strategies as strategies
import unittest
import uuid
import validators


class ImporterTest(unittest.TestCase):
    @given(strategies.basic(generate=lambda _random, _: str(uuid.uuid4())))
    def test_importer_returns_an_image(self, user_id):
        assert "gif" in pic_importer.picture_for(user_id)
