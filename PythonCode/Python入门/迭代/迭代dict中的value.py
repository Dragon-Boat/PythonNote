#coding=utf-8
#author: sloop
'''
����
����һ��dict��

d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }

���������ͬѧ��ƽ���֡�
'''

#����
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }

sum = 0.0
for i in d.itervalues():
    sum += i
print sum/len(d)

'''
����dict��value
�����Ѿ��˽���dict��������ǿɵ��������� for ѭ��ֱ�ӵ��� dict������ÿ���õ�dict��һ��key��

�������ϣ������ dict �����value��Ӧ����ô����

dict ������һ�� values() ���������������dictת����һ����������value��list�����������ǵ����ľ��� dict��ÿһ�� value��

d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
print d.values()
# [85, 95, 59]
for v in d.values():
    print v
# 85
# 95
# 59
�����ϸ�Ķ�Python���ĵ��������Է��֣�dict����values()�����⣬����һ�� itervalues() �������� itervalues() ������� values() ����������Ч����ȫһ����

d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
print d.itervalues()
# <dictionary-valueiterator object at 0x106adbb50>
for v in d.itervalues():
    print v
# 85
# 95
# 59
�������������кβ�֮ͬ���أ�

1. values() ����ʵ���ϰ�һ�� dict ת�����˰��� value ��list��

2. ���� itervalues() ��������ת���������ڵ������������δ� dict ��ȡ�� value������ itervalues() ������ values() ������ʡ������ list ������ڴ档

3. ��ӡ itervalues() ����������һ�� <dictionary-valueiterator> ������˵����Python�У�for ѭ�������õĵ�������Զ��ֹ list��tuple��str��unicode��dict�ȣ��κοɵ������󶼿���������forѭ�������ڲ���ε�������ͨ�������ù��ġ�

���һ������˵�Լ��ɵ����������Ǿ�ֱ���� for ѭ��ȥ���������ɼ���������һ�ֳ�������ݲ����������Ե��������ڲ����������κ�Ҫ��
'''