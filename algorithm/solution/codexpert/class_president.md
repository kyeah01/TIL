## 나는 학생회장이다(투표)

### 문제내용

- 세명의 후보에게 3점, 2점, 1점을 각각 n명의 사람이 투표할때, 대표를 선발하는 알고리즘.
- 총점이 같을 경우 3점이 가장 많은 사람이, 마찬가지로 2점이 가장 많은 사람이 선발된다.
- 후보를 선발할 수 없는 경우에는 0과 최고득점수를 출력한다.



### 주의할 점

- 문제에도 나와있지만 총점, 3점과 2점 득표수가 같으면 1점 득표수도 같다. 고려할 필요 없음.
- 가장 큰 값이 두번이상 나타날 수 있기 때문에 그냥 max와 index를 활용해서는 풀 수 없다.



### 풀이방법

- 3의 갯수를 찾는 방법과 2의 갯수를 찾는 방법은 똑같다. 따라서 재귀활용한다.
- 총합점을 찾는 것은 3과 2의 갯수를 찾는 방법과 조금 다르니까 그냥 바깥에서 한다!



#### 코드

```python
def check(total, nomi, num):
    number = [0,0,0]
    for j in range(n):
        for i in nomi:
            if vote[j][i] == num:
                number[i] += 1
    maxN = max(number)
    nomi = [i for i in range(3) if maxN == number[i]]
    if len(nomi) == 1:
        return (nomi[0]+1, total)
    elif num == 2:
        return (0, total)
    else:
        return check(total, nomi, num-1)

n = int(input())
vote = [list(map(int, input().split())) for _ in range(n)]

total = [0,0,0]
for i in range(n):
    for j in range(3):
        total[j] += vote[i][j]
maxN = max(total)

nomi = [i for i in range(3) if maxN == total[i]]
if len(nomi) == 1:
    print(nomi[0]+1, maxN)
else:
    print(*check(maxN, nomi, 3))
```



