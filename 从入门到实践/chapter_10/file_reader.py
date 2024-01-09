from pathlib import Path
path = Path("pi_digits.txt")
# 读取这个文件的全部内容
contents = path.read_text()
# 将读取到的内容，以换行符分隔，转成一个列表。
lines = contents.splitlines()
# 访问文件中的各行
for line in lines:
    print(line)


