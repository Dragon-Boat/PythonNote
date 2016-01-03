#coding=utf-8
#author: sloop
'''
����
��һ�ڵ�@performanceֻ�ܴ�ӡ�룬��� @performace ����һ��������������'s'��'ms'��

@performance('ms')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
'''

import time

def performance(unit):
    def performance_dec(f):
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
    for i in range(1, 1000):
        print i
    return reduce(lambda x,y: x*y, range(1, n+1))

print factorial(10)

'''
��д������decorator
������һ�ڵ� @log װ������

def log(f):
    def fn(x):
        print 'call ' + f.__name__ + '()...'
        return f(x)
    return fn
���ֶ��ڱ�װ�εĺ�����log��ӡ������ǲ��ܱ�ģ����˺���������

����еĺ����ǳ���Ҫ��ϣ����ӡ��'[INFO] call xxx()...'���еĺ�����̫��Ҫ��ϣ����ӡ��'[DEBUG] call xxx()...'����ʱ��log�����������Ҫ����'INFO'��'DEBUG'�����Ĳ���������������

@log('DEBUG')
def my_func():
    pass
������Ķ��巭��ɸ߽׺����ĵ��ã����ǣ�

my_func = log('DEBUG')(my_func)
�������俴��ȥ���ǱȽ��ƣ���չ��һ�£�

log_decorator = log('DEBUG')
my_func = log_decorator(my_func)
�����������൱�ڣ�

log_decorator = log('DEBUG')
@log_decorator
def my_func():
    pass
���ԣ���������log�������ȷ���һ��decorator�������������decorator��������my_func�������º�����

def log(prefix):
    def log_decorator(f):
        def wrapper(*args, **kw):
            print '[%s] %s()...' % (prefix, f.__name__)
            return f(*args, **kw)
        return wrapper
    return log_decorator

@log('DEBUG')
def test():
    pass
print test()
ִ�н����

[DEBUG] test()...
None
��������3��Ƕ�׵�decorator���壬������Ȱ����𿪣�

# ��׼decorator:
def log_decorator(f):
    def wrapper(*args, **kw):
        print '[%s] %s()...' % (prefix, f.__name__)
        return f(*args, **kw)
    return wrapper
return log_decorator

# ����decorator:
def log(prefix):
    return log_decorator(f)
���Ժ�ᷢ�֣����û�ʧ�ܣ���Ϊ��3��Ƕ�׵�decorator�����У����ڲ��wrapper�����������Ĳ���prefix�����ԣ���һ���հ������ͨ�ĺ������û�Ƚ����ѡ���֧�ֱհ��ı������Ҫʵ��ͬ���Ĺ��ܾ���Ҫ����Ĵ��롣
'''