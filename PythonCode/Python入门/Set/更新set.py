#coding=utf-8
#author: sloop
'''
����
��������set������һ��list����list�е�ÿһ��Ԫ�أ������set�У��ͽ���ɾ�����������set�У�����ӽ�ȥ��

s = set(['Adam', 'Paul'])
L = ['Adam', 'Lisa', 'Bart', 'Paul']
'''

#����
s = set(['Adam', 'Lisa', 'Paul'])
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for k in L:
    if k in s:
        s.remove(k)
    else:
        s.add(k)
print s

'''
����set
����set�洢����һ�鲻�ظ�������Ԫ�أ���ˣ�����set��Ҫ�������£�

һ�ǰ��µ�Ԫ����ӵ�set�У����ǰ�����Ԫ�ش�set��ɾ����

���Ԫ��ʱ����set��add()������

>>> s = set([1, 2, 3])
>>> s.add(4)
>>> print s
set([1, 2, 3, 4])
�����ӵ�Ԫ���Ѿ�������set�У�add()���ᱨ�����ǲ���ӽ�ȥ�ˣ�

>>> s = set([1, 2, 3])
>>> s.add(3)
>>> print s
set([1, 2, 3])
ɾ��set�е�Ԫ��ʱ����set��remove()������

>>> s = set([1, 2, 3, 4])
>>> s.remove(4)
>>> print s
set([1, 2, 3])
���ɾ����Ԫ�ز�����set�У�remove()�ᱨ��

>>> s = set([1, 2, 3])
>>> s.remove(4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 4
������add()����ֱ����ӣ���remove()ǰ��Ҫ�жϡ�
'''