from pathlib import Path
import json

numbers = [2, 3, 5, 7, 11, 13]
path = Path('numbers.json')
# 将一个文本文件转成JSON格式存入文件中
contents = json.dumps(numbers)
path.write_text(contents)

# 读取JSON格式的文本文件内容
contents = path.read_text()
# 将一个JSON格式的字符串作为参数，并返回一个Python对象
numbers = json.loads(contents)
print(numbers)

