import unittest
from src.main.tss.api.model import TssApi
from src.main.tss.api.environment.environments import TestEnvironment


class TestTssApi(unittest.TestCase):
    def setUp(self):
        self._environment = TestEnvironment()

    def test_should_check_eori_number_is_valid(self):
        api = TssApi(self._environment)

        valid_eori = self._environment.eori_no
        self.assertTrue(api.is_eori_valid(valid_eori))

        invalid_eori = "XI123456798012"
        self.assertFalse(api.is_eori_valid(invalid_eori))


if __name__ == '__main__':
    unittest.main()
