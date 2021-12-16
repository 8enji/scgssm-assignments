# algorithm from geeksforgeeks.org
import sys
import random
import time

A = [random.randint(1,10000) for _ in range(20000)]

start = time.time()

for i in range(len(A)):


    min_idx = i
    for j in range(i + 1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j


    A[i], A[min_idx] = A[min_idx], A[i]

end = time.time()

print(start)
print(end)
print('total time taken:', end - start, 'seconds')