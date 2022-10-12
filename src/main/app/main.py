from src.main.tss import connection


def main():
    eori_candidate = input(
        "Please input an EORI number to check type \"exit\": ")

    if eori_candidate.lower() == "exit":
        exit()

    elif connection.is_eori_valid(eori_candidate):
        print("EORI number " + eori_candidate + " is valid.")
        input("\nPress any key to continue.")
        main()

    else:
        print("EORI number " + eori_candidate + " is INVALID.")
        main()


if __name__ == '__main__':
    main()
