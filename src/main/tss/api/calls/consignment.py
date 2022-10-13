import requests
from src.main.tss.api.environment.environments import ApiEnvironment
from src.main.tss.api.environment.url import tss_url
from src.main.tss.declarations.consignment import Consignment


class ConsignmentApiCall:
    def __init__(self, configuration: ApiEnvironment):
        self._configuration = configuration
        self._url = tss_url(self._configuration, "consignment")

    def create(self, consignment: Consignment) -> dict[str, str]:
        response = requests.post(
            url=self._url,
            auth=self._configuration.authentication,
            json=consignment.dummy_consignment()
        )

        return response.json()

    def read_importer_eori(self, consignment_reference: str) -> str:
        response = requests.get(
            url=self._url,
            auth=self._configuration.authentication,
            params="reference="
                   + consignment_reference + "&fields=importer_eori"
        )

        return response.json()["result"]["importer_eori"]

    def cancel(self, dec_number: str) -> dict[str, str]:
        example_data = {
            "op_type": "cancel",
            "consignment_number": dec_number
        }

        response = requests.post(
            url=self._url,
            auth=self._configuration.authentication,
            json=example_data
        )

        return response.json()
