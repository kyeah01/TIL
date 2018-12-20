
# 파이썬 dictionary 활용 기초
# # for문, if문을 활용하는 법

# dict = {
#     "대전" : 23,
#     "서울" : 30,
#     "구미" : 25
# }


# print(type(dict.values()))


# 1. 평균을 구하세요.


# score = {
#     "국어" : 87,
#     "영어" : 92,
#     "수학" : 40
# }

# sl = len(score)
# sums = sum(score.values())
# aver = sums/sl

# sums2 = 0
# sums3 = score.values()

# for i in sums3:
#     sums2 = sums2 + i
#     # sums2 += i

# print(aver)
# print(sums2/sl)


# 2. 반평균을 구하시오


# scores = {
#     "철수" : {
#         "수학" : 80,
#         "국어" : 90,
#         "음악" : 100
#     },
#     "영희" : {
#         "수학" : 70,
#         "국어" : 60,
#         "음악" : 50
#     }
# }

# len_t = 0
# total_scores = 0

# for i in scores.keys():
#     for j in scores[i].values():
#         total_scores += j
#         len_t += 1

# aver_scores = total_scores/(len_t)

# print(aver_scores)


# for key, value in scores.items():
#     print(key)
#     print(value)


# 3. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?

cities = {
    "서울" : {-6, -10, 5},
    "대전" : {-3, -5, 2},
    "광주" : {0, -2, 10},
    "부산" : {2, -2, 9}
}

minB = 0
maxB = 0

for name, temp in cities.items():

    if minB > min(temp):
        minB = min(temp)
        nameLB = name
    else:
        pass

    if maxB < max(temp):
        maxB = max(temp)
        nameHB = name
    else:
        pass

print("가장 추웠던 곳은",nameLB,"이고,",minB,"도 였습니다.")
print("가장 더웠던 곳은", nameHB,"이고,",maxB,"도 였습니다.")