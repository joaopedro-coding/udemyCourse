from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Define the function
def caesar(original_text, shift_amount, encode_or_decode):
    output_message = ""
    
    if encode_or_decode == "encode":
        shift_amount *= -1
    
    for letter in original_text:
        if letter in alphabet:
            text_index = alphabet.index(letter) - shift_amount
            text_index %= len(alphabet)
            output_message += alphabet[text_index]
        else:
            output_message += letter
    print(f"Here is the {encode_or_decode}d result: {output_message}")

# Implement the loop
should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    while direction not in ["encode", "decode"]:
        print("Please choose a valid option!")
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    # Repeat part 
    play_again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if play_again == "no" or play_again == "n":
        should_continue = False
        print("Goodbye!")
    elif play_again == "yes" or play_again == "y":
        continue
    else:
        print("You didn't choose a valid option. Thanks for using the program!")
        should_continue = False




