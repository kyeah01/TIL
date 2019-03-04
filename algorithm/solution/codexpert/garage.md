## 창고다각형

### 문제 내용

- 문제가 말도안된다.

  <img width="350" alt="pimg1786_1" src="https://user-images.githubusercontent.com/45934061/53695909-ac1ec600-3e04-11e9-81d1-11db27741410.png">

- 한마디로 요약하면, 위와 같은 기둥이 주어졌을때, 위를 감싸되 안으로 패이지 않는 다각형을 그리고, 그 다각형의 넓이를 구하라는 문제다.

- 물론 다각형의 넓이가 최소화될때를 가정한다.



### 주의할 점

- 인덱스 에러 문제를 여러번 마주했었다. 기둥은 기둥의 갯수만큼만 주어지고 기둥이 떨어져있는 길이와는 관련이 없다.

- 가장 높은 경우로 반반을 나눠서 각각에서 출발한다고 생각했더니 가장 높은 경우의 넓이가 계산되지 않는 문제가 발생했었다.



### 풀이방법

- 첫번째 기둥을 가지는 위치로부터 마지막 기둥을 가지는 위치까지  max값을 가지는 곳을 기준으로 반반 나누어 계단을 만든다고 생각했다.
- 0부터 마지막 기둥을 가지는 위치까지 리스트를 생성한 후, 현재까지 나왔던 값 중 가장 높은 값을 기준으로 하여 흙을 채워나가듯이 리스트를 채워나갔다.(맥스값 위치까지.)
- 그 후에는 뒤에서부터 다시 출발하여 똑같은 일을 반복했다.
- 이후 그 height 리스트의 sum을 반환했다.



#### 코드

```python
n = int(input())
pillar = [list(map(int, input().split())) for _ in range(n)]
pillar.sort()
pillar_exist = [pillar[i][0] for i in range(n)]
maxN = 0

for i in range(n):
    if pillar[i][1] > pillar[maxN][1]:
        maxN = i

height = [0 for i in range(pillar[-1][0]+1)]
roof = 0
for i in range(pillar[maxN][0]+1):
    if i in pillar_exist:
        roof = max(roof, pillar[pillar_exist.index(i)][1])
    height[i] = roof

roof = 0
for i in range(len(height)-1, pillar[maxN][0], -1):
    if i in pillar_exist:
        roof = max(roof, pillar[pillar_exist.index(i)][1])
    height[i] = roof

print(sum(height))
```

