from pathlib import Path


def bcc_checksum(data):
    """这是一个异或校验的函数"""

    bcc = 0
    for byte in data:
        bcc ^= byte
    return bcc


file_path = Path("set_resistance.txt")
data_1 = [0x06, 0x02, 0x09, 0x00, 0x00]


# checksum = bcc_checksum(data_1)
# print(f"BCC checksum: 0x{checksum:02X}")

levels = [level*10 for level in range(1, 34)]
for lev in levels:
    if lev <= 250:
        data_1[3] = lev
        # 异或校验，生成checksum
        checksum = bcc_checksum(data_1)
        # 打印校验码
        # print(f"{int(lev/10)} BCC checksum: 0x{checksum:02X}")
        # 将校验码组成完整的指令
        set_resistance = f'{int(lev/10)} AA060209{lev:02X}00{checksum:02X}55'
        # 以追加模式打开
        with file_path.open('a') as file_obj:
            file_obj.write(set_resistance + "\n")
    else:
        # print(lev)
        # print(f"{lev:02X}")
        lev_16 = f"{lev:02X}"
        high_2 = '0' + lev_16[:1]
        low_2 = lev_16[1:]
        # print(low_2, high_2)
        data_1[3] = int(low_2, 16)  # 16进制转成十进制
        data_1[4] = int(high_2, 16)
        # print(data_1)

        # 异或校验，生成checksum
        checksum = bcc_checksum(data_1)
        # 打印校验码
        print(f"{int(lev/10)} BCC checksum: 0x{checksum:02X}")

        # 将校验码组成完整的指令
        set_resistance = f'{int(lev/10)} AA060209{low_2}{high_2}{checksum:02X}55'
        # 以追加模式打开
        with file_path.open('a') as file_obj:
            file_obj.write(set_resistance + "\n")
