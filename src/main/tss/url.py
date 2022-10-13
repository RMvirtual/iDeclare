from src.main.tss.environments import ApiEnvironment


def tss_url(configuration: ApiEnvironment, resource: str) -> str:
    return "https://" + "/".join((
        configuration.domain,
        "api/x_fhmrc_tss_api/v1/tss_api",
        configuration.resources[resource]
    ))

