# 에러나지 않는 구구단

a = input("몇 단을 출력할래요? : ")
a = int(a)

if a < 2 or a > 9:
    print("2부터 9까지만 입력가능해요")
else:
    for num in range(1, 10):
        b = a * num
        print("{} * {} = {}".format(a, num, b))
