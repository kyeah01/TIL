
colors = ['Apple', 'Banana', 'Coconut', 'Dell', 'Ele', 'Grape']

# 새로운 리스트 정의하기
fruit = []

deleteindex = [0,4,5]

for i in range(0, len(colors)):
    if i not in deleteindex:
        fruit.append(colors[i])
print(fruit)