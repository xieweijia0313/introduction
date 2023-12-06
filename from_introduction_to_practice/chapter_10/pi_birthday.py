from pathlib import Path
path = Path('pi_million_digits.txt')
contents = path.read_text()
lines = contents.splitlines()
pi_string = ''
for line in lines:
    # 循环将各行加入pi_string
    pi_string += line.lstrip()
print(pi_string[:52])

# birthday = input("Enter your birthday, in the form mmddyy: ")
# if birthday in pi_string:
#     print("Your birthday appears in the first million digits of pi!")
# else:
#     print("Your birthday does not appear in the first million digits ofpi.")

message = "I really like dogs."
# 将dog替换为cat
message = message.replace('dog', 'cat')
print(message)
