import dataclasses
import re
from src.main.tss.api.environment import credentials
from src.main.file_system import api_files


@dataclasses.dataclass
class ApiEnvironment:
    environment_type: str = ""
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

    def update_draft(self, new_ens: str):
        if re.fullmatch(r"ENS\d{15}", new_ens):
            api_files.update_draft_declaration(self.environment_type, new_ens)
            self.draft_declaration = new_ens


class TestEnvironment(ApiEnvironment):
    def __init__(self):
        super().__init__()
        self.environment_type = "TEST"
        self.domain = api_files.environments()[self.environment_type]

        self.draft_declaration = api_files.draft_declarations()[
            self.environment_type]

        self._initialise_login_credentials()

    def _initialise_login_credentials(self):
        login_credentials = credentials.user_credentials()
        self.user_name = login_credentials.user_name
        self.password = login_credentials.test_environment_password
        self.eori_no = login_credentials.graylaw_eori_number


class ProductionEnvironment(ApiEnvironment):
    def __init__(self):
        super().__init__()
        self.environment_type = "PROD"
        self.domain = api_files.environments()[self.environment_type]

        self.draft_declaration = api_files.draft_declarations()[
            self.environment_type]

        self._initialise_login_credentials()

    def _initialise_login_credentials(self):
        login_credentials = credentials.user_credentials()
        self.user_name = login_credentials.user_name
        self.password = login_credentials.production_environment_password
        self.eori_no = login_credentials.graylaw_eori_number

