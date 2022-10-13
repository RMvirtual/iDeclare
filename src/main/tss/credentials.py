import dataclasses
from src.main.file_system import api_files


@dataclasses.dataclass
class Credentials:
    user_name: str = ""
    test_environment_password: str = ""
    production_environment_password: str = ""
    graylaw_eori_number: str = ""


def user_credentials() -> Credentials:
    credentials = api_files.credentials()

    result = Credentials()
    result.user_name = credentials["user_name"]
    result.test_environment_password = credentials["test_environment_password"]

    result.production_environment_password = credentials[
        "production_environment_password"]

    result.graylaw_eori_number = credentials["EORI"]

    return result

