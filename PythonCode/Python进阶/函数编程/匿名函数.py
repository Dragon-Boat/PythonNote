#coding=utf-8
#author: sloop
'''
����
�����������������´��룺

def is_not_empty(s):
    return s and len(s.strip()) > 0
filter(is_not_empty, ['test', None, '', 'str', '  ', 'END'])
'''

print filter(lambda s : s and s.strip(), ['test', None, '', 'str', '  ', 'END'])

'''
print filter(lambda s : s and len(s.strip()) > 0, ['test', None, '', 'str', '  ', 'END'])
'''

'''
��������
�߽׺������Խ��պ�������������Щʱ�����ǲ���Ҫ��ʽ�ض��庯����ֱ�Ӵ����������������㡣

��Python�У������������ṩ������֧�֡�������map()����Ϊ�������� f(x)=x2 ʱ�����˶���һ��f(x)�ĺ����⣬������ֱ�Ӵ�������������

>>> map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])
[1, 4, 9, 16, 25, 36, 49, 64, 81]
ͨ���Աȿ��Կ������������� lambda x: x * x ʵ���Ͼ��ǣ�

def f(x):
    return x * x
�ؼ���lambda ��ʾ����������ð��ǰ��� x ��ʾ����������

���������и����ƣ�����ֻ����һ�����ʽ����дreturn������ֵ���Ǹñ��ʽ�Ľ����

ʹ���������������Բ��ض��庯������ֱ�Ӵ���һ���������󣬺ܶ�ʱ����Լ򻯴��룺

>>> sorted([1, 3, 9, 5, 0], lambda x,y: -cmp(x,y))
[9, 5, 3, 1, 0]
���غ�����ʱ��Ҳ���Է�������������

>>> myabs = lambda x: -x if x < 0 else x 
>>> myabs(-1)
1
>>> myabs(1)
1
'''