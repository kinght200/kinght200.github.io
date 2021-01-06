def test(a):
    a = 100


def demo(nums):
    nums[0] = 10


x = 1
test(x)
print(x)  # 1

y = [3, 4, 5, 1, 6]
demo(y)
print(y)  # [10, 4, 5, 1, 6]
