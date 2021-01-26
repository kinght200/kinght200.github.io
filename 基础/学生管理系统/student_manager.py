import file_manager
from 基础.学生管理系统 import model

name = ''


def add_student():
    """
    添加学生信息
    """
    x = file_manager.read_json(name + '.json', {})
    if not x:
        students = []
        num = 0
    else:
        students = x['all_student']
        num = int(x['num'])
    while True:
        s_name = input('请输入学生姓名：')
        s_age = input('请输入年龄：')
        s_gender = input('请输入性别：')
        s_tel = input('请输入电话号码：')

        num += 1
        # 字符串的zfill方法，在字符串的前面补0 4代表不够4位就补齐4位
        s_id = 'stu_' + str(num).zfill(4)

        # 创建一个Student对象
        s = model.Student(s_id, s_name, s_age, s_gender, s_tel)
        # {
        #     'all_student':[
        #         {'name':'zhangsan','age':18,'gender':'男','tel':'110'},
        #         {'name':'zhangsan','age':18,'gender':'男','tel':'110'}
        #     ],
        #     'num':2
        # }
        students.append(s.__dict__)

        # 拼接字典
        data = {'all_student': students, 'num': len(students)}
        # print(data) 测试
        # 把数据写入到文件里
        file_manager.write_json(name + '.json', data)
        choice = input('添加成功！\n1.继续\n2.返回\n请选择(1-2)')
        if choice == '2':
            break


def shwo_student():
    """
    查找学生信息
    """
    x = input('1.查看所有学生信息\n2.根据姓名查找\n3.根据学号查找\n其他：返回\n请选择：')
    y = file_manager.read_json(name + '.json', {})
    # if not y:   # 如果文件不存在，y是一个空字典{}
    #     students = []
    # else:
    #     students = y['all_student']
    students = y.get('all_student', [])
    if not students:
        print('该老师还没有学生，请添加学生')
        return

    if x == '1':
        pass

    elif x == '2':
        s_name = input('请输入你要查询的学生名字：')
        # same_name_students = []
        # for student in students:
        #     if student['name'] == s_name:
        #         same_name_students.append(student)

        # filter结果是一个filter类，它是一个可迭代对象

        students = filter(lambda s: s['name'] == s_name, students)  # students 就只保留了指定名字的学生

        # if not same_name_students:
        #     print('未找到学生')
        # for student in same_name_students:
        #     print('学号:{s_id},姓名:{name},性别:{gender},年龄:{age},电话:{tel}'.format(**student))

    elif x == '3':
        s_id = input('请输入你要查询的学生id：')
        students = filter(lambda s: s['s_id'] == s_id, students)

        # if not same_id_students:
        #     print('未找到学生')
        # for student in same_id_students:
        #     print('学号:{s_id},姓名:{name},性别:{gender},年龄:{age},电话:{tel}'.format(**student))
    else:
        return

    if not students:
        print('未找到学生')
        return

    for student in students:
        print('学号:{s_id},姓名:{name},性别:{gender},年龄:{age},电话:{tel}'.format(**student))


def modify_student():
    pass


def delte_student():
    y = file_manager.read_json(name + '.json', {})
    all_students = y.get('all_student', [])
    key = value = ''

    if not all_students:
        print('该老师还没有学生，请添加学生')
        return

    num = input('1.按姓名删\n2.按学号删\n其他：返回\n请选择：')
    if num == '1':
        key = 'name'
        value = input('请输入删除的学生名字:')
    elif num == '2':
        key = 's_id'
        value = input('请输入删除的学生id:')
    else:
        return

    students = list(filter(lambda s: s.get(key, '') == value, all_students))
    if not students:
        print('没有找到对应的学生')

    for i, s in enumerate(students):
        print('{x} 学号：{s_id},姓名：{name},性别：{gender},年龄：{age},电话：{tel}'.format(x=i, **s))
    n = input('请输入需要删除的学生的标号(0~{}),q-返回'.format(i))  # 使用变量 i 有潜在风险

    if not n.isdigit() or not 0 <= int(n) <= i:
        print('输入的内容不合法')
        return

    # 将学生从all_students里删除
    all_students.remove(students[int(n)])

    y['all_students'] = all_students
    file_manager.write_json(name + '.json', y)


def show_manager():
    # print('显示管理页面')
    content = file_manager.read_file('students_page.txt') % name
    # content = '欢迎%s老师进入学生管理系统:' % name
    while True:
        print(content)
        operator = input('请选择(1-5):')
        if operator == '1':
            add_student()
        elif operator == '2':
            shwo_student()
        elif operator == '3':
            modify_student()
        elif operator == '4':
            delte_student()
        elif operator == '5':
            break
        else:
            print('输入有误')
