from src.main.tss.api.environment import environments
from src.main.app.controllers.cli import command_line_interface


def main():
    command_line_interface(environment=environments.TestEnvironment())


if __name__ == '__main__':
    main()
