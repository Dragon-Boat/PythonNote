#coding=utf-8
#author: sloop
'''
����
��ο� Student �࣬��дһ�� Teacher�࣬Ҳ�̳��� Person��
'''

class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Teacher(Person):

    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name,gender)
        self.course = course

t = Teacher('Alice', 'Female', 'English')
print t.name
print t.course

'''
�̳�һ����
����Ѿ�������Person�࣬��Ҫ�����µ�Student��Teacher��ʱ������ֱ�Ӵ�Person��̳У�

class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
����Student��ʱ��ֻ��Ҫ�Ѷ�������Լ��ϣ�����score��

class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score
һ��Ҫ�� super(Student, self).__init__(name, gender) ȥ��ʼ�����࣬���򣬼̳��� Person �� Student ��û�� name �� gender��

����super(Student, self)�����ص�ǰ��̳еĸ��࣬�� Person ��Ȼ�����__init__()������ע��self��������super()�д��룬��__init__()�н���ʽ���ݣ�����Ҫд����Ҳ����д����
'''