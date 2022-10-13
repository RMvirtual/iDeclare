import datetime
import requests
from src.main.tss.environments import ApiEnvironment
from src.main.tss.url import tss_url


class DeclarationHeader:
    def __init__(self, configuration: ApiEnvironment):
        self._initialise_configuration(configuration)

    def _initialise_configuration(self, configuration: ApiEnvironment):
        self._configuration = configuration
        self._url = tss_url(self._configuration, "declaration_header")

    def create_declaration(self) -> str:
        response = requests.post(
            url=self._url,
            auth=self._configuration.authentication,
            json=self._dummy_data()
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

    def cancel_declaration(self, ens_number: str) -> dict[str, str]:
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

    def _dummy_data(self) -> dict[str, str]:
        tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)

        return {
            "op_type": "create",
            "declaration_number": "",
            "movement_type": "3",
            "identity_no_of_transport": "xy12345",
            "nationality_of_transport": "GB",
            "conveyance_ref": "",
            "arrival_date_time": tomorrow.strftime("%d/%m/%Y") + " 10:00:00",
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
