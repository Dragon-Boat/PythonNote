#coding=utf-8
#author: sloop
'''
����
��Python 3.x�У��ַ���ͳһΪunicode������Ҫ��ǰ׺ u�������ֽڴ洢��str������ǰ׺ b��������__future__��unicode_literals��Python 2.7�б�дunicode�ַ�����
'''

from __future__ import unicode_literals

s = 'am I an unicode?'
print isinstance(s, unicode)

'''
ʹ��__future__
Python���°汾�������µĹ��ܣ����ǣ�ʵ������Щ��������һ���ϰ汾�о��Ѿ������ˡ�Ҫ�����á�ĳһ�µ����ԣ��Ϳ���ͨ������__future__ģ���ĳЩ������ʵ�֡�

���磬Python 2.7��������������������������

>>> 10 / 3
3
���ǣ�Python 3.x�Ѿ��Ľ��������ĳ������㣬��/�������õ�����������//����������������

>>> 10 / 3
3.3333333333333335
>>> 10 // 3
3
Ҫ��Python 2.7������3.x�ĳ������򣬵���__future__��division��

>>> from __future__ import division
>>> print 10 / 3
3.3333333333333335
���°汾��һ��������ɰ汾������ʱ�������Խ����ھɰ汾����ӵ�__future__�У��Ա�ɵĴ������ھɰ汾�в��������ԡ�
'''