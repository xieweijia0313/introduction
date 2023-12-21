from pathlib import Path


def bcc_checksum(data):
    """这是一个异或校验的函数"""

    bcc = 0
    for byte in data:
        bcc ^= byte
    return bcc


file_path = Path("set_resistance.txt")
data1 = [0x06, 0x02, 0x09, 0x0A, 0x00]  # 十六进制
checksum = bcc_checksum(data1)
print(f"BCC checksum: 0x{checksum:02X}")
