import json
from src.main.file_system import runfiles


def deserialise_environments_file() -> dict[str, str]:
    return deserialise_json_file("config/api/environments.json")


def deserialise_draft_declarations_file() -> dict[str, str]:
    return deserialise_json_file("config/api/draft_declarations.json")


def deserialise_resource_url_links() -> dict[str, str]:
    with open(runfiles.load_path("config/api/resource_url_links.json")) as fs:
        return json.load(fs)


def deserialise_json_file(src_path: str) -> dict[str, str]:
    with open(runfiles.load_path(src_path)) as file_stream:
        return json.load(file_stream)
