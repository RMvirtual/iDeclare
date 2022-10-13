class Consignment:
    def __init__(self, ens_no: str, importer_eori_no: str):
        self.ens_no = ens_no
        self.importer_eori_no = importer_eori_no

    def dummy_consignment(self) -> dict[str, str]:
        return {
            "op_type": "create",
            "declaration_number": self.ens_no,
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
            "importer_eori": self.importer_eori_no,
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
