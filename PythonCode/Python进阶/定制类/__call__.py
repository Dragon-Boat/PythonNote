#coding=utf-8
#author: sloop
'''
����
�Ľ�һ��ǰ�涨���쳲��������У�

class Fib(object):
    ???
���һ��__call__�������õ��ø��򵥣�

>>> f = Fib()
>>> print f(10)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
'''

## fail��������©��-f(1)
class Fib(object):
    def __call__(self,num):
        L = [0, 1]
        for i in range(num-2):
            L.append(L[-1]+L[-2])
        return L

f = Fib()
print f(10)

'''
class Fib(object):
    def __call__(self, num):
        a, b, L = 0, 1, []
        for n in range(num):
            L.append(a)
            a, b = b, a + b
        return L

f = Fib()
print f(10)

-------------------------------

class Fib(object):
    def __call__(self,num):
        L=[0,1]
        for i in range(num-2):
            L.append(L[-1]+L[-2])
        return L

f = Fib()
print f(10)
'''

'''
__call__
��Python�У�������ʵ��һ������

>>> f = abs
>>> f.__name__
'abs'
>>> f(-123)
123
���� f ���Ա����ã����ԣ�f ����Ϊ�ɵ��ö���

���еĺ������ǿɵ��ö���

һ����ʵ��Ҳ���Ա��һ���ɵ��ö���ֻ��Ҫʵ��һ�����ⷽ��__call__()��

���ǰ� Person ����һ���ɵ��ö���

class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def __call__(self, friend):
        print 'My name is %s...' % self.name
        print 'My friend is %s...' % friend
���ڿ��Զ� Person ʵ��ֱ�ӵ��ã�

>>> p = Person('Bob', 'male')
>>> p('Tim')
My name is Bob...
My friend is Tim...
���� p('Tim') ���޷�ȷ�� p ��һ����������һ����ʵ�������ԣ���Python�У�����Ҳ�Ƕ��󣬶���ͺ��������𲢲�������
'''