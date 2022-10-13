import unittest
from src.main.tss.declarations.consignment import Consignment
from src.main.tss.api.calls.consignment import ConsignmentApiCall
from src.main.tss.api.environment.environments import TestEnvironment


class TestTssConsignmentAPi(unittest.TestCase):
    def setUp(self):
        self._environment = TestEnvironment()
        self._graylaw_eori = self._environment.eori_no

    def test_should_create_consignment(self) -> None:
        ens_number = "ENS000000000405352"

        consignment = Consignment(
            ens_no=ens_number, importer_eori_no=self._graylaw_eori)

        api_call = ConsignmentApiCall(self._environment)
        report = api_call.create(consignment)

        self.assertEqual("SUCCESS", report["result"]["process_message"])
        self.assertTrue(report["result"]["reference"].startswith("DEC"))

    def test_should_read_consignment_eori(self) -> None:
        dec_no = "DEC000000001010576"
        api_call = ConsignmentApiCall(self._environment)
        eori_number = api_call.read_importer_eori(dec_no)

        self.assertEqual(self._graylaw_eori, eori_number)

    def test_should_delete_consignment(self) -> None:
        ens_number = "ENS000000000405352"

        consignment = Consignment(
            ens_no=ens_number, importer_eori_no=self._graylaw_eori)

        api_call = ConsignmentApiCall(self._environment)
        creation_report = api_call.create(consignment)

        dec_reference = creation_report["result"]["reference"]
        cancel_report = api_call.cancel(dec_reference)

        self.assertEqual("SUCCESS", cancel_report["result"]["process_message"])


if __name__ == '__main__':
    unittest.main()
