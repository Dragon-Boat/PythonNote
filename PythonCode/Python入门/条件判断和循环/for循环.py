#coding=utf-8
#author: sloop
'''
����
���￼�Ժ���ʦҪͳ��ƽ���ɼ�����֪4λͬѧ�ĳɼ���list��ʾ���£�

L = [75, 92, 59, 68]

������forѭ�������ƽ���ɼ���
'''

#����
L = [75, 92, 59, 68]
sum = 0.0
for score in L:
    sum+=score
print sum / 4

'''
forѭ��
list��tuple���Ա�ʾһ�����򼯺ϡ�������������η���һ��list�е�ÿһ��Ԫ���أ����� list��

L = ['Adam', 'Lisa', 'Bart']
print L[0]
print L[1]
print L[2]
���listֻ��������Ԫ�أ�����д���У����list����1���Ԫ�أ����ǾͲ�����д1����print��

��ʱ��ѭ���������ó��ˡ�

Python�� for ѭ���Ϳ������ΰ�list��tuple��ÿ��Ԫ�ص���������

L = ['Adam', 'Lisa', 'Bart']
for name in L:
    print name
ע��:  name ����������� for ѭ���ж���ģ���˼�ǣ�����ȡ��list�е�ÿһ��Ԫ�أ�����Ԫ�ظ�ֵ�� name��Ȼ��ִ��forѭ���壨���������Ĵ���飩��

����һ��������һ��list��tuple�ͷǳ������ˡ�
'''