#coding=utf-8
#author: sloop
'''
����
���������Rational��ʹ֮����ת��Ϊfloat��
'''

class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __int__(self):
        return self.p // self.q

    def __float__(self):
        return float(self.p) / self.q

print float(Rational(7, 2))
print float(Rational(1, 3))

'''
����ת��
Rational��ʵ�������������㣬���ǣ����Ҫ�ѽ��תΪ int �� float ��ô�죿

���������͸�������ת����

>>> int(12.34)
12
>>> float(12)
12.0
���Ҫ�� Rational תΪ int��Ӧ��ʹ�ã�

r = Rational(12, 5)
n = int(r)
Ҫ��int()��������������ֻ��Ҫʵ�����ⷽ��__int__():

class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q
    def __int__(self):
        return self.p // self.q
������£�

>>> print int(Rational(7, 2))
3
>>> print int(Rational(1, 3))
0
ͬ��Ҫ��float()��������������ֻ��Ҫʵ�����ⷽ��__float__()��
'''