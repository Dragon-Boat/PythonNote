#coding=utf-8
#author: sloop

'''
����
���� for ѭ���������µ�set����ӡ�� name: score ����

s = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])
'''

#����
s = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])
for x in s:
    print x[0],':',x[1]


'''
����set
���� set Ҳ��һ�����ϣ����ԣ����� set �ͱ��� list ���ƣ�������ͨ�� for ѭ��ʵ�֡�

ֱ��ʹ�� for ѭ�����Ա��� set ��Ԫ�أ�

>>> s = set(['Adam', 'Lisa', 'Bart'])
>>> for name in s:
...     print name
... 
Lisa
Adam
Bart
ע��: �۲� for ѭ���ڱ���setʱ��Ԫ�ص�˳���list��˳��ܿ����ǲ�ͬ�ģ����Ҳ�ͬ�Ļ��������еĽ��Ҳ���ܲ�ͬ��
'''