import requests
from src.main.file_system import api_environments
from src.main.file_system.api_environments import ApiEnvironment


class TssApi:
    def __init__(self, configuration: ApiEnvironment):
        self._configuration = configuration

    def is_eori_valid(self, eori_number: str) -> bool:
        dummy_declaration = self.create_declaration()
        report = self.create_consignment(dummy_declaration, eori_number)

        success = report["result"]["process_message"] == "SUCCESS"

        if success:
            self.cancel_consignment(report["result"]["reference"])

        self.cancel_declaration(dummy_declaration)

        return success

    def read_consignment(self, consignment_reference: str) -> str:
        environment = api_environments.TestEnvironment()

        response = requests.get(
            url="https://" + environment.DOMAIN
                + "/api/x_fhmrc_tss_api/v1/tss_api/consignments",
            auth=(environment.USER_NAME, environment.PASSWORD),
            params="reference=" + consignment_reference
                + "&fields=importer_eori"
        )

        return response.json()["result"]["importer_eori"]


    def cancel_consignment(self, dec_number: str) -> dict[str, str]:
        environment = api_environments.TestEnvironment()

        example_data = {
            "op_type": "cancel",
            "consignment_number": dec_number
        }

        response = requests.post(
            url="https://" + environment.DOMAIN +
                "/api/x_fhmrc_tss_api/v1/tss_api/consignments",
            auth=(environment.USER_NAME, environment.PASSWORD),
            json=example_data
        )

        return response.json()


    def create_consignment(self,
            ens_number: str, importer_eori_number: str) -> dict[str, str]:
        environment = api_environments.TestEnvironment()

        example_data = {
            "op_type": "create",
            "declaration_number": ens_number,
            "consignment_number": "",
            "goods_description": "DUMMY TO CHECK EORI",
            "trader_reference": "",
            "transport_document_number": "DUMMY JOB",
            "controlled_goods": "no",
            "goods_domestic_status": "",
            "supervising_customs_office": "",
            "customs_warehouse_identifier": "",
            "ducr": "",
            "consignor_eori": "",
            "consignor_name": "DUMMY",
            "consignor_street_number": "DUMMY",
            "consignor_city": "DUMMY",
            "consignor_postcode": "BT1 1AA",
            "consignor_country": "GB",
            "consignee_eori": "",
            "consignee_name": "DUMMY",
            "consignee_street_number": "DUMMY",
            "consignee_city": "DUMMY",
            "consignee_postcode": "DUMMY",
            "consignee_country": "GB",
            "importer_eori": importer_eori_number,
            "exporter_eori": "",
            "exporter_name": "DUMMY",
            "exporter_street_number": "DUMMY",
            "exporter_city": "DUMMY",
            "exporter_postcode": "DUMMY",
            "exporter_country": "GB",
            "header_previous_document": [
                {
                    "op_type": "create",
                    "previous_document_class": "",
                    "previous_document_type": "",
                    "previous_document_ref": ""
                }
            ],
            "holder_of_authorisation": [
                {
                    "op_type": "create",
                    "auth_role_id": "",
                    "auth_type_code": ""
                }
            ]
        }

        response = requests.post(
            url="https://" + environment.DOMAIN +
                "/api/x_fhmrc_tss_api/v1/tss_api/consignments",
            auth=(environment.USER_NAME, environment.PASSWORD),
            json=example_data
        )

        return response.json()


    def read_declaration(self) -> None:
        environment = api_environments.TestEnvironment()

        response = requests.get(
            url="https://" + environment.DOMAIN
                + "/api/x_fhmrc_tss_api/v1/tss_api/headers",
            auth=(environment.USER_NAME, environment.PASSWORD),
            params="reference=ENS000000000405352"
                + "&fields=status,arrival_port,seal_number,route,carrier_eori"
        )

        return response.json()


    def cancel_declaration(self, ens_number: str) -> dict[str, str]:
        environment = api_environments.TestEnvironment()

        example_data = {
            "op_type": "cancel",
            "declaration_number": ens_number
        }

        response = requests.post(
            url="https://" + environment.DOMAIN
                + "/api/x_fhmrc_tss_api/v1/tss_api/headers",
            auth=(environment.USER_NAME, environment.PASSWORD),
            json=example_data
        )

        return response.json()


    def create_declaration(self) -> str:
        environment = api_environments.TestEnvironment()

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
            url="https://" + environment.DOMAIN +
                "/api/x_fhmrc_tss_api/v1/tss_api/headers?",
            auth=(environment.USER_NAME, environment.PASSWORD),
            json=example_data
        )

        return response.json()["result"]["reference"]
