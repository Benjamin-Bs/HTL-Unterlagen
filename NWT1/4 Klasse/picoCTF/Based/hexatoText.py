def hex_to_text(hex_str):
    try:
        # Remove any leading "0x" if present
        hex_str = hex_str.replace("0x", "")

        # Ensure the hexadecimal string has an even length
        hex_str = hex_str.zfill((len(hex_str) + 1) // 2 * 2)

        # Convert hexadecimal string to bytes
        byte_data = bytes.fromhex(hex_str)

        # Decode bytes to text using ASCII encoding
        text_data = byte_data.decode('ascii')

        return text_data
    except ValueError:
        print("Invalid hexadecimal string. Please provide a valid hexadecimal input.")
        return None


# Get hexadecimal input from the user
hex_input = input("Enter a hexadecimal string: ")

# Call the function with user input
text_result = hex_to_text(hex_input)

# Display the result if it's not None
if text_result is not None:
    print("Hexadecimal Input:", hex_input)
    print("Text Output:", text_result)
