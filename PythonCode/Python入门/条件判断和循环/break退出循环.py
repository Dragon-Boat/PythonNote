#coding=utf-8
#author: sloop
'''
����
���� while True ����ѭ����� break ��䣬���� 1 + 2 + 4 + 8 + 16 + ... ��ǰ20��ĺ͡�
'''

#����
sum = 0
x = 1
n = 1
while True:
    sum+=x
    x*=2
    n+=1
    if n>20:
        break
print sum

'''
break�˳�ѭ��
�� for ѭ������ while ѭ��ʱ�����Ҫ��ѭ������ֱ���˳�ѭ��������ʹ�� break ��䡣

�������1��100�������ͣ�������while��ʵ�֣�

sum = 0
x = 1
while True:
    sum = sum + x
    x = x + 1
    if x > 100:
        break
print sum
զһ���� while True ����һ����ѭ����������ѭ�����ڣ����ǻ��ж��� x > 100 ��������ʱ����break����˳�ѭ��������Ҳ����ʵ��ѭ���Ľ�����
'''