# Sort 기법

- 버블정렬 구현
- 퀵, 머지정렬을 구현할 줄 안다.



## 버블정렬

- 버블정렬은 두개의 원소를 비교하며 최대 n<sup>2</sup> 번의 연산이 필요하다.

```python
for i in range(N-1):
    for j in range(i+1, N):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]
```

순차적으로 대소를 비교해 교환하며, 

순차적으로 교환이 일어난다는 것과 연산횟수가 점점 줄어들게 설계할수 있음을 알아야 한다.



## 머지정렬

- O(nlogn)

```python
def MergeSort(s,e):
    if s >= e:
        return
    m = (s+e)//2
    MergeSort(s, m)
    MergeSort(m+1, e)
    L,R,T = s, m+1, s  # 왼쪽, 오른쪽, 임시버퍼의 위치 할당.
    while L <= m and R <= e:
        if arr[L] < arr[R]:		# 왼쪽영역 값이 작으면 왼쪽영역값을 임시버퍼로
            temp[T] = arr[L]
        else:
            temp[T] = arr[R]
        T += 1
        R += 1
    # 왼쪽 영역이 아직 남아있으면 나머지를 한꺼번에 보내주기
    # 좀 다르게 할 수 있을것 같은데... 개선필요
    while L <= m:
        temp[T] = arr[L]
        T += 1
        L += 1
    # 마찬가지로 오른쪽영역이 아직 남아있으면 나머지를 한꺼번에 보내주기
    while R <= e:
        temp[T] = arr[R]
        T += 1
        R += 1
    # 소트 작업이 끝난 배열을 다시 원본배열에 넣어주기.
    for i in range(s, e+1):
        arr[i] = temp[i]
```



## 퀵정렬

- 최악의 경우 n<sup>2</sup>번 연산.
- 비교대상과 교환대상이 다른 정렬인것에 유의해야 한다.
- 재귀적으로 구현한다.

```python
def QuickSort(s,e):
    if s >= e:
        return
    pivot, target = e, s
    for left in range(s, e-1):
        if arr[left] < arr[pivot]:
            arr[left], arr[pivot] = arr[pivot], arr[left]
            target = s+1
    arr[pivot], arr[target] = arr[target], arr[pivot]
    QuickSort(s, target-1)
    QuickSort(target+1, e)
```

