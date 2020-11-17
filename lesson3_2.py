# 9! => 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1

def factorial(n, result=0):
    if n == 1:
        return result
    result = result + n
    return factorial(n - 1, result)


print(factorial(9))