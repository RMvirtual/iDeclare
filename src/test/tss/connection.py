import unittest
from src.main.tss import connection
from src.main.file_system.credentials import user_credentials


class TestTssApi(unittest.TestCase):
    def test_should_create_declaration(self) -> None:
        ens_reference = connection.create_declaration()
        self.assertTrue(ens_reference.startswith("ENS"))

    def test_should_create_consignment(self) -> None:
        eori_number = user_credentials().graylaw_eori_number
        report = connection.create_consignment(eori_number)

        self.assertEqual("SUCCESS", report["result"]["process_message"])
        self.assertTrue(report["result"]["reference"].startswith("DEC"))

    def test_should_read_consignment_eori(self) -> None:
        consignment = "DEC000000001010576"
        eori_number = connection.read_consignment(consignment)
        correct_eori_number = user_credentials().graylaw_eori_number

        self.assertEqual(correct_eori_number, eori_number)


if __name__ == '__main__':
    unittest.main()
