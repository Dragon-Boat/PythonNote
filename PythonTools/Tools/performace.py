#coding=utf-8
#author: sloop


import time, functools

'''
���㺯������-����ʱ��
���������'s' 'ms'
'''
def performance(unit):
    def performance_dec(f):
        @functools.wraps(f) #��ɺ����Զ����ƹ��ܣ���ֹ�ı亯��ԭ�е�����
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
print factorial.__name__
