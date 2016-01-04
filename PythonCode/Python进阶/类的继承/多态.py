#coding=utf-8
#author: sloop
'''
����
Python�ṩ��open()��������һ�������ļ��������� File ����File������һ��read()�������Զ�ȡ�ļ����ݣ�

���磬���ļ���ȡ���ݲ�����ΪJSON�����

import json
f = open('/path/to/file.json', 'r')
print json.load(f)
����Python�Ķ�̬���ԣ�json.load()����һ��Ҫ��һ��File�����ȡ���ݡ��κζ���ֻҪ��read()�������ͳ�ΪFile-like Object�������Դ���json.load()��

�볢�Ա�дһ��File-like Object����һ���ַ��� r'["Tim", "Bob", "Alice"]'��װ�� File-like Object ���� json.load() ������
'''

import json

class Students(object):
    def read(self):
        return r'["Tim", "Bob", "Alice"]'

s = Students()

print json.load(s)

'''
��̬
����м̳й�ϵ�������������Ϳ�������ת�Ϳ����������ͣ�������Ǵ� Person ������ Student��Teacher ������д��һ�� whoAmI() ������

class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    def whoAmI(self):
        return 'I am a Person, my name is %s' % self.name

class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score
    def whoAmI(self):
        return 'I am a Student, my name is %s' % self.name

class Teacher(Person):
    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name, gender)
        self.course = course
    def whoAmI(self):
        return 'I am a Teacher, my name is %s' % self.name
��һ�������У�������ǽ���һ������ x�������۸� x �� Person��Student���� Teacher����������ȷ��ӡ�������

def who_am_i(x):
    print x.whoAmI()

p = Person('Tim', 'Male')
s = Student('Bob', 'Male', 88)
t = Teacher('Alice', 'Female', 'English')

who_am_i(p)
who_am_i(s)
who_am_i(t)
���н����

I am a Person, my name is Tim
I am a Student, my name is Bob
I am a Teacher, my name is Alice
������Ϊ��Ϊ��̬��Ҳ����˵���������ý������� x ��ʵ�������ϡ�s ��Student���ͣ���ʵ����ӵ���Լ��� whoAmI()�����Լ��� Person�̳е� whoAmI������������ s.whoAmI()�����Ȳ���������Ķ��壬���û�ж��壬��˳�ż̳������ϲ��ң�ֱ����ĳ���������ҵ�Ϊֹ��

����Python�Ƕ�̬���ԣ����ԣ����ݸ����� who_am_i(x)�Ĳ��� x ��һ���� Person �� Person �������͡��κ��������͵�ʵ�������ԣ�ֻҪ����һ��whoAmI()�ķ������ɣ�

class Book(object):
    def whoAmI(self):
        return 'I am a book'
���Ƕ�̬���Ժ;�̬���ԣ�����Java�����Ĳ��֮һ����̬���Ե���ʵ����������������ͣ�ֻҪ�������ڣ�������ȷ���Ϳ��Ե��á�
'''