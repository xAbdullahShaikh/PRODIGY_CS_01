class ceaser_cipher:
    def __init__(self, shift_value):
        self.shift_value = shift_value
        self.cipher_text = ""
        self.plain_text = ""

    def c_s_encryption(self):
        self.cipher_text = ""
        self.plain_text = ""

        self.plain_text = input("Enter the plaintext: ")
        for x in self.plain_text:
            shifted_ascii_code = ord(x) + self.shift_value
            if x.isalpha():
                if x.islower() and shifted_ascii_code > ord('z'):
                    shifted_ascii_code -= 26
                elif x.isupper() and shifted_ascii_code > ord('Z'):
                    shifted_ascii_code -= 26

                self.cipher_text += chr(shifted_ascii_code)
            else:
                self.cipher_text += x

        return self.cipher_text

    def c_s_decryption(self):
        self.plain_text = ""
        self.cipher_text = input("Enter the ciphertext: ")

        for x in self.cipher_text:
            if x.isalpha():
                shifted_ascii_code = ord(x) - self.shift_value
                if x.islower() and shifted_ascii_code < ord('a'):
                    shifted_ascii_code += 26
                elif x.isupper() and shifted_ascii_code < ord('A'):
                    shifted_ascii_code += 26

                self.plain_text += chr(shifted_ascii_code)
            else:
                self.plain_text += x

        return self.plain_text


def main():
    print("Name: Abdullah_Shaikh\nRoll_no:21k4783")

    shift_value = int(input("Please provide the shift value:"))
    e_obj = ceaser_cipher(shift_value)

    while True:
        print("____________________________________________________________________\n")
        print("select 1 for encryption\nselect 2 for decryption\nselect 3 to exit")
        print("____________________________________________________________________\n")
        user_input = int(input("Enter choice:"))

        if user_input == 1:
            cipher = e_obj.c_s_encryption()
            print(f"cipher text is :{cipher}")

        elif user_input == 2:
            plaintext = e_obj.c_s_decryption()
            print(f"plain text is :{plaintext}")

        elif user_input == 3:
            exit(1)

        else:
            print("Invalid option. Program exiting -----")


if __name__ == "__main__":
    main()
