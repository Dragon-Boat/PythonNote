#coding=utf-8
#author: sloop

'''
����
��������set����ʶ��Сд�����֣���Ľ�set��ʹ�� 'adam' �� 'bart'���ܷ���True��
'''

#����
s = set(['Adam', 'Lisa', 'Bart', 'Paul'])
temp = set()
for k in s:
    l = k.lower()
    temp.add(l)
for k in temp:
    s.add(k)
print 'adam' in s
print 'bart' in s
print s

'''
����set
����set�洢�������򼯺ϣ���������û��ͨ�����������ʡ�

���� set�е�ĳ��Ԫ��ʵ���Ͼ����ж�һ��Ԫ���Ƿ���set�С�

���磬�洢�˰���ͬѧ���ֵ�set��

>>> s = set(['Adam', 'Lisa', 'Bart', 'Paul'])
���ǿ����� in �������жϣ�

Bart�Ǹð��ͬѧ��

>>> 'Bart' in s
True
Bill�Ǹð��ͬѧ��

>>> 'Bill' in s
False
bart�Ǹð��ͬѧ��

>>> 'bart' in s
False
������Сд����Ҫ��'Bart' �� 'bart'����Ϊ��������ͬ��Ԫ�ء�
'''