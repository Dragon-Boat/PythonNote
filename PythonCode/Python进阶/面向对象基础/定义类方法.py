#coding=utf-8
#author: sloop
'''
����
����������� count ��Ϊ˽������__count�����ⲿ�޷���ȡ__score��������ͨ��һ���෽����ȡ�����д�෽�����__countֵ��
'''

class Person(object):
    __count = 0

    @classmethod
    def how_many(cls):
        return cls.__count
    
    def __init__(self, name):
        self.name = name
        Person.__count += 1

print Person.how_many()
p1 = Person('Bob')
print Person.how_many()

'''
�����෽��
���������ƣ�����Ҳ��ʵ���������෽����

��class�ж����ȫ����ʵ��������ʵ��������һ������ self ��ʵ������

Ҫ��class�ж����෽������Ҫ��ôд��

class Person(object):
    count = 0
    @classmethod
    def how_many(cls):
        return cls.count
    def __init__(self, name):
        self.name = name
        Person.count = Person.count + 1

print Person.how_many()
p1 = Person('Bob')
print Person.how_many()
ͨ�����һ�� @classmethod���÷������󶨵� Person ���ϣ��������ʵ�����෽���ĵ�һ�������������౾��ͨ��������������Ϊ cls������� cls.count ʵ�����൱�� Person.count��

��Ϊ�������ϵ��ã�����ʵ���ϵ��ã�����෽���޷�����κ�ʵ��������ֻ�ܻ��������á�
'''