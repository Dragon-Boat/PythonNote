#coding=utf-8
#author: sloop

'''
����
�����Paul�ĳɼ� 72 ���������dict��

d = {
    95: 'Adam',
    85: 'Lisa',
    59: 'Bart'
}
'''

#����
d = {
    95: 'Adam',
    85: 'Lisa',
    59: 'Bart'
}
d[72]='Paul'
print d

'''
����dict
dict�ǿɱ�ģ�Ҳ����˵�����ǿ�����ʱ��dict������µ� key-value����������dict��

d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
Ҫ����ͬѧ'Paul'�ĳɼ� 72 �ӽ�ȥ���ø�ֵ��䣺

>>> d['Paul'] = 72
�ٿ���dict�����ݣ�

>>> print d
{'Lisa': 85, 'Paul': 72, 'Adam': 95, 'Bart': 59}
��� key �Ѿ����ڣ���ֵ�����µ� value �滻��ԭ���� value��

>>> d['Bart'] = 60
>>> print d
{'Lisa': 85, 'Paul': 72, 'Adam': 95, 'Bart': 60}
'''