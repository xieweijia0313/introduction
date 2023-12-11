import requests
import plotly.express as px

# 执行 API 调用并查看响应
# URL 的主要部分
# https://api.github.com GitHub的API地址
# search/repositories 让API搜索GitHub上的所有仓库
# ? 指出需要传递一个参数
# q= 指定查询
# language:python 获取语言为python的仓库
# +sort:stars 指定将项目按星级排序
# stars:>10000
url = "https://api.github.com/search/repositories"
# 查询字符串
url += "?q=language:python+sort:stars+stars:>10000"
# headers是http请求的请求头，给服务器发送额外的信息。
# Accept告诉服务器我们作为客户端想要接受的数据类型。
headers = {"Accept": "application/vnd.github.v3+json"}
# 使用requests的get方法获取信息
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")
"""运行结果。
Status code: 200  # 状态码，200请求成功。4开头客户端错误，5错误服务端错误

--------------------------------------------------"""

# 使用json()方法将这些信息转换为一个 Python 字典
response_dict = r.json()
# 打印字典的所有键
print(response_dict.keys())
"""运行结果
dict_keys(['total_count', 'incomplete_results', 'items'])
total_count //python项目数量。
incomplete_results //GitHub是否处理完查询，True 未完成；False 完成。
items //python项目的详细信息。
"""

print(f"Total repositories: {response_dict['total_count']}")
print(f"Complete results: {not response_dict['incomplete_results']}")
"""运行结果
Total repositories: 427  //指出API调用返回了多少个Python仓库。
Complete results: True  //GitHub是否有足够的时间处理完这个查询。打印与之相反的值：如果为 True，就表明收到了完整的结果集。

--------------------------------------------------"""

# 探索有关仓库的信息。
# 与item关联的值是一个列表，其中包含很多字典，而每一个字典都吧包含有关一个python仓库的信息。
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")  # 仓库数量及列表的长度
# 研究第一个仓库
repo_dict = repo_dicts[0]  # 探索列表中的第一个字典
print(f"\nKeys: {len(repo_dict)}")  # 第一个仓库信息量及字典的长度
#  第一个仓库的所有key，看看其中包含哪些信息。
# for key in sorted(repo_dict.keys()):
#     print(key)

"""运行结果
Repositories returned: 30  //第一页的仓库数量

Keys: 80  //第一个仓库信息
allow_forking  //其中包含哪些信息
archive_url

"""
# 探索其中包含的信息
print(f"\nSelected(选择) information（信息） about first repository（存储库）:")
for repo_dict in repo_dicts:
    print(f"Name(项目名称): {repo_dict['name']}")
    print(f"Owner（所有者的登录名）: {repo_dict['owner']['login']}")  # owner访问所有者的字典，login获取登录名。
    print(f"Stars（项目获得星星数）: {repo_dict['stargazers_count']}")
    print(f"Repository（项目仓库url）: {repo_dict['html_url']}")
    print(f"Created（项目创建时间）: {repo_dict['created_at']}")
    print(f"Updated（项目最后更新时间）: {repo_dict['updated_at']}")
    print(f"Description（仓库描述）: {repo_dict['description']}")
