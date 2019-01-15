def solution(arr):
    # # count를 이용해서 -1번만큼 지우는 방식
    # for i in arr:
    #     if arr.count(i) > 1:
    #         answer = arr.pop(arr.count(i)-1)
    # return answer               # 분절됐다가 다시 연속되는 값을 제거할 수 없다. 

# remove말고 pop을 사용할 수는 없을까?
    for i in range(len(arr)):     # range값으로 할당하면 global로 할당되기 때문에 pop이나 remove를 써서 값을 뽑아내면 
        if arr[i] == arr[i+1]:    # 무조건 range값이 초과될 수 밖에 없음
            arr.pop(i)
    return arr

print(solution([1,1,3,3,0,1,1]))