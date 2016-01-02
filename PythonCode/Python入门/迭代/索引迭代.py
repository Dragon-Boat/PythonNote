#coding=utf-8
#author: sloop
'''
����
zip()�������԰����� list ���һ�� list��

>>> zip([10, 20, 30], ['A', 'B', 'C'])
[(10, 'A'), (20, 'B'), (30, 'C')]
�ڵ��� ['Adam', 'Lisa', 'Bart', 'Paul'] ʱ������������ӡ������ - ���֣����δ�1��ʼ)���뿼������ڵ����д�ӡ������

��ʾ������ʹ��zip()������range()����
'''

#����
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for index, name in zip(range(1,len(L)+1),L):
    print index, '-', name

'''
��������
Python�У�������Զ��ȡ��Ԫ�ر�������Ԫ�ص�������

�������򼯺ϣ�Ԫ��ȷʵ���������ġ��е�ʱ������ȷʵ���� for ѭ�����õ���������ô�죿

������ʹ�� enumerate() ������

>>> L = ['Adam', 'Lisa', 'Bart', 'Paul']
>>> for index, name in enumerate(L):
...     print index, '-', name
... 
0 - Adam
1 - Lisa
2 - Bart
3 - Paul
ʹ�� enumerate() ���������ǿ�����forѭ����ͬʱ������index��Ԫ��name�����ǣ��ⲻ�� enumerate() �������﷨��ʵ���ϣ�enumerate() �����ѣ�

['Adam', 'Lisa', 'Bart', 'Paul']
��������ƣ�

[(0, 'Adam'), (1, 'Lisa'), (2, 'Bart'), (3, 'Paul')]
��ˣ�������ÿһ��Ԫ��ʵ������һ��tuple��

for t in enumerate(L):
    index = t[0]
    name = t[1]
    print index, '-', name
�������֪��ÿ��tupleԪ�ض���������Ԫ�أ�forѭ���ֿ��Խ�һ����дΪ��

for index, name in enumerate(L):
    print index, '-', name
��������������򵥣����һ�����������ֵ��䡣

�ɼ�����������Ҳ������İ��������ʣ������� enumerate() �����Զ���ÿ��Ԫ�ر�� (index, element) ������tuple���ٵ�������ͬʱ�����������Ԫ�ر���
'''