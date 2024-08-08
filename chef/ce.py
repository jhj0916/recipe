import requests
import pprint
import json

url = "http://openapi.foodsafetykorea.go.kr/api/baba58c32c4343b78e78/COOKRCP01/json/1/30"

response = requests.get(url)
contents = response.tex


pp = pprint.PrettyPrinter(indent=4)
print(pp.pprint(contents))

# json_ob = json.loads(contents)
# print(json_ob)
# print(type(json_ob))

# body = json_ob['response']['body']['items']
# print(body)

# import pandas as pd
# from pandas.io.json import json_normalize

# dataframe = json_normalize(body)
# print(dataframe)
# ## dataframe으로 저장된 데이터 csv로 저장
# dataframe.to_csv('과속방지턱.csv',index=False)







