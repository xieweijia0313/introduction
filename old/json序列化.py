import json
historyTransactions = [

    {
        'time'   : '20170101070311',  # 交易时间
        'amount' : '3088',            # 交易金额
        'productid' : '45454455555',  # 货号
        'productname' : 'iphone7'     # 货名
    },
    {
        'time'   : '20170101050311',  # 交易时间
        'amount' : '18',              # 交易金额
        'productid' : '453455772955', # 货号
        'productname' : '奥妙洗衣液'   # 货名
    }

]

# dumps 方法将数据对象序列化为 json格式的字符串
jsonstr = json.dumps(historyTransactions,ensure_ascii=False)
print(jsonstr)

#反序列化
obj = json.loads(jsonstr)
print(obj)
