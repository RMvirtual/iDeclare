import requests
from src.main.file_system import credentials, api_environments


def read_consignment() -> None:
    login = credentials.user_credentials()
    environment = api_environments.environments().TEST

    response = requests.get(
        url="https://" + environment
            + "/api/x_fhmrc_tss_api/v1/tss_api/consignments",
        auth=(login.user_name, login.password),
        params="reference=DEC000000001010576"
            + "&fields=importer_eori"
    )

    print(response.text)


def create_consignment() -> None:
    login = credentials.user_credentials()
    environment = api_environments.environments().TEST

    example_data = {
        "op_type": "create",
        "declaration_number": "ENS000000000405352",
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
        "importer_eori": login.graylaw_eori_number,
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
        url="https://" + environment +
            "/api/x_fhmrc_tss_api/v1/tss_api/consignments",
        auth=(login.user_name, login.password),
        json=example_data
    )

    print(response.json())


def read_declaration() -> None:
    login = credentials.user_credentials()
    environment = api_environments.environments().TEST

    response = requests.get(
        url="https://" + environment
            + "/api/x_fhmrc_tss_api/v1/tss_api/headers",
        auth=(login.user_name, login.password),
        params="reference=ENS000000000405352"
            + "&fields=status,arrival_port,seal_number,route,carrier_eori"
    )

    print(response.text)


def create_declaration() -> str:
    login = credentials.user_credentials()
    environment = api_environments.environments().TEST

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
        url="https://" + environment +
            "/api/x_fhmrc_tss_api/v1/tss_api/headers?",
        auth=(login.user_name, login.password),
        json=example_data
    )

    print(response.text)
