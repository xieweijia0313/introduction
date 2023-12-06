import requests


# 执行 API 调用并查看响应
# URL 的主要部分
url = "https://api.github.com/search/repositories"
# 查询字符串
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
# status_code状态码；200请求成功
# print(f"Status code: {r.status_code}")
"""运行结果
Status code: 200
"""

# 使用 json() 方法将这些信息转换为一个 Python 字典
response_dict = r.json()

# 处理结果
# print(response_dict.keys())
"""运行结果
dict_keys(['total_count', 'incomplete_results', 'items'])
"""

print(f"Total repositories: {response_dict['total_count']}")
print(f"Complete results: {not response_dict['incomplete_results']}")
"""运行结果
Total repositories: 427  //指出API 调用返回了多少个 Python 仓库
Complete results: True  //GitHub 是否有足够的时间处理完这个查询。打印与之相反的值：如果为 True，就表明收到了完整的结果集。

"""

# 探索有关仓库的信息
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")
# 研究第一个仓库
repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(key)
