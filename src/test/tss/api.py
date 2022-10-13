import unittest
from src.main.tss.api import TssApi
from src.main.file_system.api_environments import TestEnvironment


class TestTssApi(unittest.TestCase):
    def setUp(self):
        self._environment = TestEnvironment()
        self._graylaw_eori = self._environment.eori_no
        self._api = TssApi(self._environment)

    def test_should_check_eori_number_is_valid(self):
        self.assertTrue(self._api.is_eori_valid(self._graylaw_eori))

        invalid_eori = "XI123456798012"
        self.assertFalse(self._api.is_eori_valid(invalid_eori))


if __name__ == '__main__':
    unittest.main()
