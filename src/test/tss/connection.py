import unittest
from src.main.tss.api import TssApi
from src.main.tss.declaration import DeclarationHeader
from src.main.tss.consignment import Consignment
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

    def test_should_create_declaration(self) -> None:
        header = DeclarationHeader(self._environment)
        ens_reference = header.create_declaration()

        self.assertTrue(ens_reference.startswith("ENS"))

    def test_should_cancel_declaration(self) -> None:
        header = DeclarationHeader(self._environment)
        ens_reference = header.create_declaration()
        report = header.cancel_declaration(ens_reference)

        self.assertEqual("SUCCESS", report["result"]["process_message"])

    def test_should_create_consignment(self) -> None:
        ens_number = "ENS000000000405352"
        consignment = Consignment(self._environment)
        report = consignment.create_consignment(ens_number, self._graylaw_eori)

        self.assertEqual("SUCCESS", report["result"]["process_message"])
        self.assertTrue(report["result"]["reference"].startswith("DEC"))

    def test_should_read_consignment_eori(self) -> None:
        dec_no = "DEC000000001010576"
        consignment = Consignment(self._environment)
        eori_number = consignment.read_consignment(dec_no)

        self.assertEqual(self._graylaw_eori, eori_number)

    def test_should_delete_consignment(self) -> None:
        ens_no = "ENS000000000405352"
        consignment = Consignment(self._environment)

        create_report = consignment.create_consignment(
            ens_no, self._graylaw_eori)

        dec_reference = create_report["result"]["reference"]
        cancel_report = consignment.cancel_consignment(dec_reference)

        self.assertEqual("SUCCESS", cancel_report["result"]["process_message"])


if __name__ == '__main__':
    unittest.main()
