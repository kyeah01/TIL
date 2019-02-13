def square(n):
    sum_number = 0
    for number in range(1, n+1):
        sum_number += number**2
    return sum_number

print(square(3))