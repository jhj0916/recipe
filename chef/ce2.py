import requests
import json

url = 'http://openapi.foodsafetykorea.go.kr/api/baba58c32c4343b78e78/COOKRCP01/json/1/2'


response = requests.get(url)
   
data = response.json()
recipes = data['COOKRCP01']['row']


recipe_info = [
    {
        'name': recipe['RCP_NM'],
        'hashtag': recipe['HASH_TAG'],
        'calories': recipe['INFO_ENG'],
        'carbs': recipe['INFO_CAR'],
        'protein': recipe['INFO_PRO'],
        'fat': recipe['INFO_FAT'],
        'ingredients':recipe['RCP_PARTS_DTLS']
    }
    for recipe in recipes
]

print(recipe_info)
