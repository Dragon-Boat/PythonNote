#coding=utf-8
#author: sloop
'''
װ����ģʽ
�ڲ��ı�ԭ�����Ļ��������ø߽׺������ӹ���
ʹ�� decorator ��Python�ṩ�� @ �﷨���������Ա����ֶ���д f = decorate(f) �����Ĵ��롣
'''
# װ���� log
def log(f):
    def fn(*args, **kw):    #ʹ�ÿɱ����
        print 'call '+f.__name__+'()...'
        return f(*args, **kw)
    return fn

# �׳�
@log
def factorial(n):
    return reduce(lambda x,y: x*y, range(1,n+1))

print factorial(10)

@log
def add(x,y):
    return x+y

print add(1,2)

'''
def f1(x):
    return x*2

def new_fn(f):
    def fn(x):
        print 'call '+f.__name__+'()'
        return f(x)
    return fn

g = new_fn(f1)
print g(2)
'''