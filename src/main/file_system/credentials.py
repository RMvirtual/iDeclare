import dataclasses
import json
from src.main.file_system import runfiles


@dataclasses.dataclass
class Credentials:
    user_name: str = ""
    test_environment_password: str = ""
    production_environment_password: str = ""
    graylaw_eori_number: str = ""


def user_credentials() -> Credentials:
    credentials = _deserialise_credentials_file()

    result = Credentials()
    result.user_name = credentials["user_name"]
    result.test_environment_password = credentials["test_environment_password"]

    result.production_environment_password = credentials[
        "production_environment_password"]

    result.graylaw_eori_number = credentials["EORI"]

    return result


def _deserialise_credentials_file() -> dict[str, str]:
    credentials_file = runfiles.load_path("config/api/credentials.json")

    with open(credentials_file) as file_stream:
        return json.load(file_stream)
