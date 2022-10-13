import requests

from src.main.tss.api.environment.environments import ApiEnvironment
from src.main.tss.api.environment.url import tss_url
from src.main.tss.declarations.declaration_header import DeclarationHeader


class DeclarationHeaderApiCall:
    def __init__(self, configuration: ApiEnvironment):
        self._initialise_configuration(configuration)

    def _initialise_configuration(self, configuration: ApiEnvironment):
        self._configuration = configuration
        self._url = tss_url(self._configuration, "declaration_header")

    def create(self, declaration_header: DeclarationHeader) -> str:
        response = requests.post(
            url=self._url,
            auth=self._configuration.authentication,
            json=declaration_header.dummy_data()
        )

        return response.json()["result"]["reference"]

    def is_ens_no_draft(self, ens_number) -> bool:
        reading = self.read_declaration(ens_number)

        return reading["result"]["status"].lower() == "draft"

    def read_declaration(self, ens_number) -> dict[str, str]:
        response = requests.get(
            url=self._url,
            auth=self._configuration.authentication,
            params="reference=" + ens_number
                   + "&fields=status,arrival_port,seal_number,route,"
                     "carrier_eori"
        )

        return response.json()

    def cancel(self, ens_number: str) -> dict[str, str]:
        example_data = {
            "op_type": "cancel",
            "declaration_number": ens_number
        }

        response = requests.post(
            url=self._url,
            auth=self._configuration.authentication,
            json=example_data
        )

        return response.json()
