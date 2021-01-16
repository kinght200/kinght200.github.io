class A(object):
    pass


class B(object):
    def foo(self):
        print('我是B类里的foo方法')


class C(A):
    def foo(self):
        print('我是C类里的foo方法')


class D(B):
    pass


class X(D, C):
    pass


x = X()
x.foo()
print(X.__mro__)
# (<class '__main__.X'>, <class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>,
# <class 'object'>)
