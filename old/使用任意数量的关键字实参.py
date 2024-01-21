###使用任意数量的关键字实参


"""形参**user_info 中的两个星号让Python创建一个名为user_info 的
空字典，并将收到的所有名称—值对都封装到这个字典中。在这个函数中，可以像访问其他字典那样访问user_info 中的名称—值对。
"""
def build_profile(first, last, **user_info):
    #创建一个空字典
    profile = {}
    #将键值对存入字典
    profile['first_name'] = first
    profile['last_name'] = last

    #获取所有的key - value对
    for key, value in user_info.items():
        # 将键值对存入字典
        profile[key] = value
    #返回字典
    return profile
user_profile = build_profile('albert', 'einstein',location='princeton',field='physics')
print(user_profile)
