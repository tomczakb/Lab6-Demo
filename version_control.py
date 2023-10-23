
# B Tomczak


def print_menu():
    print("Menu\n"
          "-------------\n"
          "1. Encode\n"
          "2. Decode\n"
          "3. Quit\n\n")


def encoder(original):
    encoded = ""
    for i in original:
        if 0 <= int(i) <= 6:
            encoded += str(int(i) + 3)
        if 7 <= int(i) <= 9:
            encoded += str(int(i) - 7)
    return encoded


def decoder(encoded):
    # partner will create decoder function here
    pass


def main():
    while True:
        print_menu()
        option = int(input("Please enter an option: "))
        if option == 1:
            original = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!\n")
            encoded = encoder(original)
        if option == 2:
            decoded = decoder(encoded)
            print(f"The encoded password is {encoded}, and the original password is {decoded}"
                  " (error: will show 'None' until partner changes def decoder).")
        elif option == 3:
            return False


if __name__ == '__main__':
    main()