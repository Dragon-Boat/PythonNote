#coding=utf-8
#author: sloop
'''
����
���ַ�������ʱ����ʱ����Դ�Сд���������ϰ�ߡ�������sorted()�߽׺�����ʵ�ֺ��Դ�Сд������㷨��

���룺['bob', 'about', 'Zoo', 'Credit']
�����['about', 'bob', 'Credit', 'Zoo']
'''

def cmp_ignore_case(s1, s2):
    return -1 if s1.lower() < s2.lower() else 1

print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)

'''
def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0

def cmp_ignore_case(s1, s2):
    if s1[0].upper()>s2[0].upper():
        return 1
    return -1

def cmp_ignore_case(s1, s2):
    return cmp(s1.upper(),s2.upper())
'''

'''
�Զ���������
Python���õ� sorted()�����ɶ�list��������

>>>sorted([36, 5, 12, 9, 21])

[5, 9, 12, 21, 36]
�� sorted()Ҳ��һ���߽׺����������Խ���һ���ȽϺ�����ʵ���Զ������򣬱ȽϺ����Ķ����ǣ������������Ƚϵ�Ԫ�� x, y����� x Ӧ������ y ��ǰ�棬���� -1����� x Ӧ������ y �ĺ��棬���� 1����� x �� y ��ȣ����� 0��

��ˣ��������Ҫʵ�ֵ�������ֻ��Ҫ��дһ��reversed_cmp������

def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0
���������� sorted() ������ reversed_cmp �Ϳ���ʵ�ֵ�������

>>> sorted([36, 5, 12, 9, 21], reversed_cmp)
[36, 21, 12, 9, 5]
sorted()Ҳ���Զ��ַ������������ַ���Ĭ�ϰ���ASCII��С���Ƚϣ�

>>> sorted(['bob', 'about', 'Zoo', 'Credit'])
['Credit', 'Zoo', 'about', 'bob']
'Zoo'����'about'֮ǰ����Ϊ'Z'��ASCII���'a'С��
'''