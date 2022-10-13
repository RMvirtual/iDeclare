from src.main.file_system.api_environments import ApiEnvironment


def tss_url(configuration: ApiEnvironment, resource: str) -> str:
    return (
            "https://"
            + configuration.domain
            + "/api/x_fhmrc_tss_api/v1/tss_api/"
            + configuration.resources[resource]
        )
