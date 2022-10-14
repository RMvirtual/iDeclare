from src.main.tss.api.environment import environments
from src.main.app.controllers.gui import TssGuiController


def main():
    controller = TssGuiController(environments.TestEnvironment())
    controller.run()


if __name__ == '__main__':
    main()
