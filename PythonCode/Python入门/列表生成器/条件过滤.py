#coding=utf-8
#author: sloop
'''
����
���дһ��������������һ�� list��Ȼ���list�е������ַ�����ɴ�д�󷵻أ����ַ���Ԫ�ؽ������ԡ�

��ʾ��

1. isinstance(x, str) �����жϱ��� x �Ƿ����ַ�����

2. �ַ����� upper() �������Է��ش�д����ĸ��
'''

#����
def toUppers(L):
    return [i.upper() for i in L if isinstance(i, str) ]

print toUppers(['Hello', 'world', 101])

'''
��������
�б�����ʽ�� for ѭ�����滹���Լ��� if �жϡ����磺

>>> [x * x for x in range(1, 11)]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
�������ֻ��Ҫż����ƽ�������Ķ� range()������£����Լ��� if ��ɸѡ��

>>> [x * x for x in range(1, 11) if x % 2 == 0]
[4, 16, 36, 64, 100]
���� if ������ֻ�� if �ж�Ϊ True ��ʱ�򣬲Ű�ѭ���ĵ�ǰԪ����ӵ��б��С�
'''