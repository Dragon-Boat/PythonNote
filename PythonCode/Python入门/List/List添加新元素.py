#coding=utf-8
#author: sloop

'''
����
��������һ��ѧ��Paul��Paul ͬѧ�ĳɼ���Bart�ã����Ǳ�Lisa���Ӧ���ŵ���������λ�ã����ô���ʵ�֡�
'''

#����
L = ['Adam', 'Lisa', 'Bart']
L.insert(2,'Paul')
print L

'''
�����Ԫ��
���ڣ�������3��ͬѧ��

>>> L = ['Adam', 'Lisa', 'Bart']
���죬����ת��һ����ͬѧ Paul����ΰ���ͬѧ��ӵ����е� list ���أ�

��һ���취���� list �� append() ����������ͬѧ׷�ӵ� list ��ĩβ��

>>> L = ['Adam', 'Lisa', 'Bart']
>>> L.append('Paul')
>>> print L
['Adam', 'Lisa', 'Bart', 'Paul']
append()���ǰ��µ�Ԫ����ӵ� list ��β����

��� Paul ͬѧ��ʾ�Լ����ǿ����֣�Ҫ����ӵ���һ��λ�ã���ô�죿

��������list�� insert()������������������������һ�������������ţ��ڶ��������Ǵ���ӵ���Ԫ�أ�

>>> L = ['Adam', 'Lisa', 'Bart']
>>> L.insert(0, 'Paul')
>>> print L
['Paul', 'Adam', 'Lisa', 'Bart']
L.insert(0, 'Paul') ����˼�ǣ�'Paul'������ӵ�����Ϊ 0 ��λ���ϣ�Ҳ���ǵ�һ��������ԭ������Ϊ 0 ��Adamͬѧ���Լ����������ͬѧ�����Զ�����ƶ�һλ��
'''
