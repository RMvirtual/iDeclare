from src.main.file_system import api_environments
from src.main.app.eori_checker import eori_checker


def main():
    eori_checker(environment=api_environments.TestEnvironment())


if __name__ == '__main__':
    main()
