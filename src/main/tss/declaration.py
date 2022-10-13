import requests
from src.main.file_system.api_environments import ApiEnvironment


class DeclarationHeader:
    def __init__(self, configuration: ApiEnvironment):
        self._configuration = configuration

    def read_declaration(self) -> None:
        response = requests.get(
            url="https://" + self._configuration.domain
                + "/api/x_fhmrc_tss_api/v1/tss_api/headers",
            auth=(self._configuration.user_name, self._configuration.password),
            params="reference=ENS000000000405352"
                   + "&fields=status,arrival_port,seal_number,route,"
                     "carrier_eori"
        )

        return response.json()

    def cancel_declaration(self, ens_number: str) -> dict[str, str]:
        example_data = {
            "op_type": "cancel",
            "declaration_number": ens_number
        }

        response = requests.post(
            url="https://" + self._configuration.domain
                + "/api/x_fhmrc_tss_api/v1/tss_api/headers",
            auth=(self._configuration.user_name, self._configuration.password),
            json=example_data
        )

        return response.json()

    def create_declaration(self) -> str:
        example_data = {
            "op_type": "create",
            "declaration_number": "",
            "movement_type": "3",
            "identity_no_of_transport": "xy12345",
            "nationality_of_transport": "GB",
            "conveyance_ref": "",
            "arrival_date_time": "13/10/2022 10:00:00",
            "arrival_port": "GBAUBELBELBEL",
            "place_of_loading": "Birkenhead",
            "place_of_unloading": "Belfast",
            "seal_number": "s123456",
            "route": "gb-ni",
            "transport_charges": "Y",
            "carrier_eori": "XI123456789012",
            "carrier_name": "",
            "carrier_street_number": "",
            "carrier_city": "",
            "carrier_postcode": "",
            "carrier_country": "",
            "haulier_eori": ""
        }

        response = requests.post(
            url="https://" + self._configuration.domain +
                "/api/x_fhmrc_tss_api/v1/tss_api/headers?",
            auth=(self._configuration.user_name, self._configuration.password),
            json=example_data
        )

        return response.json()["result"]["reference"]

