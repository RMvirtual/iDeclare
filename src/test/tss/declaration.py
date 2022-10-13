import unittest
from src.main.tss.declarations.declaration_header import DeclarationHeader
from src.main.tss.api.environment.environments import TestEnvironment
from src.main.tss.api.calls.declaration import DeclarationHeaderApiCall


class TestTssDeclaration(unittest.TestCase):
    def setUp(self):
        self._environment = TestEnvironment()
        self._graylaw_eori = self._environment.eori_no

    def test_should_create_declaration(self) -> None:
        api_call = DeclarationHeaderApiCall(self._environment)
        header = DeclarationHeader()
        ens_reference = api_call.create(header)

        self.assertTrue(ens_reference.startswith("ENS"))

    def test_should_find_declaration_ens_is_draft(self) -> None:
        api_call = DeclarationHeaderApiCall(self._environment)

        self.assertTrue(api_call.is_ens_no_draft(
            self._environment.draft_declaration))

    def test_should_cancel_declaration(self) -> None:
        api_call = DeclarationHeaderApiCall(self._environment)
        header = DeclarationHeader()
        ens_reference = api_call.create(header)
        report = api_call.cancel(ens_reference)

        self.assertEqual("SUCCESS", report["result"]["process_message"])


if __name__ == '__main__':
    unittest.main()
