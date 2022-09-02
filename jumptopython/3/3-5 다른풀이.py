#    scores = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
#    total = 0

#    for i in range(len(scores)):
#        total += scores[i]

#    print(total/len(scores))

scores = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0

for score in scores:
    total += score # 점수를 모두 더한다.

average = total / len(scores)
[print(average)]