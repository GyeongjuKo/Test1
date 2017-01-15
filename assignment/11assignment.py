## 한식, 일식, 중식 중 한가지를 선택받아 식당 임의 추천

import random

# kind = ["한식", "중식", "일식"]
korean = ["고향집", "엄마밥상", "함흥냉면"]
chinese = ["사천왕", "홍콩집", "장순루"]
japanese = ["이자카야", "원참치", "초밥집"]

a = input("한식, 중식, 일식 중 한가지를 고르세요 : ")
# print(type(a))

if a == "한식":
    print("{}을(를) 추천합니다.".format(random.choice(korean)))
else:
    if a == "중식":
        print("{}을(를) 추천합니다.".format(random.choice(chinese)))
    else:
        if a == "일식":
            print("{}을(를) 추천합니다.".format(random.choice(japanese)))
        else:
            print("세개 중 한가지를 고르세요!")
