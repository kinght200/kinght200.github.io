s1 = 'hello'
s2 = 'world'
print(s1 + s2)
# 列表可以使用extend方法将两个列表合并成为一个列表

nums1 = [1, 2, 3, 4, 5]
nums2 = [6, 7, 8, 9]
nums1.extend(nums2)
print(nums1)
print(nums1 + nums2)

words1 = ('hello', 'good')
words2 = ('yes', 'ok')
print(words1 + words2)  # ('hello', 'good', 'yes', 'ok')

person1 = {'name': '张三', 'age': 18}
person2 = {'addr': '上海', 'height': 180}
person1.update(person2)
print(person1)

# 字典之间不支持加法运算，只能使用update来连接
# print(person1 + person2)
