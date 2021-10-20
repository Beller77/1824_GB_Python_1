import time
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]
start = time.perf_counter()
result = [i for i in src if src.count(i) == 1]
print(result)
print(time.perf_counter()-start)
