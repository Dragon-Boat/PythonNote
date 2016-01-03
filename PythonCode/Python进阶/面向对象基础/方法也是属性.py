#coding=utf-8
#author: sloop
'''
����
�������Կ�������ͨ��ֵ������ str��int �ȣ�Ҳ�����Ƿ������������Ǻ�������ҿ��������������н��������һ�� p1.get_grade Ϊʲô�Ǻ��������Ƿ�����
'''

class Person(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.get_grade = lambda: 'A'

p1 = Person('Bob', 90)
print p1.get_grade
print p1.get_grade()


'''
����Ҳ������
������ class �ж����ʵ��������ʵҲ�����ԣ���ʵ������һ����������

class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
        return 'A'

p1 = Person('Bob', 90)
print p1.get_grade
# => <bound method Person.get_grade of <__main__.Person object at 0x109e58510>>
print p1.get_grade()
# => A
Ҳ����˵��p1.get_grade ���ص���һ���������󣬵����������һ���󶨵�ʵ���ĺ�����p1.get_grade() ���Ƿ������á�

��Ϊ����Ҳ��һ�����ԣ����ԣ���Ҳ���Զ�̬����ӵ�ʵ���ϣ�ֻ����Ҫ�� types.MethodType() ��һ��������Ϊһ��������

import types
def fn_get_grade(self):
    if self.score >= 80:
        return 'A'
    if self.score >= 60:
        return 'B'
    return 'C'

class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

p1 = Person('Bob', 90)
p1.get_grade = types.MethodType(fn_get_grade, p1, Person)
print p1.get_grade()
# => A
p2 = Person('Alice', 65)
print p2.get_grade()
# ERROR: AttributeError: 'Person' object has no attribute 'get_grade'
# ��Ϊp2ʵ����û�а�get_grade
��һ��ʵ����̬��ӷ�������������ֱ����class�ж���Ҫ��ֱ�ۡ�
'''