from pathlib import Path

path = Path('alice.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
else:
    # 以空白为分隔符将字符串分拆，并返回一个列表
    words = contents.split()
    # 计算文件大致包含多少个单词（列表的长度）
    num_words = len(words)
    print(f"The file {path} has about {num_words} words.")
