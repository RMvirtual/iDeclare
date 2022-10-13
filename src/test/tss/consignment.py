import re
import unittest

from src.main.tss.api.calls.consignment import ConsignmentApiCall
from src.main.tss.api.environment.environments import TestEnvironment
from src.main.tss.declarations.consignment import Consignment


class TestConsignmentApiCall(unittest.TestCase):
    def setUp(self):
        self._environment = TestEnvironment()
        self._own_eori_number = self._environment.eori_no
        self._pre_existing_dec_reference = "DEC000000001010576"
        self._draft_ens = self._environment.draft_declaration

    def test_should_create_consignment(self) -> None:
        # ens_number = "ENS000000000405352"

        consignment = Consignment(self._draft_ens, self._own_eori_number)

        api_call = ConsignmentApiCall(self._environment)
        report = api_call.create(consignment)

        success_reported = report["result"]["process_message"] == "SUCCESS"
        self.assertTrue(success_reported)

        reference = report["result"]["reference"]
        dec_ref_received = bool(re.fullmatch(r"DEC\d{15}", reference))
        self.assertTrue(dec_ref_received)

    def test_should_read_importer_eori(self) -> None:
        # dec_no = "DEC000000001010576"
        api_call = ConsignmentApiCall(self._environment)

        eori_number = api_call.read_importer_eori(
            self._pre_existing_dec_reference)

        self.assertEqual(self._own_eori_number, eori_number)

    def test_should_delete_consignment(self) -> None:
        # ens_number = "ENS000000000405352"

        consignment = Consignment(self._draft_ens, self._own_eori_number)

        api_call = ConsignmentApiCall(self._environment)
        creation_report = api_call.create(consignment)

        dec_reference = creation_report["result"]["reference"]
        report = api_call.cancel(dec_reference)

        success_reported = report["result"]["process_message"] == "SUCCESS"
        self.assertTrue(success_reported)


if __name__ == '__main__':
    unittest.main()
