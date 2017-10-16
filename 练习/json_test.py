import json

data = [{'a':1,'b':2,'c':3,'d':4,'e':5}]
# data = ['a','b','c','d']
# print(type(data),data)
json_str = json.dumps(data,sort_keys=True,indent=4,separators=(',',':'))
print(type(json_str),json_str)

# json_list = json.loads(json_str)
# print(type(json_list),json_list)