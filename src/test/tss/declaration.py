import re
import unittest

from src.main.tss.api.calls.declaration import DeclarationHeaderApiCall
from src.main.tss.api.environment.environments import TestEnvironment
from src.main.tss.declarations.declaration_header import DeclarationHeader


class TestDeclarationHeaderApiCall(unittest.TestCase):
    def setUp(self):
        self._environment = TestEnvironment()
        self._graylaw_eori = self._environment.eori_no
        self._declaration_header = DeclarationHeader()
        self._dummy_draft = self._environment.draft_declaration

    def test_should_create_declaration(self) -> None:
        api_call = DeclarationHeaderApiCall(self._environment)
        ens_no = api_call.create(self._declaration_header)

        ens_reference_received = bool(re.fullmatch(r"ENS\d{15}", ens_no))
        self.assertTrue(ens_reference_received)

    def test_should_find_declaration_ens_is_draft(self) -> None:
        api_call = DeclarationHeaderApiCall(self._environment)
        ens_draft_exists = api_call.is_ens_no_draft(self._dummy_draft)

        self.assertTrue(ens_draft_exists)

    def test_should_cancel_declaration(self) -> None:
        api_call = DeclarationHeaderApiCall(self._environment)
        ens_reference = api_call.create(self._declaration_header)
        report = api_call.cancel(ens_reference)

        success_reported = (report["result"]["process_message"] == "SUCCESS")
        self.assertTrue(success_reported)


if __name__ == '__main__':
    unittest.main()
