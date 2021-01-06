# 使用递归求n!   n!=n*(n-1)!
# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n - 1)
#
#
# print(factorial(6))


# 求斐波那契数列
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 2) + fibonacci(n - 1)


print(fibonacci(8))
