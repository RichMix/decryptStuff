# decryptStuff

CTF Decryption Toolkit

# Overview

The CTF Decryption Toolkit is a collection of tools and scripts designed to assist with decryption challenges commonly encountered in Capture The Flag (CTF) competitions. It supports various encryption algorithms, file formats, and encoded data types, enabling users to quickly analyze and decrypt data to solve challenges efficiently.

# Goal for repo features
Support for Common Encryption Algorithms:

- AES (128, 192, 256)
- DES, 3DES
- RSA
- XOR-based encryption
- Encoding Decoders:
- Base64, Base58, Base32
- Hexadecimal and Binary
- URL Encoding
- File Type Analysis:
- Extract metadata from files (e.g., exiftool)
- Identify file types (binwalk, file)
- Steganography Tools:
- Hidden data extraction from images and files.
- Brute-forcing Tools:
- Automated brute-force for simple ciphers and passwords.
- Modular and Extensible:
- Add custom scripts and algorithms as needed.

# Getting Started:
- Installation -- Clone the repository:

# bash
git clone https://github.com/username/ctf-decryption-toolkit.git
cd ctf-decryption-toolkit

# Dependencies
Install the required Python libraries:

# bash
pip install -r requirements.txt

# Additional tools somewhat required:

OpenSSL
binwalk
steghide
exiftool

# Install them on Linux-based systems:

# bash
sudo apt-get install openssl binwalk steghide libimage-exiftool-perl
Usage
Decrypting AES Files
Decrypt AES-encrypted files using the provided script:

# bash
python tools/aes_decrypt.py --file encrypted_file.enc --key YOUR_KEY --iv YOUR_IV
Decoding Base64 Strings
Decode a Base64 string:

# bash
python tools/base64_decode.py --data "SGVsbG8gV29ybGQ="
Extracting Hidden Data
Use binwalk to extract hidden files:

# bash
binwalk -e suspicious_file.img
Steganography
Extract hidden messages from image files:

# bash
steghide extract -sf hidden_image.jpg
Tool List
Python Scripts
aes_decrypt.py - AES decryption with custom key and IV.
xor_crack.py - Crack XOR-encrypted text or files.
rsa_decrypt.py - RSA decryption with private key.
base64_decode.py - Decode Base64-encoded strings.

# External Tools
openssl - Encryption and decryption for various algorithms.
binwalk - Analyze and extract data from binary files.
steghide - Extract hidden data in image/audio files.
exiftool - Analyze metadata in files.

# Contributing - We welcome contributions! If you have a tool or script to add, follow these steps:

Fork the repository.
Create a branch for your feature.
Add your tool to the appropriate directory (e.g., tools/).
Update README.md with usage instructions.
Submit a pull request.


# Feel free to adapt this README to suit your repository's structure and focus!
