#    a = 0
#    while a < 1000:
#        a = a + 1
#        if a % 3 != 0: continue
#        print(a)
# 3의 배수들이 모두 출력된다. 어떻게 합으로 만들지??

result = 0 # 합
i = 1
while i <= 1000:
    if i % 3 == 0 : # 3으로 떨어지는 수
        result += i # 합하고
    i += 1 # 다시 +1해서 돌리기

print(result)
