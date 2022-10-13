import dataclasses
import json
from src.main.file_system import runfiles
from src.main.file_system import credentials


def _deserialise_resource_url_links() -> dict[str, str]:
    with open(runfiles.load_path("config/api/resource_url_links.json")) as fs:
        return json.load(fs)


@dataclasses.dataclass
class ApiEnvironment:
    domain: str = ""
    user_name: str = ""
    password: str = ""
    eori_no: str = ""
    draft_declaration: str = ""
    resources: dict[str, str] = dataclasses.field(
        default_factory=_deserialise_resource_url_links)


class TestEnvironment(ApiEnvironment):
    def __init__(self):
        super().__init__()
        self.domain = _deserialise_environments_file()["TEST"]
        self.draft_declaration = _deserialise_draft_declarations_file()["TEST"]
        self._initialise_login_credentials()

    def _initialise_login_credentials(self):
        login_credentials = credentials.user_credentials()
        self.user_name = login_credentials.user_name
        self.password = login_credentials.test_environment_password
        self.eori_no = login_credentials.graylaw_eori_number


class ProductionEnvironment(ApiEnvironment):
    def __init__(self):
        super().__init__()
        self.domain = _deserialise_environments_file()["PROD"]
        self.draft_declaration = _deserialise_draft_declarations_file()["PROD"]
        self._initialise_login_credentials()

    def _initialise_login_credentials(self):
        login_credentials = credentials.user_credentials()
        self.user_name = login_credentials.user_name
        self.password = login_credentials.production_environment_password
        self.eori_no = login_credentials.graylaw_eori_number


def _deserialise_environments_file() -> dict[str, str]:
    return _deserialise_json_file("config/api/environments.json")


def _deserialise_draft_declarations_file() -> dict[str, str]:
    return _deserialise_json_file("config/api/draft_declarations.json")


def _deserialise_json_file(src_path: str) -> dict[str, str]:
    with open(runfiles.load_path(src_path)) as file_stream:
        return json.load(file_stream)
