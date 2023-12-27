from pathlib import Path


def bcc_checksum(data):
    """这是一个异或校验的函数"""

    bcc = 0
    for byte in data:
        bcc ^= byte
    return bcc


# 指令范围0~num
num = 45
# 存放指令的文件
file_path = Path("cmd_settings.txt")
# 清空文件内容
file_path.write_text("")

# 要进行校验的数据，字节3:速度;  字节4:坡度
check_data = [0x02, 0x53, 0x02, 0x00, 0x00, 0xFF, 0x03]

for lev in range(0, num):
    cmd_data = ""
    if lev >= 0:
        check_data[3] = 0x1E
        check_data[4] = lev
        # 异或校验，生成checksum
        checksum = bcc_checksum(check_data[1:-2])
        # 打印校验码
        print(f"{lev} BCC checksum: 0x{checksum:02X}")
        # 将校验码放到数据列表中
        check_data[-2] = checksum

        for i in check_data:
            cmd_data += f'{i:02X}'
        # 保存指令
        with file_path.open('a') as file_obj:
            file_obj.write(f'{lev} [{cmd_data}]\n')
        print(f'{lev} [{cmd_data}]')
