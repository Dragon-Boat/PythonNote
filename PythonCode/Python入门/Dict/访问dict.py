#coding=utf-8
#author: sloop
'''
����
��������dict��

d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
���ӡ����

Adam: 95
Lisa: 85
Bart: 59
'''

#����
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
print 'Adam:',d.get('Adam')
print 'Lisa:',d.get('Lisa')
print 'Bart:',d.get('Bart')

'''
����dict
�����Ѿ��ܴ���һ��dict�����ڱ�ʾ���ֺͳɼ��Ķ�Ӧ��ϵ��

d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
��ô����θ������������Ҷ�Ӧ�ĳɼ��أ�

���Լ򵥵�ʹ�� d[key] ����ʽ�����Ҷ�Ӧ�� value����� list ���񣬲�֮ͬ���ǣ�list ����ʹ���������ض�Ӧ��Ԫ�أ���dictʹ��key��

>>> print d['Adam']
95
>>> print d['Paul']
Traceback (most recent call last):
  File "index.py", line 11, in <module>
    print d['Paul']
KeyError: 'Paul'
ע��: ͨ�� key ���� dict ��value��ֻҪ key ���ڣ�dict�ͷ��ض�Ӧ��value�����key�����ڣ���ֱ�ӱ���KeyError��

Ҫ���� KeyError �������������취��

һ�����ж�һ�� key �Ƿ���ڣ��� in ��������

if 'Paul' in d:
    print d['Paul']
��� 'Paul' �����ڣ�if����ж�ΪFalse����Ȼ����ִ�� print d['Paul'] ���Ӷ������˴���

����ʹ��dict�����ṩ��һ�� get ��������Key�����ڵ�ʱ�򣬷���None��

>>> print d.get('Bart')
59
>>> print d.get('Paul')
None
'''