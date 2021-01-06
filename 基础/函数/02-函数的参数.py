# def 函数名(参数)：
#   函数体

# 调用函数：函数名(参数)
# 函数声明时，括号里的参数我们称为形式参数，简称形参
# 形参的值是不确定的，只是用来占位的
def ccc(place, person1, person2):
    # place='道观',person1='老道',person2='道童'
    print('从前有座山')
    print('山上有座' + place)
    print(place + '有个' + person1)
    print('还有个' + person2)
    print(person1 + '在给' + person2 + '讲故事')


# 调用函数时传递数据
# 函数调用时传入的参数，才是真正的参与运算的数据，我们称为实参
ccc('道观', '老道', '道童')  # 会把实参一一对应的传递，交给形参处理
# 还可以通过定义变量名的形式给形参赋值
ccc(person1='禅师', person2='青年')
