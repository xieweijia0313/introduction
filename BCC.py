from pathlib import Path

def bcc_checksum(data):
    """这是一个异或校验的函数"""

    bcc = 0
    for byte in data:
        bcc ^= byte
    return bcc


file_path = Path("set_resistance.txt")
data_1 = [0x06, 0x02, 0x09, 0x00, 0x00]

checksum = bcc_checksum(data_1)
# print(f"BCC checksum: 0x{checksum:02X}")
# https://blog.51cto.com/u_16175438/6865399
print(f"BCC checksum: 0x{260:02X}")
# 存放指令
set_resistance = ''

levels = [level*10 for level in range(1, 34)]
for lev in levels:
    if lev <= 250:
        data_1[3] = lev
        # 异或校验，生成checksum
        checksum = bcc_checksum(data_1)
        # 打印校验码
        # print(f"{int(lev/10)} BCC checksum: 0x{checksum:02X}")
        # 组成完整的指令
        set_resistance = f'{int(lev/10)} 06020900{lev:02X}{checksum:02X}'
        # 以追加模式打开
        with file_path.open('a') as file_obj:
            file_obj.write(set_resistance + "\n")
        # print(set_resistance)
    else:
        print(f"BCC checksum: 0x{lev:02X}")

