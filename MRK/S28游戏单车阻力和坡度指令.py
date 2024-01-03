from pathlib import Path


def bcc_checksum(data):
    """这是一个异或校验的函数"""

    bcc = 0
    for byte in data:
        bcc ^= byte
    return bcc


# 指令上限1~num
num = 34
# 存放指令的文件
file_path = Path("cmd_settings.txt")
# 清空文件内容
file_path.write_text("")

# 要进行校验的数据，字节2:阻力08/坡度09;字节3,4:坡度/阻力值
check_data = [0x06, 0x02, 0x09, 0x00, 0x00]

# 生成的指令范围1~num
level_lists = [level*10 for level in range(1, num)]

for lev in level_lists:
    if lev <= 250:
        check_data[3] = lev
        # 异或校验，生成checksum
        checksum = bcc_checksum(check_data)
        # 打印校验码
        # print(f"{int(lev/10)} BCC checksum: 0x{checksum:02X}")
        cmd_data = ''
        # 依次循环要校验的数据，转成16进制，组成1个新的字符串
        for i in check_data:
            cmd_data += f'{i:02X}'
        # 组成完整的指令
        set_resistance = f'{int(lev/10)} [AA{cmd_data}{checksum:02X}55]'
        print(set_resistance)
        # 以追加模式打开
        with file_path.open('a') as file_obj:
            file_obj.write(set_resistance + "\n")
    else:
        lev_16 = f"{lev:02X}"
        high_2 = '0' + lev_16[:1]
        low_2 = lev_16[1:]
        # 大小端，16进制转成十进制
        check_data[3], check_data[4] = int(low_2, 16), int(high_2, 16)

        # 异或校验，生成checksum
        checksum = bcc_checksum(check_data)
        # 打印校验码
        # check = f"{int(lev/10)} BCC checksum: 0x{checksum:02X}"
        # print(check)
        cmd_data = ''
        for i in check_data:
            cmd_data += f'{i:02X}'

        # 组成完整的指令
        set_resistance = f'{int(lev/10)} [AA{cmd_data}{checksum:02X}55]'
        print(set_resistance)
        # 以追加模式打开
        with file_path.open('a', encoding="utf-8") as file_obj:
            file_obj.write(set_resistance + "\n")
