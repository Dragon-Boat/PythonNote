#coding=utf-8
#author: sloop
'''
����
���� 3 ��forѭ�����б�����ʽ���ҳ��ԳƵ� 3 λ�������磬121 ���ǶԳ�������Ϊ���ҵ��󵹹������� 121��
'''

#����
print [100*a + 10*b + a for a in range(0,10) for b in range(1, 10)]

'''
print [a * 100 + b * 10 + c for a in range(1, 10) for b in range(0, 10) for c in range(0, 10) if a == c]
'''

'''
�����ʽ
forѭ������Ƕ�ף���ˣ����б�����ʽ�У�Ҳ�����ö�� for ѭ���������б�

�����ַ��� 'ABC' �� '123'������ʹ������ѭ��������ȫ���У�

>>> [m + n for m in 'ABC' for n in '123']
['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
�����ѭ�������������������

L = []
for m in 'ABC':
    for n in '123':
        L.append(m + n)
'''