#coding=utf-8
#author: sloop

'''
����쳲�������
�������: ����
'''
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))

for i in range(1, 20):
    print factorial(i)