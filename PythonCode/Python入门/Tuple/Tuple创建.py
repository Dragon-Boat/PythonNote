#coding=utf-8
#author: sloop

'''
����
����һ��tuple��˳�����0 - 9��10������
'''

#����
t = (0,1,2,3,4,5,6,7,8,9)
print t

'''
����tuple
tuple����һ��������б����ķ���Ϊ�� Ԫ�� ����tuple �� list �ǳ����ƣ����ǣ�tupleһ��������ϣ��Ͳ����޸��ˡ�

ͬ���Ǳ�ʾ����ͬѧ�����ƣ���tuple��ʾ���£�

>>> t = ('Adam', 'Lisa', 'Bart')
����tuple�ʹ���listΨһ��֮ͬ������( )�����[ ]��

���ڣ���� t �Ͳ��ܸı��ˣ�tupleû�� append()������Ҳû��insert()��pop()���������ԣ���ͬѧû��ֱ���� tuple ����ӣ���ͬѧ���˳� tuple Ҳ���С�

��ȡ tuple Ԫ�صķ�ʽ�� list ��һģһ���ģ����ǿ�������ʹ�� t[0]��t[-1]��������ʽ����Ԫ�أ����ǲ��ܸ�ֵ�ɱ��Ԫ�أ����ſ������ԣ�

>>> t[0] = 'Paul'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
'''