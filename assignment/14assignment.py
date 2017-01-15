# 00100
# 01110
# 11111
# 01110
# 00100
# for loop 중첩 이용 가능
#
# 000*000
# 00***00
# 0*****0
# *******
# 0*****0
# 00***00
# 000*000

a = 1
b = 5

for i in range(1, 6):
    if a <= 5:
        left_right = "0" * ((b - a) // 2)
        center = "1" * a
        print("{0}{1}{2}".format(left_right,center,left_right))
        a += 2
        else:
            a = 5
            for 1 range(1, 5):
                a -= 2
