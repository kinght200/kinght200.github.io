# 声明一个字典保存一个学生的信息，学生信息中包括：姓名、年龄、成绩（单科）、电话、性别（男、女、不明）
# student = {'name': '张三', 'age': 18, 'score': 98, 'tel': '1388888998', 'gender': 'female'}
# 声明一个列表，在列表中保存6个学生的信息（6个题1中的字典）
students = [
    {'name': '张三', 'age': 18, 'score': 98, 'tel': '1388888998', 'gender': 'female'},
    {'name': '李四', 'age': 28, 'score': 95, 'tel': '1388666666', 'gender': 'male'},
    {'name': '王五', 'age': 21, 'score': 98, 'tel': '1365588999', 'gender': 'unknown'},
    {'name': 'Chris', 'age': 17, 'score': 58, 'tel': '137775523', 'gender': 'male'},
    {'name': 'jack', 'age': 23, 'score': 52, 'tel': '1399999928', 'gender': 'female'},
    {'name': 'tony', 'age': 15, 'score': 89, 'tel': '1388888888', 'gender': 'unknown'}
]
# 1、统计不及格学生的个数
# count = 0
# for student in students:
#     if student['score'] < 60:
#         count += 1
# print('不及格的学生有%d个' % count)

# 打印不及格学生的名字和对应的成绩
# count = 0
# for student in students:
#     if student['score'] < 60:
#         count += 1
#         print('%s不及格，分数是%d' % (student['name'], student['score']))
# print('不及格的学生有%d个' % count)

# 统计未成年学生的个数
# count = 0
# teenager_count=0
# for student in students:
#     if student['score'] < 60:
#         count += 1
#         print('%s不及格，分数是%d' % (student['name'], student['score']))
#         if student['age'] < 18:
#             teenager_count += 1
# print('不及格的学生有%d个' % count)
# print('未成年的学生有%d个' % teenager_count)

# 打印手机尾号是8的学生的名字
# count = 0
# teenager_count=0
# for student in students:
#     if student['score'] < 60:
#         count += 1
#         print('%s不及格，分数是%d' % (student['name'], student['score']))
#     if student['age'] < 18:
#         teenager_count += 1
#     if student['tel'].endswith('8'):
#         print('%s的手机好以8结尾' % student['name'])
# print('不及格的学生有%d个' % count)
# print('未成年的学生有%d个' % teenager_count)

# 打印最高分和对应的学生名字
# max_score = students[0]['score']  # 假设第0个学生的成绩是最高分
# # max_index = 0  # 假设最高分的学生下标是 0
# for i, student in enumerate(students):
#     if student['score'] > max_score:  # 遍历时,发现了一个学生的成绩大于假设的最大数
#         max_score = student['score']
#         # max_index = i  # 修改最高分的同时,把最高分的下标也修改
# print('最高的成绩是%d分' % max_score)
#
# for student in students:
#     if student['score'] == max_score:
#         print('最高分是%s' % student['name'])
# print('最高分的名字是%s' % students[max_index]['name'])

# 将列表按学生成绩从大到小排序
for j in range(0, len(students) - 1):
    for i in range(0, len(students) - 1 - j):
        if students[i]['score'] < students[i + 1]['score']:
            students[i], students[i + 1] = students[i + 1], students[i]
print(students)
