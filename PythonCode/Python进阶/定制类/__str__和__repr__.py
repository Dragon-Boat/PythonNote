#coding=utf-8
#author: sloop
'''
����
���Student �ඨ��__str__��__repr__������ʹ���ܴ�ӡ��<Student: name, gender, score>��

class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score
'''

class Person(object):

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Student(Person):

    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score

    def __str__(self):
        return '(Student: %s, %s, %s)' % (self.name, self.gender, self.score)
    __repr__ = __str__

s = Student('Bob', 'male', 88)
print s

'''
__str__��__repr__
���Ҫ��һ�����ʵ����� str������Ҫʵ�����ⷽ��__str__()��

class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    def __str__(self):
        return '(Person: %s, %s)' % (self.name, self.gender)
���ڣ��ڽ���ʽ���������� print ���ԣ�

>>> p = Person('Bob', 'male')
>>> print p
(Person: Bob, male)
���ǣ����ֱ���ñ��� p��

>>> p
<main.Person object at 0x10c941890>
�ƺ�__str__() ���ᱻ���á�

��Ϊ Python ������__str__()��__repr__()���ַ�����__str__()������ʾ���û�����__repr__()������ʾ��������Ա��

��һ��͵���Ķ���__repr__�ķ�����

class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    def __str__(self):
        return '(Person: %s, %s)' % (self.name, self.gender)
    __repr__ = __str__
'''