#coding=utf-8
#author: sloop
'''
����
�ַ����и����� upper() ���԰��ַ���ɴ�д��ĸ��

>>> 'abc'.upper()
'ABC'
�������������ĸ����ɴ�д�������һ��������������һ���ַ�����Ȼ�󷵻�һ��������ĸ��ɴ�д���ַ�����

��ʾ��������Ƭ�������ַ���������
'''

#����
def firstCharUpper(s):
    return s[:1].upper()+s[1:]

print firstCharUpper('hello')
print firstCharUpper('sunday')
print firstCharUpper('september')

'''
���ַ�����Ƭ
�ַ��� 'xxx'�� Unicode�ַ��� u'xxx'Ҳ���Կ�����һ��list��ÿ��Ԫ�ؾ���һ���ַ�����ˣ��ַ���Ҳ��������Ƭ������ֻ�ǲ�����������ַ�����

>>> 'ABCDEFG'[:3]
'ABC'
>>> 'ABCDEFG'[-3:]
'EFG'
>>> 'ABCDEFG'[::2]
'ACEG'
�ںܶ��������У�����ַ����ṩ�˺ܶ���ֽ�ȡ��������ʵĿ�ľ��Ƕ��ַ�����Ƭ��Pythonû������ַ����Ľ�ȡ������ֻ��Ҫ��Ƭһ�������Ϳ�����ɣ��ǳ��򵥡�
'''