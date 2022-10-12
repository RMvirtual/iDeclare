import dataclasses
import json
from src.main.file_system import runfiles


@dataclasses.dataclass
class Credentials:
    user_name: str = ""
    password: str = ""


def user_credentials() -> Credentials:
    credentials = _deserialise_credentials_file()

    result = Credentials()
    result.user_name = credentials["user_name"]
    result.password = credentials["password"]

    return result


def _deserialise_credentials_file() -> dict[str, str]:
    credentials_file = runfiles.load_path("config/api/test_credentials.json")

    with open(credentials_file) as file_stream:
        return json.load(file_stream)
