def missing_number(list ,n):
    return sum(range(1, n+1)) - sum(list)
print(missing_number([1 , 2, 3, 4 ], 5))
