#coding=utf-8
#author: sloop
'''
����
��� Person ������һ��˽������ __score����ʾ������������һ��ʵ������ get_grade()���ܸ��� __score ��ֵ�ֱ𷵻� A-����, B-����, C-������������
'''

class Person(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_grade(self):
        if self.__score > 80:
            return 'A'
        if self.__score >= 60:
            return 'B'
        return 'C'

p1 = Person('Bob', 90)
p2 = Person('Alice', 65)
p3 = Person('Tim', 48)

print p1.get_grade()
print p2.get_grade()
print p3.get_grade()

'''
����ʵ������
һ��ʵ����˽�����Ծ�����__��ͷ�����ԣ��޷����ⲿ���ʣ�����Щ���Զ�����ʲô�ã�

��Ȼ˽�������޷����ⲿ���ʣ����ǣ�������ڲ��ǿ��Է��ʵġ����˿��Զ���ʵ���������⣬�����Զ���ʵ���ķ�����

ʵ���ķ������������ж���ĺ��������ĵ�һ��������Զ�� self��ָ����ø÷�����ʵ����������������һ����ͨ��������ȫһ���ģ�

class Person(object):

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name
get_name(self) ����һ��ʵ�����������ĵ�һ��������self��__init__(self, name)��ʵҲ�ɿ�����һ�������ʵ��������

����ʵ������������ʵ���ϵ��ã�

p1 = Person('Bob')
print p1.get_name()  # self����Ҫ��ʽ����
# => Bob
��ʵ�������ڲ������Է�������ʵ�����ԣ�����������ⲿ��Ҫ����˽�����ԣ�����ͨ���������û�ã��������ݷ�װ����ʽ�����ܱ����ڲ�����һ�����⣬�����Լ��ⲿ���õ��Ѷ�
'''