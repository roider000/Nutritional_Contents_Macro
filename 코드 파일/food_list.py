import csv
import time
start_time = time.time()
# 걸리는 시간 1초도 안걸림 

# 전체_리스트 외 리스트 품복20종
곡류_및_그_제품_리스트 = [] 
감자_및_전분류_리스트 = []
당류_리스트 = []
두류_리스트 = []
견과_및_종실류_리스트 = []
채소류_리스트 = []
버섯류_리스트 = []
과일류_리스트 = []
육류_리스트 = []
난류_리스트 = []
어패류_및_기타_수산물_리스트  = []
해조류_리스트  = []
우유류_및_유제품_리스트  = []
유지류_리스트  = []
차류_리스트  = []
음료류_리스트  = []
주류_리스트  = []
조미료류_리스트  = []
조리가공식품류_리스트 = []
기타_리스트  = []


with open("Nutritional_Contents_DB.csv", "r", encoding ="cp949") as f:
    rows_read = csv.reader(f)
    전체_리스트 = [row for row in rows_read]
    for row in 전체_리스트:
        if row[0] == "곡류 및 그 제품":
           곡류_및_그_제품_리스트.append(list(row))
        elif row[0] == "감자 및 전분류":
            감자_및_전분류_리스트.append(list(row))
        elif row[0] == "당류":
            당류_리스트.append(list(row))
        elif row[0] == "두류":
            두류_리스트.append(list(row))
        elif row[0] == "견과 및 종실류":
            견과_및_종실류_리스트.append(list(row))
        elif row[0] == "채소류":
            채소류_리스트.append(list(row))
        elif row[0] == "버섯류":
            버섯류_리스트.append(list(row))
        elif row[0] == "과일류":
            과일류_리스트.append(list(row))
        elif row[0] == "육류":
            육류_리스트.append(list(row))
        elif row[0] == "난류":
            난류_리스트.append(list(row))
        elif row[0] == "어패류 및 기타 수산물":
            어패류_및_기타_수산물_리스트.append(list(row))
        elif row[0] == "해조류":
            해조류_리스트.append(list(row))
        elif row[0] == "우유류 및 유제품":
            우유류_및_유제품_리스트.append(list(row))
        elif row[0] == "유지류":
            유지류_리스트.append(list(row))
        elif row[0] == "차류":
            차류_리스트.append(list(row))
        elif row[0] == "음료류":
            음료류_리스트.append(list(row))
        elif row[0] == "주류":
            주류_리스트.append(list(row))
        elif row[0] == "조미료류":
            조미료류_리스트.append(list(row))
        elif row[0] == "조리가공식품류":
            조리가공식품류_리스트.append(list(row))
        elif row[0] == "기타":
            기타_리스트.append(list(row))

# 리스트 선택에 따라 리스트 박스에서 보여주는 항목이 다름


# 직접 검색 : 식품명에 입력한 글자가 포함되면 출력
food_name = input("음식명 :")

for food in 전체_리스트:
    if food_name in food[1]:
        print(food)
