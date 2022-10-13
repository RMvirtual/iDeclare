import unittest
from src.main.tss.declarations.declaration import DeclarationHeader
from src.main.tss.api.environments import TestEnvironment


class TestTssDeclaration(unittest.TestCase):
    def setUp(self):
        self._environment = TestEnvironment()
        self._graylaw_eori = self._environment.eori_no

    def test_should_create_declaration(self) -> None:
        header = DeclarationHeader(self._environment)
        ens_reference = header.create_declaration()

        self.assertTrue(ens_reference.startswith("ENS"))

    def test_should_find_declaration_ens_is_draft(self) -> None:
        header = DeclarationHeader(self._environment)

        self.assertTrue(header.is_ens_no_draft(
            self._environment.draft_declaration))

    def test_should_cancel_declaration(self) -> None:
        header = DeclarationHeader(self._environment)
        ens_reference = header.create_declaration()
        report = header.cancel_declaration(ens_reference)

        self.assertEqual("SUCCESS", report["result"]["process_message"])


if __name__ == '__main__':
    unittest.main()
