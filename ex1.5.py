import timeit
import matplotlib.pyplot as plt

def func(n):    
    if n == 0 or n == 1:
        return n
    else:
        return (func(n-1) + func(n-2))


def memoized(n, cache = {}):
    result = 0
    if n in cache:
        result = cache[n]
    elif n == 0:
        result = 0
        cache[n] = result
    elif n == 1:
        result = 1
        cache[n] = result
    else:
        result = memoized(n-2) + memoized(n-1)
        cache[n] = result
    return result

elapsed_time_old = timeit.timeit(lambda : func(35), number = 1)
print(f'Elapsed time: {elapsed_time_old} seconds')

elapsed_time_new = timeit.timeit(lambda : memoized(35), number = 1)
print(f'Elapsed time: {elapsed_time_new} seconds')

input_values = range(36)
et_old = []
et_new = []
for i in input_values:
    et_old.append(timeit.timeit(lambda : func(i), number = 1))
    et_new.append(timeit.timeit(lambda : memoized(i), number = 1))
plt.plot(input_values, et_old, label='Original')
plt.plot(input_values, et_new, label='Memoized')
plt.xlabel('Data')
plt.ylabel('Time (s)')
plt.legend()
plt.show()