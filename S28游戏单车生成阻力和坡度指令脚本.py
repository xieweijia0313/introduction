from pathlib import Path


def bcc_checksum(data):
    """这是一个异或校验的函数"""

    bcc = 0
    for byte in data:
        bcc ^= byte
    return bcc


file_path = Path("set_resistance.txt")
# 字节2，09阻力08坡度； 字节3,4，坡度/阻力值
data_1 = [0x06, 0x02, 0x09, 0x00, 0x00]
# data_1字符串格式
data_2 = ''

# checksum = bcc_checksum(data_1)
# print(f"BCC checksum: 0x{checksum:02X}")

levels = [level*10 for level in range(1, 34)]
for lev in levels:
    if lev <= 250:
        data_1[3] = lev

        # 异或校验，生成checksum
        checksum = bcc_checksum(data_1)
        # 打印校验码
        print(f"{int(lev/10)} BCC checksum: 0x{checksum:02X}")

        data_2 = ''
        for i in data_1:
            data_2 += f'{i:02X}'
        # 将校验码组成完整的指令
        set_resistance = f'{int(lev/10)} AA{data_2}{checksum:02X}55'
        # 以追加模式打开
        with file_path.open('a') as file_obj:
            file_obj.write(set_resistance + "\n")
    else:
        lev_16 = f"{lev:02X}"
        high_2 = '0' + lev_16[:1]
        low_2 = lev_16[1:]
        data_1[3] = int(low_2, 16)  # 16进制转成十进制
        data_1[4] = int(high_2, 16)

        # # 异或校验，生成checksum
        checksum = bcc_checksum(data_1)
        # # 打印校验码
        check = f"{int(lev/10)} BCC checksum: 0x{checksum:02X}"
        print(check)

        data_2 = ''
        for i in data_1:
            data_2 += f'{i:02X}'

        # 将校验码组成完整的指令
        set_resistance = f'{int(lev/10)} AA{data_2}{checksum:02X}55'
        # 以追加模式打开
        with file_path.open('a') as file_obj:
            file_obj.write(set_resistance + "\n")
