#coding=utf-8
#author: sloop
'''
����
�����еļ��� 0 - 100 ��whileѭ�����и��죬ͨ������ continue ��䣬ʹ��ֻ���������ĺͣ�

sum = 0
x = 1
while True:
    sum = sum + x
    x = x + 1
    if x > 100:
        break
print sum
'''

#����
sum = 0
x = 0
while True:
    x = x + 1
    if x > 100:
        break
    if x%2==0:
        continue
    sum+=x
print sum

'''
continue����ѭ��
��ѭ�������У�������break�˳���ǰѭ������������continue��������ѭ�����룬������һ��ѭ����

���������Ѿ�д��������forѭ������ƽ���ֵĴ��룺

L = [75, 98, 59, 81, 66, 43, 69, 85]
sum = 0.0
n = 0
for x in L:
    sum = sum + x
    n = n + 1
print sum / n
������ʦֻ��ͳ�Ƽ��������ƽ���֣���Ҫ�� x < 60 �ķ����޳�������ʱ������ continue������������ x < 60��ʱ�򣬲�����ִ��ѭ����ĺ������룬ֱ�ӽ�����һ��ѭ����

for x in L:
    if x < 60:
        continue
    sum = sum + x
    n = n + 1
'''