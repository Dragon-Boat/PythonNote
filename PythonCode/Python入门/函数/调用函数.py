#coding=utf-8
#author: sloop
'''
����
sum()��������һ��list��Ϊ������������list����Ԫ��֮�͡������ 1*1 + 2*2 + 3*3 + ... + 100*100��
'''

#����
L = [i*i for i in range(1,101)]
print sum(L)

'''
L = []
i=1
while i <= 100:
    L.append(i*i)
    i+=1
print sum(L)
'''

'''
���ú���
Python�����˺ܶ����õĺ��������ǿ���ֱ�ӵ��á�

Ҫ����һ����������Ҫ֪�����������ƺͲ��������������ֵ�ĺ��� abs��������һ��������

����ֱ�Ӵ�Python�Ĺٷ���վ�鿴�ĵ���
http://docs.python.org/2/library/functions.html#abs
Ҳ�����ڽ���ʽ������ͨ�� help(abs) �鿴abs�����İ�����Ϣ��

���� abs ������

>>> abs(100)
100
>>> abs(-20)
20
>>> abs(12.34)
12.34
���ú�����ʱ���������Ĳ����������ԣ��ᱨTypeError�Ĵ��󣬲���Python����ȷ�ظ����㣺abs()���ҽ���1����������������������

>>> abs(1, 2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: abs() takes exactly one argument (2 given)
�������Ĳ��������ǶԵģ����������Ͳ��ܱ����������ܣ�Ҳ�ᱨTypeError�Ĵ��󣬲��Ҹ���������Ϣ��str�Ǵ���Ĳ������ͣ�

>>> abs('a')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: bad operand type for abs(): 'str'
���ȽϺ��� cmp(x, y) ����Ҫ������������� x<y������ -1����� x==y������ 0����� x>y������ 1��

>>> cmp(1, 2)
-1
>>> cmp(2, 1)
1
>>> cmp(3, 3)
0
Python���õĳ��ú�����������������ת������������   int()�������԰�������������ת��Ϊ������

>>> int('123')
123
>>> int(12.34)
12
str()��������������ת���� str��

>>> str(123)
'123'
>>> str(1.23)
'1.23'
'''