#coding=utf-8
#author: sloop
'''
����
�����dict��

d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }

��ӡ�� name : score������ٴ�ӡ��ƽ���� average : score��
'''

#����
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }

sum = 0.0
for k, v in d.items():
    sum = sum + v
    print k,':',v
print 'average', ':', sum/len(d)

'''
����dict��key��value
�����˽�����ε��� dict ��key��value����ô����һ�� for ѭ���У��ܷ�ͬʱ���� key��value�����ǿ϶��ġ�

���ȣ����ǿ��� dict ����� items() �������ص�ֵ��

>>> d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
>>> print d.items()
[('Lisa', 85), ('Adam', 95), ('Bart', 59)]
���Կ�����items() ������dict����ת�����˰���tuple��list�����Ƕ����list���е���������ͬʱ���key��value��

>>> for key, value in d.items():
...     print key, ':', value
... 
Lisa : 85
Adam : 95
Bart : 59
�� values() ��һ�� itervalues() ���ƣ� items() Ҳ��һ����Ӧ�� iteritems()��iteritems() ����dictת����list�������ڵ��������в��ϸ��� tuple�����ԣ� iteritems() ��ռ�ö�����ڴ档
'''