import dataclasses
import json
from src.main.file_system import runfiles
from src.main.file_system import credentials


@dataclasses.dataclass
class ApiEnvironment:
    domain: str = ""
    user_name: str = ""
    password: str = ""
    eori_no: str = ""
    draft_declaration: str = ""


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
    with open(runfiles.load_path("config/api/environments.json")) as stream:
        return json.load(stream)


def _deserialise_draft_declarations_file() -> dict[str, str]:
    with open(runfiles.load_path("config/api/draft_declarations.json")) as fs:
        return json.load(fs)
