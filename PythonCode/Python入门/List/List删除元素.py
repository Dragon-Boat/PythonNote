#coding=utf-8
#author: sloop
'''
����
ע���ұ߱༭�������� list ���£�

L = ['Adam', 'Lisa', 'Paul', 'Bart']

Paul��������2��Bart��������3���������Ҫ��Paul��Bart��ɾ�������������Ĵ���Ϊʲô������ȷ���У�

L.pop(2)
L.pop(3)

��������������԰�Paul��Bart����ȷɾ������
'''

#����
L = ['Adam', 'Lisa', 'Paul', 'Bart']
L.pop(2)
L.pop(2)
print L

'''
��listɾ��Ԫ��
Paulͬѧ����������Ҫת���ˣ���ô������ô��Paul �����е�list��ɾ���أ�

���Paulͬѧ�������һ�������ǿ�����list��pop()����ɾ����

>>> L = ['Adam', 'Lisa', 'Bart', 'Paul']
>>> L.pop()
'Paul'
>>> print L
['Adam', 'Lisa', 'Bart']
pop()��������ɾ��list�����һ��Ԫ�أ����������������Ԫ�أ���������ִ�� L.pop() �󣬻��ӡ�� 'Paul'��

���Paulͬѧ�����������һ����ô�죿����Paulͬѧ���ڵ�����

>>> L = ['Adam', 'Lisa', 'Paul', 'Bart']
Ҫ��Paul�߳�list�����Ǿͱ����ȶ�λPaul��λ�á�����Paul��������2����ˣ��� pop(2)��Paulɾ����

>>> L.pop(2)
'Paul'
>>> print L
['Adam', 'Lisa', 'Bart']
'''