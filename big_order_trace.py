import tushare as ts
import json

datas = ts.top_list('2018-07-17')
j = json.dumps(datas)
print j