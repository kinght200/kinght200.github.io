chars = ['a', 'c', 'x', 'd', 'p', 'a', 'p', 'a', 'c']

# {'a':3,'c':2,'x':1,'d':1.'p':2}
char_count = {}

for char in chars:
    # if char in char_count:
    #     # print('字典里已经有了这个字符' % char)
    #     char_count[char] += 1
    # else:
    #     # print('字典里没有这个字符%s'%char)
    #     char_count[char] = 1    # {'a':1}
    if char not in char_count:
        char_count[char] = chars.count(char)
print(char_count)
# print(char_count.items())
