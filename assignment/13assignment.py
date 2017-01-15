## 가위,바위,보 게임
## 모두 3번을 지거나 3번을 이기면 게임은 최종 스코어를 보여주며 종료

import random

kind = ["가위", "바위", "보"]

your_score = 0
com_score = 0

while your_score != 3 or com_score != 3:
    a = input("가위, 바위, 보 중 고르세요 : ")
    com = random.choice(kind)
    if a == "가위" and com == "가위":
        print("비겼습니다")
