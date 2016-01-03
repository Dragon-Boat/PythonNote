#coding=utf-8
#author: sloop
'''
����
���дһ������calc_prod(lst)��������һ��list������һ�����������غ������Լ�������ĳ˻���
'''

def calc_prod(lst):
    def prod(x, y):
        return x*y
    def lazy_prod():
        return reduce(prod,lst)
    return lazy_prod

f = calc_prod([1, 2, 3, 4])
print f()

'''
����ʵ�ַ�ʽ

�ȶ����ܼ���˻��ĺ������ٽ��˺������ء�

�ο�����:

def calc_prod(lst):
    def lazy_prod():
        def f(x, y):
            return x * y
        return reduce(f, lst, 1)
    return lazy_prod
f = calc_prod([1, 2, 3, 4])
print f()


def calc_prod(lst):
    def sum_list():
        return reduce((lambda x, y:x * y),lst)
    return sum_list

f = calc_prod([1, 2, 3, 4])
print f()
'''

'''
���غ���
Python�ĺ����������Է���int��str��list��dict���������ͣ������Է��غ�����

���磬����һ������ f()��������������һ������ g����������д��

def f():
    print 'call f()...'
    # ���庯��g:
    def g():
        print 'call g()...'
    # ���غ���g:
    return g
��ϸ�۲�����ĺ������壬�����ں��� f �ڲ��ֶ�����һ������ g�����ں��� g Ҳ��һ�����󣬺����� g ����ָ���� g �ı��������ԣ�����㺯�� f ���Է��ر��� g��Ҳ���Ǻ��� g ����

���ú��� f�����ǻ�õ� f ���ص�һ��������

>>> x = f()   # ����f()
call f()...
>>> x   # ����x��f()���صĺ�����
<function g at 0x1037bf320>
>>> x()   # xָ��������˿��Ե���
call g()...   # ����x()����ִ��g()��������Ĵ���
��ע�����ַ��غ����ͷ���ֵ��

def myabs():
    return abs   # ���غ���
def myabs2(x):
    return abs(x)   # ���غ������õĽ��������ֵ��һ����ֵ
���غ������԰�һЩ�����ӳ�ִ�С����磬�������һ����ͨ����ͺ�����

def calc_sum(lst):
    return sum(lst)
����calc_sum()����ʱ�������̼��㲢�õ������

>>> calc_sum([1, 2, 3, 4])
10
���ǣ��������һ���������Ϳ��ԡ��ӳټ��㡱��

def calc_sum(lst):
    def lazy_sum():
        return sum(lst)
    return lazy_sum
# ����calc_sum()��û�м������������Ƿ��غ���:

>>> f = calc_sum([1, 2, 3, 4])
>>> f
<function lazy_sum at 0x1037bfaa0>
# �Է��صĺ������е���ʱ���ż�������:

>>> f()
10
���ڿ��Է��غ����������ں���������Ϳ��Ծ�������Ҫ��Ҫ���øú�����
'''