import requests
from src.main.file_system import credentials, api_environments


def authenticate() -> str:
    login = credentials.user_credentials()
    environment = api_environments.environments().TEST

    example_data = """{
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
    }"""

    response = requests.post(
        url="https://" + environment +
            "/api/x_fhmrc_tss_api/v1/tss_api/headers?",
        auth=(login.user_name, login.password),
        data=example_data
    )

    print(response.text)
