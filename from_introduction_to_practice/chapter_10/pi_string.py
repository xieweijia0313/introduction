from pathlib import Path
path = Path('pi_digits.txt')
contents = path.read_text()
lines = contents.splitlines()
pi_string = ''
for line in lines:
    # 循环将各行加入pi_string
    pi_string += line.lstrip()

print(pi_string)
print(len(pi_string))
