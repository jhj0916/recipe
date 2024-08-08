def display_recipes(recipes):
    result_div = document.getElementById('result')  # Element 대신 document.getElementById 사용
    result_div.innerHTML = ""  # 기존 내용 지우기

    for recipe in recipes:
        name = recipe['RCP_NM']
        hashtag = recipe['HASH_TAG']
        calories = recipe['INFO_ENG']
        carbs = recipe['INFO_CAR']
        protein = recipe['INFO_PRO']
        fat = recipe['INFO_FAT']
        ingredients = recipe['RCP_PARTS_DTLS']

        recipe_info = f"""
            <div class="recipe">
                <h3>{name}</h3>
                <p><strong>해시태그:</strong> {hashtag}</p>
                <p><strong>칼로리:</strong> {calories}</p>
                <p><strong>탄수화물:</strong> {carbs}</p>
                <p><strong>단백질:</strong> {protein}</p>
                <p><strong>지방:</strong> {fat}</p>
                <p><strong>재료:</strong> {ingredients}</p>
            </div>
        """
        result_div.innerHTML += recipe_info  # 레시피 정보를 결과 div에 추가
