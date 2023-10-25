
# B Tomczak
# 2nd commit: changed whitespace

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
    # Mariyah: Updated decoder function based on partner's encoder function
    decoded = ''
    for item in encoded:
        if int(item) >= 3:
            new_item = int(item) - 3
            decoded += str(new_item)
        elif int(item) <= 2:
            new_item = 0
            for i in range(int(item) + 1):
                new_item = int(i) + 7
            decoded += str(new_item)
    return decoded


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
            print(f"The encoded password is {encoded}, and the original password is {decoded}")
        elif option == 3:
            return False


if __name__ == '__main__':
    main()
