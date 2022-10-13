import os
from src.main.tss.api import TssApi
from src.main.file_system.api_environments import ProductionEnvironment


def main():
    eori_candidate = input(
        "Please input an EORI number to check or type \"exit\": ")

    if eori_candidate.lower() == "exit":
        os.system("cls")
        exit()

    elif TssApi(ProductionEnvironment()).is_eori_valid(eori_candidate):
        print("EORI number " + eori_candidate + " is valid.")
        input("\nPress any key to continue.")
        os.system("cls")
        main()

    else:
        print("EORI number " + eori_candidate + " is INVALID.")
        input("\nPress any key to continue.")
        os.system("cls")
        main()


if __name__ == '__main__':
    main()
