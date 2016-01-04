#coding=utf-8
#author: sloop
'''
����
쳲������������� 0, 1, 1, 2, 3, 5, 8...���ɡ�

���дһ��Fib�࣬Fib(10)��ʾ���е�ǰ10��Ԫ�أ�print Fib(10) ���Դ�ӡ�����е�ǰ 10 ��Ԫ�أ�len(Fib(10))������ȷ�������еĸ���10��
'''

class Fib(object):

    def __init__(self, num):
        a,b,L = 0,1,[]
        for n in range(num):
            L.append(a)
            a,b = b, a+b
        self.numbers = L

    def __str__(self):
        return str(self.numbers)
    
    __repr__ = __str__

    def __len__(self):
        return len(self.numbers)

f = Fib(10)
print f
print len(f)

'''
__len__
���һ������ֵ���һ��list��Ҫ��ȡ�ж��ٸ�Ԫ�أ��͵��� len() ������

Ҫ�� len() ��������������������ṩһ�����ⷽ��__len__()��������Ԫ�صĸ�����

���磬����дһ�� Students �࣬�����ִ���ȥ��

class Students(object):
    def __init__(self, *args):
        self.names = args
    def __len__(self):
        return len(self.names)
ֻҪ��ȷʵ����__len__()�������Ϳ�����len()��������Studentsʵ���ġ����ȡ���

>>> ss = Students('Bob', 'Alice', 'Tim')
>>> print len(ss)
3
'''