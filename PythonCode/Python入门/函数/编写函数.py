#coding=utf-8
#author: sloop
'''
����
�붨��һ�� square_of_sum ������������һ��list������list��ÿ��Ԫ��ƽ���ĺ͡�
'''

#����
def square_of_sum(L):
    return sum(i*i for i in L)

print square_of_sum([1, 2, 3, 4, 5])
print square_of_sum([-5, 0, 5, 15, 25])


'''
def square_of_sum(L):
    sum = 0
    for x in L:
        sum = sum + x * x
    return sum
'''

'''
��д����
��Python�У�����һ������Ҫʹ�� def ��䣬����д�������������š������еĲ�����ð��:��Ȼ�����������б�д�����壬�����ķ���ֵ�� return ��䷵�ء�

�������Զ���һ�������ֵ�� my_abs ����Ϊ����

def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
��ע�⣬�������ڲ��������ִ��ʱ��һ��ִ�е�returnʱ��������ִ����ϣ�����������ء���ˣ������ڲ�ͨ�������жϺ�ѭ������ʵ�ַǳ����ӵ��߼���

���û��return��䣬����ִ����Ϻ�Ҳ�᷵�ؽ����ֻ�ǽ��Ϊ None��

return None���Լ�дΪreturn��
'''