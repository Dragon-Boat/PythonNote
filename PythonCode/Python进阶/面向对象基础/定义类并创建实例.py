#coding=utf-8
#author: sloop
'''
����
����ϰ����Person�࣬������������ʵ������ӡʵ�����ٱȽ�����ʵ���Ƿ���ȡ�
'''

class Person(object):
    pass

xiaoming = Person()
xiaohong = Person()

print xiaoming
print xiaohong
print xiaoming == xiaohong

'''
�����ಢ����ʵ��
��Python�У���ͨ�� class �ؼ��ֶ��塣�� Person Ϊ��������һ��Person�����£�

class Person(object):
    pass
���� Python �ı��ϰ�ߣ������Դ�д��ĸ��ͷ����������(object)����ʾ�����Ǵ��ĸ���̳������ġ���ļ̳н��ں�����½ڽ��⣬��������ֻ��Ҫ�򵥵ش�object��̳С�

����Person��Ķ��壬�Ϳ��Դ����������xiaoming��xiaohong��ʵ��������ʵ��ʹ�� ����+()�����ƺ������õ���ʽ������

xiaoming = Person()
xiaohong = Person()
'''