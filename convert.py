# Let's perform the conversions for each question

# Q1: Octal to ASCII conversion
q1_octal = ['071', '144', '157', '147', '154', '157', '166', '145', '162', '066']
q1_text = ''.join(chr(int(oct_val, 8)) for oct_val in q1_octal)

# Q2: Base64 to ASCII conversion
import base64
q2_base64 = "NjMgNzkgNjIgNjUgNzIgNjcgNjEgNzQgNjUgMzY="
q2_text = base64.b64decode(q2_base64).decode('utf-8')

# Q3: Hexadecimal to ASCII conversion
q3_hex = ["31", "31", "36", "20", "31", "32", "37", "20", "31", "34", "34", "20", "31", "36", "36", "20",
          "31", "34", "32", "20", "31", "30", "37", "20", "31", "32", "32", "20", "31", "35", "34", "20",
          "31", "34", "32", "20", "31", "35", "35", "20", "31", "34", "34", "20", "31", "36", "36", "20",
          "31", "33", "31", "20", "31", "33", "30", "20", "31", "32", "31", "20", "30", "36", "30"]
q3_text = ''.join(chr(int(hex_val, 16)) for hex_val in q3_hex)

# Q4: Binary to ASCII conversion
q4_binary = ["00110001", "00110001", "00110101", "00100000", "00110000", "00110110", "00110011", "00100000",
             "00110001", "00110001", "00110010", "00100000", "00110001", "00110110", "00110000", "00100000",
             "00110001", "00110100", "00110100", "00100000", "00110001", "00110101", "00110110", "00100000",
             "00110001", "00110101", "00110100", "00100000", "00110001", "00110101", "00110110", "00100000",
             "00110001", "00110100", "00110001", "00100000", "00110001", "00110101", "00110110", "00100000",
             "00110001", "00110011", "00110010", "00100000", "00110001", "00110101", "00110000", "00100000",
             "00110001", "00110001", "00110110", "00100000", "00110001", "00110010", "00110001", "00100000",
             "00110000", "00110111", "00110101", "00100000", "00110000", "00110111", "00110101"]
q4_text = ''.join(chr(int(bin_val, 2)) for bin_val in q4_binary)

q1_text, q2_text, q3_text, q4_text

('9doglover6',
 '63 79 62 65 72 67 61 74 65 36',
 '116 127 144 166 142 107 122 154 142 155 144 166 131 130 121 060',
 '115 063 112 160 144 156 154 156 141 156 132 150 116 121 075 075')

# Further conversion of ASCII code sequences for Q2, Q3, and Q4

# Convert ASCII codes to characters for Q2
q2_ascii_sequence = [63, 79, 62, 65, 72, 67, 61, 74, 65, 36]
q2_text_final = ''.join(chr(code) for code in q2_ascii_sequence)

# Convert ASCII codes to characters for Q3
q3_ascii_sequence = [116, 127, 144, 166, 142, 107, 122, 154, 142, 155, 144, 166, 131, 130, 121, 60]
q3_text_final = ''.join(chr(code) for code in q3_ascii_sequence)

# Convert ASCII codes to characters for Q4
q4_ascii_sequence = [115, 63, 112, 160, 144, 156, 154, 156, 141, 156, 132, 150, 116, 121, 75, 75]
q4_text_final = ''.join(chr(code) for code in q4_ascii_sequence)

q2_text_final, q3_text_final, q4_text_final
# Result
('?O>AHC=JA$',
 't\x7f\x90¦\x8ekz\x9a\x8e\x9b\x90¦\x83\x82y<',
 's?p\xa0\x90\x9c\x9a\x9c\x8d\x9c\x84\x96tyKK')

# After decoding, here are the final results:

# Q1 Answer: 9doglover6
# Q2 Answer: ?O>AHC=JA$
# Q3 Answer: The ASCII characters appear garbled: t\x7f\x90¦\x8ekz\x9a\x8e\x9b\x90¦\x83\x82y<
# Q4 Answer: The ASCII characters also appear garbled: s?p\xa0\x90\x9c\x9a\x9c\x8d\x9c\x84\x96tyKK
# It appears that Q3 and Q4 may not represent readable ASCII text, or they might use non-standard encoding. The decoded sequences for Q3 and Q4 seem to contain control or extended characters, suggesting that they might not represent common passwords from a wordlist.

# For a typical rockyou password, you might want to try a different approach or revisit the encoding assumptions. Let me know if you'd like further assistance with these specific parts! ​​