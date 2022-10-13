from src.main.file_system.api_environments import ApiEnvironment
from src.main.tss.declaration import DeclarationHeader
from src.main.tss.consignment import Consignment


class TssApi:
    def __init__(self, configuration: ApiEnvironment):
        self._configuration = configuration

    def is_eori_valid(self, eori_number: str) -> bool:
        dummy_declaration = DeclarationHeader(self._configuration)
        ens_no = dummy_declaration.create_declaration()

        consignment = Consignment(self._configuration)
        report = consignment.create_consignment(ens_no, eori_number)
        success = report["result"]["process_message"] == "SUCCESS"

        if success:
            consignment.cancel_consignment(report["result"]["reference"])

        dummy_declaration.cancel_declaration(ens_no)

        return success
