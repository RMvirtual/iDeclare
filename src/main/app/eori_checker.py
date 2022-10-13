import os
from src.main.tss.api import TssApi
from src.main.file_system.api_environments import ApiEnvironment


def eori_checker(environment: ApiEnvironment):
    api = TssApi(environment)
    should_exit = None

    while not should_exit:
        user_input = input(
            "Please input an EORI number to check or type \"exit\": ")

        if user_input.lower() == "exit":
            should_exit = True
            print("Exiting...")

        elif api.is_eori_valid(user_input):
            print("EORI number " + user_input + " is valid.")

        else:
            print("EORI number " + user_input + " is INVALID.")

        input("\nPress any key to continue.")
        os.system("cls")
