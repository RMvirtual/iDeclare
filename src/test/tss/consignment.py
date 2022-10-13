import re
import unittest

from src.main.tss.api.calls.consignment import ConsignmentApiCall
from src.main.tss.api.environment.environments import TestEnvironment
from src.main.tss.declarations.consignment import Consignment


class TestConsignmentApiCall(unittest.TestCase):
    def setUp(self):
        self._environment = TestEnvironment()
        self._pre_existing_dec_ref = "DEC000000001010576"

        self._consignment = Consignment(
            self._environment.draft_declaration, self._environment.eori_no)

    def test_should_create_consignment(self) -> None:
        api_call = ConsignmentApiCall(self._environment)
        report = api_call.create(self._consignment)

        self.assertTrue(self._is_success_reported(report))
        self.assertTrue(self._is_dec_reference_received(report))

    def test_should_read_importer_eori(self) -> None:
        api_call = ConsignmentApiCall(self._environment)
        eori_no = api_call.read_importer_eori(self._pre_existing_dec_ref)

        self.assertEqual(self._environment.eori_no, eori_no)

    def test_should_delete_consignment(self) -> None:
        api_call = ConsignmentApiCall(self._environment)
        creation_report = api_call.create(self._consignment)

        dec_reference = creation_report["result"]["reference"]
        cancellation_report = api_call.cancel(dec_reference)

        self.assertTrue(self._is_success_reported(cancellation_report))

    @staticmethod
    def _is_success_reported(report: dict[str, dict[str, str]]) -> bool:
        return report["result"]["process_message"] == "SUCCESS"

    @staticmethod
    def _is_dec_reference_received(report: dict[str, dict[str, str]]) -> bool:
        reference = report["result"]["reference"]

        return bool(re.fullmatch(r"DEC\d{15}", reference))


if __name__ == '__main__':
    unittest.main()
