def bcc_checksum(data):
    bcc = 0
    for byte in data:
        bcc ^= byte
    return bcc


data = [0x01, 0x02, 0x03, 0x04, 0x05]
checksum = bcc_checksum(data)
print(f"BCC checksum: 0x{checksum:02x}")

# https://blog.51cto.com/u_16175438/6865399
