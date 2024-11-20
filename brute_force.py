from itertools import product
import re

# Given encrypted message in hexadecimal form
encrypted_message_hex = "cf ac ef 32 57 4f 20 5e e1 fa bb 74 09 31 53 3f fe 98"
# Convert it to bytes
encrypted_message = bytes.fromhex(encrypted_message_hex)

# Define the expected flag format using a regular expression
flag_pattern = re.compile(rb"^SKY-\d{4}-[A-Z]{4}$")

# Define the brute-force function
def brute_force_xor_key():
    # Iterate over all possible 8-byte keys (each byte in the range 0x00 to 0xFF)
    for key_tuple in product(range(256), repeat=8):
        # Convert tuple to bytes for easier XOR operation
        xor_key = bytes(key_tuple)
        
        # Decrypt the message by XORing with the key (repeating the key as necessary)
        decrypted_message = bytes(
            encrypted_message[i] ^ xor_key[i % len(xor_key)] for i in range(len(encrypted_message))
        )
        
        # Attempt to match the decrypted message with the expected flag pattern
        # The flag is expected to be in the location starting after the version number and length fields
        flag = decrypted_message[5:]  # Skip version (1 byte) and length (4 bytes)
        if flag_pattern.match(flag):
            # Print the results if a match is found
            print("XOR Key (Hex):", xor_key.hex())
            print("Decrypted Flag:", flag.decode())
            return xor_key.hex(), flag.decode()  # Return values for further use if needed

    print("No valid flag found with brute-force approach.")
    return None, None

# Run the brute-force decryption
brute_force_xor_key()
