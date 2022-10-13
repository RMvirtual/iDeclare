import requests
from src.main.tss.environments import ApiEnvironment
from src.main.tss.url import tss_url


class Consignment:
    def __init__(self, configuration: ApiEnvironment):
        self._configuration = configuration
        self._url = tss_url(self._configuration, "consignment")

    def create_consignment(
            self, ens_no: str, importer_eori_no: str) -> dict[str, str]:
        example_data = {
            "op_type": "create",
            "declaration_number": ens_no,
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
            "importer_eori": importer_eori_no,
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
            url=self._url,
            auth=self._configuration.authentication,
            json=example_data
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

    def cancel_consignment(self, dec_number: str) -> dict[str, str]:
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
