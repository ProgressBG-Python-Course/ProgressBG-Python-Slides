# import base64

# # base64 needs binary data:
# data_bytes = b'abracadabra'

# # encoding binary data to Base64
# data_base64 = base64.b64encode(data_bytes)
# print(f'data_base64: {data_base64}')

# # decoding Base64-encoded data back to binary
# decoded_data_bytes = base64.b64decode(data_base64)
# print("Decoded:", decoded_data_bytes)

# # data_base64: b'YWJyYWNhZGFicmE='
# # Decoded: b'abracadabra'


string_a = "A"
bytes_a = string_a.encode("utf-8")

print(f"String: {string_a}, Bytes: {bytes_a}")
print(string_a == bytes_a)
