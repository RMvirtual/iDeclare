import json
from src.main.file_system import runfiles


def environments() -> dict[str, str]:
    return deserialise_json_file("config/api/environments.json")


def draft_declarations() -> dict[str, str]:
    return deserialise_json_file("config/api/draft_declarations.json")


def resource_url_links() -> dict[str, str]:
    return deserialise_json_file("config/api/resource_url_links.json")


def credentials() -> dict[str, str]:
    return deserialise_json_file("config/api/credentials.json")


def deserialise_json_file(src_path: str) -> dict[str, str]:
    with open(runfiles.load_path(src_path)) as file_stream:
        return json.load(file_stream)
