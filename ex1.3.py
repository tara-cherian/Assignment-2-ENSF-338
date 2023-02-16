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