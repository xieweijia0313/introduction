from pathlib import Path

file_path = Path("S28_data.txt")
contents = file_path.read_text().rstrip().split('-')
print(contents)

bit_lists = [f'bit_{i}' for i in range(0, 41)]
bit_datas = contents
bit_dicts = {}
i = 0
for bit_dict in bit_lists:
    bit_dicts[bit_dict] = bit_datas[i]
    i += 1
print(bit_dicts)

print(bit_dicts['bit_0'])
