def bcc_checksum(data):
    """这是一个异或校验的函数"""

    bcc = 0
    for byte in data:
        bcc ^= byte
    return bcc


data1 = [0x06, 0x02, 0x08, 0xF6, 0xFF]  # 十六进制
checksum = bcc_checksum(data1)
print(f"BCC checksum: 0x{checksum:02X}")
