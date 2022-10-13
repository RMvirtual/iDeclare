from src.main.tss.api.environment import environments
from src.main.app.eori_checker import eori_checker


def main():
    eori_checker(environment=environments.TestEnvironment())


if __name__ == '__main__':
    main()
