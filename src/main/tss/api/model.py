import re
from src.main.tss.api.environment.environments import ApiEnvironment
from src.main.tss.declarations.declaration_header import DeclarationHeader
from src.main.tss.declarations.consignment import Consignment
from src.main.tss.api.calls.consignment import ConsignmentApiCall
from src.main.tss.api.calls.declaration import DeclarationHeaderApiCall


class TssApi:
    def __init__(self, configuration: ApiEnvironment):
        self._configuration = configuration

    def is_eori_valid(self, eori_number: str) -> bool:
        draft_ens_no = self._find_draft()

        consignment = Consignment(
            ens_no=draft_ens_no, importer_eori_no=eori_number)

        api_call = ConsignmentApiCall(self._configuration)
        report = api_call.create(consignment)
        success = report["result"]["process_message"] == "SUCCESS"

        if success:
            dec_number = report["result"]["reference"]
            api_call.cancel(dec_number)

        return success

    def _find_draft(self) -> str:
        api_call = DeclarationHeaderApiCall(self._configuration)
        draft_ens_no = self._configuration.draft_declaration

        if not api_call.is_ens_no_draft(draft_ens_no):
            draft_ens_no = self._create_new_draft(api_call)

            if re.fullmatch(r"ENS\d{15}", draft_ens_no):
                self._configuration.update_draft(draft_ens_no)

        return draft_ens_no

    def _create_new_draft(self, api_call: DeclarationHeaderApiCall):
        header = DeclarationHeader()
        draft_ens_no = api_call.create(header)

        consignment_api_call = ConsignmentApiCall(self._configuration)

        draft_consignment_for_padding = Consignment(
            ens_no=draft_ens_no,
            importer_eori_no=self._configuration.eori_no
        )

        consignment_api_call.create(draft_consignment_for_padding)

        return draft_ens_no
