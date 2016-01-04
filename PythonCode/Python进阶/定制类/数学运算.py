#coding=utf-8
#author: sloop
# ��������
'''
����
Rational����Ȼ�������ӷ������޷����������˷��ͳ��������������Rational�࣬ʵ���������㡣

��ʾ��
�������㣺__sub__
�˷����㣺__mul__
�������㣺__div__
'''

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __add__(self, r):
        return Rational(self.p * r.q + self.q * r.p, self.q * r.q)

    def __sub__(self, r):
        return Rational(self.p*r.q - r.p*self.q, self.q*r.q)

    def __mul__(self, r):
        return Rational(self.p*r.p, self.q*r.q)

    def __div__(self, r):
        return Rational(self.p*r.q, self.q*r.p)

    def __str__(self):
        g = gcd(self.p, self.q) 
        return '%s/%s' %(self.p/g, self.q/g)

    __repr__ = __str__

r1 = Rational(1, 2)
r2 = Rational(1, 4)
print r1 + r2
print r1 - r2
print r1 * r2
print r1 / r2

'''
��ѧ����
Python �ṩ�Ļ����������� int��float �����������͸�������������Լ��˷������㡣

���ǣ��������㲻������int��float����������������������ȡ�

Ҫ��ʾ��������������һ��Rational������ʾ��

class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q
p��q ������������ʾ������ p/q��

���Ҫ��Rational����+���㣬��Ҫ��ȷʵ��__add__��

class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q
    def __add__(self, r):
        return Rational(self.p * r.q + self.q * r.p, self.q * r.q)
    def __str__(self):
        return '%s/%s' % (self.p, self.q)
    __repr__ = __str__
���ڿ��������������ӷ���

>>> r1 = Rational(1, 3)
>>> r2 = Rational(1, 2)
>>> print r1 + r2
5/6
'''