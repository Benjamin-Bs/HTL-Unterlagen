import keyboard


def binary_to_text(binary_str):
    # Remove spaces from the binary string
    binary_str = binary_str.replace(" ", "")

    # Ensure the binary string has a multiple of 8 characters
    binary_str = binary_str.zfill((len(binary_str) + 7) // 8 * 8)

    # Convert binary string to bytes
    byte_data = int(binary_str, 2).to_bytes(len(binary_str) // 8, byteorder='big')

    # Decode bytes to text using ASCII encoding
    text_data = byte_data.decode('ascii')

    return text_data


# Get binary input from the user
binary_input = ""

print("Enter a binary string (Press Esc to finish):")

while True:
    event = keyboard.read_event(suppress=True)

    if event.event_type == keyboard.KEY_DOWN:
        char = event.name

        if char == 'esc':
            break
        elif char in ['0', '1']:
            binary_input += char
        elif char == 'backspace':
            binary_input = binary_input[:-1]

        # Call the function with the current user input
        text_result = binary_to_text(binary_input)

        # Display the current input and result
        print("Binary Input:", binary_input, end='\r')  # '\r' is used to overwrite the line

        if text_result:
            print("Text Output:", text_result, end='\r')

# Display the final result
print("\nFinal Binary Input:", binary_input)
print("Final Text Output:", text_result)
