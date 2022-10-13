import unittest
from src.main.tss import connection
from src.main.file_system.api_environments import TestEnvironment


class TestTssApi(unittest.TestCase):
    def setUp(self):
        self._environment = TestEnvironment()
        self._api = connection.TssApi(self._environment)

    def test_should_check_eori_number_is_valid(self):
        self.assertTrue(self._api.is_eori_valid(self._environment.EORI_NO))

        invalid_eori = "XI123456798012"
        self.assertFalse(self._api.is_eori_valid(invalid_eori))

    def test_should_create_declaration(self) -> None:
        ens_reference = self._api.create_declaration()
        self.assertTrue(ens_reference.startswith("ENS"))

    def test_should_cancel_declaration(self) -> None:
        ens_reference = self._api.create_declaration()
        report = self._api.cancel_declaration(ens_reference)
        self.assertEqual("SUCCESS", report["result"]["process_message"])

    def test_should_create_consignment(self) -> None:
        ens_number = "ENS000000000405352"

        report = self._api.create_consignment(
            ens_number, self._environment.EORI_NO)

        self.assertEqual("SUCCESS", report["result"]["process_message"])
        self.assertTrue(report["result"]["reference"].startswith("DEC"))

    def test_should_read_consignment_eori(self) -> None:
        consignment = "DEC000000001010576"
        eori_number = self._api.read_consignment(consignment)

        self.assertEqual(self._environment.EORI_NO, eori_number)

    def test_should_delete_consignment(self) -> None:
        ens_number = "ENS000000000405352"

        report = self._api.create_consignment(
            ens_number, self._environment.EORI_NO)

        dec_reference = report["result"]["reference"]
        cancel_report = self._api.cancel_consignment(dec_reference)

        self.assertEqual(
            "SUCCESS", cancel_report["result"]["process_message"])


if __name__ == '__main__':
    unittest.main()
