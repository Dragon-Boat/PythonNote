#coding=utf-8
#author: sloop
'''
����
������filter()���˳�1~100��ƽ���������������������Ӧ���ǣ�

[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
'''

import math
def is_sqr(x):
    return math.sqrt(x)%1 == 0

print filter(is_sqr, range(1, 101))

'''
is_sqr����ʵ�ַ�ʽ
def is_sqr(x):
    r = int(math.sqrt(x))
    return r*r==x

def is_sqr(x):
    return math.sqrt(x)- int(math.sqrt(x)) == 0

 def is_sqr(x):
    math.modf( math.sqrt(x) )[0] != 0.0
 
def is_sqr(x):
    return x==int(math.sqrt(x))**2
'''

'''
filter()����
filter()������ Python ���õ���һ�����õĸ߽׺�����filter()��������һ������ f ��һ��list��������� f �������Ƕ�ÿ��Ԫ�ؽ����жϣ����� True�� False��filter()�����жϽ���Զ����˵�������������Ԫ�أ������ɷ�������Ԫ����ɵ���list��

���磬Ҫ��һ��list [1, 4, 6, 7, 9, 12, 17]��ɾ��ż�����������������ȣ�Ҫ��дһ���ж������ĺ�����

def is_odd(x):
    return x % 2 == 1
Ȼ������filter()���˵�ż����

filter(is_odd, [1, 4, 6, 7, 9, 12, 17])
�����[1, 7, 9, 17]

����filter()��������ɺܶ����õĹ��ܣ����磬ɾ�� None ���߿��ַ�����

def is_not_empty(s):
    return s and len(s.strip()) > 0
filter(is_not_empty, ['test', None, '', 'str', '  ', 'END'])
�����['test', 'str', 'END']

ע��: s.strip(rm) ɾ�� s �ַ����п�ͷ����β���� rm ���е��ַ���

��rmΪ��ʱ��Ĭ��ɾ���հ׷�������'\n', '\r', '\t', ' ')�����£�

a = '     123'
a.strip()
����� '123'

a='\t\t123\r\n'
a.strip()
�����'123'
'''