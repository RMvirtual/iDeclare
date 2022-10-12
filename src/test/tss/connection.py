import unittest
from src.main.tss import connection
from src.main.file_system.credentials import user_credentials


class TestTssApi(unittest.TestCase):
    def test_should_check_eori_number_is_valid(self):
        valid_eori = user_credentials().graylaw_eori_number
        self.assertTrue(connection.is_eori_valid(valid_eori))

        invalid_eori = "XI123456798012"
        self.assertFalse(connection.is_eori_valid(invalid_eori))

    def test_should_create_declaration(self) -> None:
        ens_reference = connection.create_declaration()
        self.assertTrue(ens_reference.startswith("ENS"))

    def test_should_cancel_declaration(self) -> None:
        ens_reference = connection.create_declaration()
        report = connection.cancel_declaration(ens_reference)
        self.assertEqual("SUCCESS", report["result"]["process_message"])

    def test_should_create_consignment(self) -> None:
        eori_number = user_credentials().graylaw_eori_number
        ens_number = "ENS000000000405352"
        report = connection.create_consignment(ens_number, eori_number)

        self.assertEqual("SUCCESS", report["result"]["process_message"])
        self.assertTrue(report["result"]["reference"].startswith("DEC"))

    def test_should_read_consignment_eori(self) -> None:
        consignment = "DEC000000001010576"
        eori_number = connection.read_consignment(consignment)
        correct_eori_number = user_credentials().graylaw_eori_number

        self.assertEqual(correct_eori_number, eori_number)

    def test_should_delete_consignment(self) -> None:
        eori_number = user_credentials().graylaw_eori_number
        ens_number = "ENS000000000405352"
        report = connection.create_consignment(ens_number, eori_number)

        dec_reference = report["result"]["reference"]
        cancel_report = connection.cancel_consignment(dec_reference)

        self.assertEqual(
            "SUCCESS", cancel_report["result"]["process_message"])


if __name__ == '__main__':
    unittest.main()
