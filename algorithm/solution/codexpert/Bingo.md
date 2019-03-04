## Bingo

### 문제설명

- 빙고판을 만든 뒤, 하나씩 지워나가다가 3줄의 빙고가 생기는 순간 몇번째 수를 들었는지 리턴하는 프로그램.



### 풀이 방법

- 빙고판은 split하여 5*5 행렬로 나타낸다.
- 숫자는 하나씩 받아서 `i:j`로 하나씩 딕셔너리로 정렬한다
- 숫자를 하나씩 지울때마다 몇줄의 빙고가 생겼는지 확인한다.



#### 코드

```python
def bingo(match):
    cnt = 0
    for x in match:
        if len(match[x]) == 5:
            cnt += 1
    for i in range(5):
        for j in range(5):
            if i not in match[j]:
                break
        else:
            cnt += 1
    for i in range(5):
        if i not in match[i]:
            break
    else:
        cnt += 1
    for i in range(5):
        if i not in match[4-i]:
            break
    else:
        cnt += 1
    return cnt

def check(arr, numbers):
    match = {i:[] for i in range(5)}
    for i in range(5):
        for j in range(5):
            for k in range(5):
                if numbers[i][j] in arr[k]:
                    match[k] += [arr[k].index(numbers[i][j])]
                    break
            if bingo(match) >= 3:
                return i*5+j+1

arr = [input().split() for _ in range(5)]
numbers = [input().split() for _ in range(5)]
print(check(arr, numbers))
```

