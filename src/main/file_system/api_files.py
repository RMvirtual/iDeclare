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


def update_draft_declaration(environment_type: str, new_ens_no: str) -> None:
    contents = draft_declarations()
    contents[environment_type] = new_ens_no

    serialise_to_json_file("config/api/draft_declarations.json", contents)


def deserialise_json_file(src_path: str) -> dict[str, str]:
    with open(runfiles.load_path(src_path)) as file_stream:
        return json.load(file_stream)


def serialise_to_json_file(src_path: str, values: dict[str, str]) -> None:
    with open(runfiles.load_path(src_path), "w") as file_stream:
        json.dump(values, file_stream, indent=4, sort_keys=True)
