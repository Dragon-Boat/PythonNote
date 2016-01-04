#coding=utf-8
#author: sloop
'''
����
����ݼ̳���������ת��������˼�� t �Ƿ��� Person��Student��Teacher��object ���ͣ���ʹ��isinstance()�ж�����֤���Ĵ𰸡�
'''

class Person(object):

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Student(Person):

    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score

class Teacher(Person):

    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name, gender)
        self.course = course

t = Teacher('Alice', 'Female', 'English')

print isinstance(t, Person)
print isinstance(t, Student)
print isinstance(t, Teacher)
print isinstance(t, object)

'''
�ж�����
����isinstance()�����ж�һ�����������ͣ��ȿ�������Python���õ�����������str��list��dict��Ҳ�������������Զ�����࣬���Ǳ����϶����������͡�

���������µ� Person��Student �� Teacher �Ķ��弰�̳й�ϵ���£�

class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score

class Teacher(Person):
    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name, gender)
        self.course = course

p = Person('Tim', 'Male')
s = Student('Bob', 'Male', 88)
t = Teacher('Alice', 'Female', 'English')
�������õ����� p��s��t ʱ������ʹ�� isinstance �ж����ͣ�

>>> isinstance(p, Person)
True    # p��Person����
>>> isinstance(p, Student)
False   # p����Student����
>>> isinstance(p, Teacher)
False   # p����Teacher����
��˵���ڼ̳����ϣ�һ�������ʵ���������������ͣ���Ϊ����ȸ������һЩ���Ժͷ�����

�����ٿ��� s ��

>>> isinstance(s, Person)
True    # s��Person����
>>> isinstance(s, Student)
True    # s��Student����
>>> isinstance(s, Teacher)
False   # s����Teacher����
s ��Student���ͣ�����Teacher���ͣ����������⡣���ǣ�s Ҳ��Person���ͣ���ΪStudent�̳���Person����Ȼ����Person����һЩ���Ժͷ��������ǣ��� s ����Person��ʵ��Ҳ�ǿ��Եġ�

��˵����һ���̳����ϣ�һ��ʵ�����Կ�������������ͣ�Ҳ���Կ�������������͡�
'''