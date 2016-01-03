#coding=utf-8
#author: sloop
'''
����
���дһ��@performance�������Դ�ӡ���������õ�ʱ�䡣
'''

import time

def performance(f):
    def fn(*args, **kw):
        t1 = time.time()
        r = f(*args, **kw)
        t2 = time.time()
        print 'call %s() in %fs' %(f.__name__,(t2 - t1))
        return r
    return fn

@performance
def factorial(n):
    for i in range(0,1000):
        x = i
    return reduce(lambda x,y: x*y, range(1, n+1))

print factorial(10)

'''
��д�޲���decorator
Python�� decorator �����Ͼ���һ���߽׺�����������һ��������Ϊ������Ȼ�󣬷���һ���º�����

ʹ�� decorator ��Python�ṩ�� @ �﷨���������Ա����ֶ���д f = decorate(f) �����Ĵ��롣

����һ��@log�Ķ��壺

def log(f):
    def fn(x):
        print 'call ' + f.__name__ + '()...'
        return f(x)
    return fn
���ڽ׳˺�����@log�����úܺã�

@log
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
print factorial(10)
�����

call factorial()...
3628800
���ǣ����ڲ�������һ���ĺ��������ý�����

@log
def add(x, y):
    return x + y
print add(1, 2)
�����

Traceback (most recent call last):
  File "test.py", line 15, in <module>
    print add(1,2)
TypeError: fn() takes exactly 1 argument (2 given)
��Ϊ add() ������Ҫ������������������ @log д����ֻ��һ�������ķ��غ�����

Ҫ�� @log ����Ӧ�κβ�������ĺ�������������Python�� *args �� **kw����֤��������Ĳ����������������ã�

def log(f):
    def fn(*args, **kw):
        print 'call ' + f.__name__ + '()...'
        return f(*args, **kw)
    return fn
���ڣ��������⺯����@log ��������������
'''