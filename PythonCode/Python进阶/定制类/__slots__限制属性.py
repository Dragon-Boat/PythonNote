#coding=utf-8
#author: sloop
'''
����
����Person��ͨ��__slots__������name��gender������������Student��ͨ��__slots__�������score�Ķ��壬ʹStudent�����ʵ��name��gender��score 3�����ԡ�
'''

class Person(object):

    __slots__ = ('name', 'gender')

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Student(Person):

    __slots__ = ('score')

    def __init__(self, name, gender, score):
        super(Student,self).__init__(name, gender)
        self.score = score

s = Student('Bob', 'male', 59)
s.name = 'Tim'
s.score = 99
print s.score

'''
__slots__
����Python�Ƕ�̬���ԣ��κ�ʵ���������ڶ����Զ�̬��������ԡ�

���Ҫ������ӵ����ԣ����磬Student��ֻ������� name��gender��score ��3�����ԣ��Ϳ�������Python��һ�������__slots__��ʵ�֡�

����˼�壬__slots__��ָһ��������������б�

class Student(object):
    __slots__ = ('name', 'gender', 'score')
    def __init__(self, name, gender, score):
        self.name = name
        self.gender = gender
        self.score = score
���ڣ���ʵ�����в�����

>>> s = Student('Bob', 'male', 59)
>>> s.name = 'Tim' # OK
>>> s.score = 99 # OK
>>> s.grade = 'A'
Traceback (most recent call last):
  ...
AttributeError: 'Student' object has no attribute 'grade'
__slots__��Ŀ�������Ƶ�ǰ������ӵ�е����ԣ��������Ҫ������⶯̬�����ԣ�ʹ��__slots__Ҳ�ܽ�ʡ�ڴ档
'''