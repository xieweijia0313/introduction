from pathlib import Path


def count_words(filename):
    """计算一个文件应该大致包含多少个单词"""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        # 计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")


filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    path = Path(filename)
    count_words(path)

line = "Row, row, row your boat"
message = line.lower().count('str')
print(message)




while True:
    message1 = input('请输入第一个数字')
    if message1 == "n":
        break
    message2 = input('请输入第二个数字')
    if message2 == "n":
        break
    try:
        message3 = int(message1) / int(message2)

    except ValueError:
        print("The input is not a number. Please try again")

    except ZeroDivisionError:
        print("division by zero")

    else:
        print(message3)
