import dataclasses
import json
from src.main.file_system import runfiles


@dataclasses.dataclass
class ApiEnvironments:
    TEST: str = ""
    PROD: str = ""


def environments() -> ApiEnvironments:
    credentials = _deserialise_environments_file()

    result = ApiEnvironments()
    result.TEST = credentials["TEST"]
    result.PROD = credentials["PROD"]

    return result


def _deserialise_environments_file() -> dict[str, str]:
    environments_file = runfiles.load_path("config/api/environments.json")

    with open(environments_file) as file_stream:
        return json.load(file_stream)
