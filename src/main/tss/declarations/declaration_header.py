import datetime


class DeclarationHeader:
    def __init__(self):
        pass

    def dummy_data(self) -> dict[str, str]:
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
