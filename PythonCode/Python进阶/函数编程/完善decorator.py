#coding=utf-8
#author: sloop
'''
����
��˼����������@decorator��@functools.wrapsӦ�÷������ģ�

def performance(unit):
    def perf_decorator(f):
        def wrapper(*args, **kw):
            ???
        return wrapper
    return perf_decorator
'''

import time, functools

def performance(unit):
    def performance_dec(f):
        @functools.wraps(f)
        def wrapper(*args, **kw):
            t1 = time.time()
            r = f(*args, **kw)
            t2 = time.time()
            t = (t2 - t1) * 1000 if unit=='ms' else (t2 - t1)
            print 'call %s() in %f %s' % (f.__name__, t, unit)
            return r
        return wrapper
    return performance_dec

@performance('ms')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))

print factorial.__name__

'''
����decorator
@decorator���Զ�̬ʵ�ֺ������ܵ����ӣ����ǣ�����@decorator�����족��ĺ�������ԭ������ȣ����˹��ܶ�һ���⣬��û��������ͬ�ĵط���

��û��decorator������£���ӡ��������

def f1(x):
    pass
print f1.__name__
����� f1

��decorator������£��ٴ�ӡ��������

def log(f):
    def wrapper(*args, **kw):
        print 'call...'
        return f(*args, **kw)
    return wrapper
@log
def f2(x):
    pass
print f2.__name__
����� wrapper

�ɼ�������decorator���ص��º����������Ѿ�����'f2'������@log�ڲ������'wrapper'���������Щ�����������Ĵ���ͻ�ʧЧ��decorator���ı��˺�����__doc__���������ԡ����Ҫ�õ����߿�����һ������������@decorator�ġ����족������Ҫ��ԭ������һЩ���Ը��Ƶ��º����У�

def log(f):
    def wrapper(*args, **kw):
        print 'call...'
        return f(*args, **kw)
    wrapper.__name__ = f.__name__
    wrapper.__doc__ = f.__doc__
    return wrapper
����дdecorator�ܲ����㣬��Ϊ����Ҳ���Ѱ�ԭ���������б�Ҫ���Զ�һ��һ�����Ƶ��º����ϣ�����Python���õ�functools���������Զ��������������ơ�������

import functools
def log(f):
    @functools.wraps(f)
    def wrapper(*args, **kw):
        print 'call...'
        return f(*args, **kw)
    return wrapper
�����Ҫָ�����������ǰ�ԭ����ǩ���ĳ���(*args, **kw)����ˣ��޷����ԭ������ԭʼ������Ϣ���������ǲ��ù̶�������װ��ֻ��һ�������ĺ�����

def log(f):
    @functools.wraps(f)
    def wrapper(x):
        print 'call...'
        return f(x)
    return wrapper
Ҳ���ܸı�ԭ�����Ĳ���������Ϊ�º����Ĳ�����ʼ���� 'x'��ԭ��������Ĳ�������һ���� 'x'��
'''