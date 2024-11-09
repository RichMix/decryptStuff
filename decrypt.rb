require 'openssl'
require 'base64'

# Provided Base64 encoded target key
key = "WSYZmB+qrU0ZR/bnFXKNwA=="
# Decode the key from Base64
decoded_key = Base64.decode64(key)

# Set up AES decryption with the hardcoded key
cipher = OpenSSL::Cipher::AES.new(128, :ECB)
cipher.decrypt
cipher.key = 'BaconEggsAnToast'

# Decrypt the decoded key
decrypted_data = cipher.update(decoded_key) + cipher.final

# XOR each byte with 0xf4 to retrieve the original passcode
passcode = decrypted_data.bytes.map { |byte| byte ^ 0xf4 }.pack('c*')

puts "The passcode is: #{passcode}"
