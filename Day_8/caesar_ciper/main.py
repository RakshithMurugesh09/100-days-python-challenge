from asii_art import log
# List of lowercase alphabet letters
ALPHABET = (
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
)

print(log)
def caesar_cipher(message: str, shift: int) -> str:
    """
    Encrypts or decrypts a message using Caesar cipher with a given shift.

    Args:
        message (str): The Input message to encrypt or decrypt.
        shift (int): The shift amount (positive for encryption, negative for decryption).

    Returns:
        str: The resulting encrypted or decrypted message.
    """
    result = ""
    for letter in message:
        if letter in ALPHABET:
            # Find the original position of the letter in the alphabet
            original_position = ALPHABET.index(letter)
            # Calculate new shifted position with wrapping using modulo
            shifted_position = (original_position + shift) % 26
            # Get the shifted letter
            new_letter = ALPHABET[shifted_position]
            result += new_letter
        else:
            # Non-alphabet characters are added unchanged
            result += letter
    return result


def main():
    """
    Main function to take user Input for encryption or decryption and display the result.
    """
    # Prompt user for mode selection
    mode = input("Type 'e' to Encrypt, type 'd' to Decrypt: ").strip().lower()
    # Prompt user for message Input
    user_message = input("Type a message: ").lower()
    # Prompt user for shift value and convert to int
    shift_value = int(input("Type the Shift number: "))

    # Determine whether to encrypt or decrypt based on user choice
    if mode == "d":
        # For decryption, invert the shift
        shift_value *= -1
        result_message = caesar_cipher(message=user_message, shift=shift_value)
        print(f"Decrypted message: {result_message}")
    elif mode == "e":
        result_message = caesar_cipher(message=user_message, shift=shift_value)
        print(f"Encrypted message: {result_message}")
    else:
        print("Invalid option! Please type 'e' to Encrypt or 'd' to Decrypt.")


# Call the main function to start the program
while True:
    main()
    need_to_continue = (input("\nDo you needed to rerun? Y/N:")).lower()
    if need_to_continue == "n":
        print("\nGood Bye!")
        break

