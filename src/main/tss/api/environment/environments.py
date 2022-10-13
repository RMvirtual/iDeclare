import dataclasses
from src.main.tss.api.environment import credentials
from src.main.file_system import api_files


@dataclasses.dataclass
class ApiEnvironment:
    domain: str = ""
    user_name: str = ""
    password: str = ""
    eori_no: str = ""
    draft_declaration: str = ""
    resources: dict[str, str] = dataclasses.field(
        default_factory=api_files.resource_url_links)

    @property
    def authentication(self) -> tuple[str, str]:
        return self.user_name, self.password


class TestEnvironment(ApiEnvironment):
    def __init__(self):
        super().__init__()
        self.domain = api_files.environments()["TEST"]
        self.draft_declaration = api_files.draft_declarations()["TEST"]
        self._initialise_login_credentials()

    def _initialise_login_credentials(self):
        login_credentials = credentials.user_credentials()
        self.user_name = login_credentials.user_name
        self.password = login_credentials.test_environment_password
        self.eori_no = login_credentials.graylaw_eori_number


class ProductionEnvironment(ApiEnvironment):
    def __init__(self):
        super().__init__()
        self.domain = api_files.environments()["PROD"]
        self.draft_declaration = api_files.draft_declarations()["PROD"]
        self._initialise_login_credentials()

    def _initialise_login_credentials(self):
        login_credentials = credentials.user_credentials()
        self.user_name = login_credentials.user_name
        self.password = login_credentials.production_environment_password
        self.eori_no = login_credentials.graylaw_eori_number

