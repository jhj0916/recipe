from flask import Flask, render_template_string
import requests

app = Flask(__name__)

@app.route('/')
def home():
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
            'ingredients': recipe['RCP_PARTS_DTLS']
        }
        for recipe in recipes
    ]

    # HTML 템플릿 생성
    html_template = '''
    <!doctype html>
    <html lang="ko">
    <head>
        <meta charset="utf-8">
        <title>레시피 목록</title>
    </head>
    <body>
        <h1>레시피 목록</h1>
        <ul>
            {% for recipe in recipes %}
                <li>
                    <h2>{{ recipe.name }}</h2>
                    <p>해시태그: {{ recipe.hashtag }}</p>
                    <p>칼로리: {{ recipe.calories }}</p>
                    <p>탄수화물: {{ recipe.carbs }}</p>
                    <p>단백질: {{ recipe.protein }}</p>
                    <p>지방: {{ recipe.fat }}</p>
                    <p>재료: {{ recipe.ingredients }}</p>
                </li>
            {% endfor %}
        </ul>
    </body>
    </html>
    '''

    return render_template_string(html_template, recipes=recipe_info)

if __name__ == '__main__':
    app.run(debug=True)
