#coding=utf-8
#author: sloop
'''
����
���д���ܿɱ������ average() ������
'''
#����
def average(*args):
    s = sum(args)*1.0           #��
    l = len(args)               #����
    return 0.0 if l==0 else s/l #ƽ��ֵ

print average()
print average(1, 2)
print average(1, 2, 2, 3, 4)

'''
def average(*args):
    return 0.0 if len(args)==0 else sum(args)*1.0/len(args)
'''

'''
����ɱ����
�������һ�������ܽ�����������������ǾͿ��Զ���һ���ɱ������

def fn(*args):
    print args
�ɱ����������ǰ���и� * �ţ����ǿ��Դ���0����1�������������ɱ������

>>> fn()
()
>>> fn('a')
('a',)
>>> fn('a', 'b')
('a', 'b')
>>> fn('a', 'b', 'c')
('a', 'b', 'c')
�ɱ����Ҳ���Ǻ����أ�Python��������Ѵ����һ�������װ��һ��tuple���ݸ��ɱ��������ˣ��ں����ڲ���ֱ�Ӱѱ��� args ����һ�� tuple �ͺ��ˡ�

����ɱ������Ŀ��Ҳ��Ϊ�˼򻯵��á���������Ҫ�������������ƽ��ֵ���Ϳ��Զ���һ���ɱ������

def average(*args):
    ...
�������ڵ��õ�ʱ�򣬿�������д��

>>> average()
0
>>> average(1, 2)
1.5
>>> average(1, 2, 2, 3, 4)
2.4
'''