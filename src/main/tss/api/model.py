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
            print("Cancelling DEC Number:", dec_number)

        return success

    def _find_draft(self) -> str:
        draft_ens_no = self._configuration.draft_declaration
        api_call = DeclarationHeaderApiCall(self._configuration)

        if api_call.is_ens_no_draft(draft_ens_no):
            print("Old draft found of:", draft_ens_no)

        else:
            header = DeclarationHeader()
            draft_ens_no = api_call.create(header)

            print("Have made new draft:", draft_ens_no)
            # Needs to add a dummy consignment so that consignment
            # cancellation later does not cancel the entire declaration.

            # Update draft json file too look at that consignment too.

        return draft_ens_no
