import os
from src.main.tss.api import TssApi
from src.main.file_system.api_environments import (
    ProductionEnvironment, TestEnvironment)


def main():
    should_exit = None
    api = TssApi(TestEnvironment())

    while not should_exit:
        user_input = input(
            "Please input an EORI number to check or type \"exit\": ")

        if user_input.lower() == "exit":
            should_exit = True

        elif api.is_eori_valid(user_input):
            print("EORI number " + user_input + " is valid.")

        else:
            print("EORI number " + user_input + " is INVALID.")

        input("\nPress any key to continue.")
        os.system("cls")

    os.system("cls")


if __name__ == '__main__':
    main()
