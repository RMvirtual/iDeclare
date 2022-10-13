from src.main.file_system.api_environments import ApiEnvironment
from src.main.tss.declaration import DeclarationHeader
from src.main.tss.consignment import Consignment


class TssApi:
    def __init__(self, configuration: ApiEnvironment):
        self._configuration = configuration

    def is_eori_valid(self, eori_number: str) -> bool:
        draft_ens_no = self._find_draft()

        consignment = Consignment(self._configuration)
        report = consignment.create_consignment(draft_ens_no, eori_number)
        success = report["result"]["process_message"] == "SUCCESS"

        if success:
            dec_number = report["result"]["reference"]
            consignment.cancel_consignment(dec_number)
            print("Cancelling DEC Number:", dec_number)

        return success

    def _find_draft(self) -> str:
        draft_ens_no = self._configuration.draft_declaration
        draft_dec = DeclarationHeader(self._configuration)

        if draft_dec.is_ens_no_draft(draft_ens_no):
            print("Old draft found of:", draft_ens_no)

        else:
            draft_ens_no = draft_dec.create_declaration()
            print("Have made new draft:", draft_ens_no)
            # Needs to add a dummy consignment so that consignment
            # cancellation later does not cancel the entire declaration.
            # Update draft json file here too.

        return draft_ens_no
