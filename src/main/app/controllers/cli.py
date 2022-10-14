import os
from src.main.tss.api.model import TssApi
from src.main.tss.api.environment.environments import ApiEnvironment


def command_line_interface(environment: ApiEnvironment):
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
