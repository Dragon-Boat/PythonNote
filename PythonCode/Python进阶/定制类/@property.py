#coding=utf-8
#author: sloop
'''
����
���û�ж���set�������Ͳ��ܶԡ����ԡ���ֵ����ʱ���Ϳ��Դ���һ��ֻ�������ԡ���

���Student���һ��grade���ԣ����� score ���� A��>=80����B��C��<60����
'''

class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.__score = score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        if score < 0 or score > 100:
            raise ValueError('invalid score')
        self.__score = score

    @property
    def grade(self):
        if self.score < 60:
            return 'C'
        if self.score < 80:
            return 'B'
        return 'A'

s = Student('Bob', 59)
print s.grade

s.score = 60
print s.grade

s.score = 99
print s.grade

'''
@property
���� Student �ࣺ

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
��������Ҫ�޸�һ�� Student �� scroe ����ʱ��������ôд��

s = Student('Bob', 59)
s.score = 60
����Ҳ������ôд��

s.score = 1000
��Ȼ��ֱ�Ӹ����Ը�ֵ�޷�����������Ч�ԡ�

�����������������

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score
    def get_score(self):
        return self.__score
    def set_score(self, score):
        if score < 0 or score > 100:
            raise ValueError('invalid score')
        self.__score = score
����һ����s.set_score(1000) �ͻᱨ��

����ʹ�� get/set ��������װ��һ�����Եķ����������������̵������ж��ܳ�����

����д s.get_score() �� s.set_score() û��ֱ��д s.score ����ֱ�ӡ�

��û����ȫ�����ķ�����----�С�

��ΪPython֧�ָ߽׺������ں���ʽ��������ǽ�����װ����������������װ���������� get/set ������װ�Ρ������Ե��ã�

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self, score):
        if score < 0 or score > 100:
            raise ValueError('invalid score')
        self.__score = score
ע��: ��һ��score(self)��get��������@propertyװ�Σ��ڶ���score(self, score)��set��������@score.setterװ�Σ�@score.setter��ǰһ��@propertyװ�κ�ĸ���Ʒ��

���ڣ��Ϳ�����ʹ������һ������score�ˣ�

>>> s = Student('Bob', 59)
>>> s.score = 60
>>> print s.score
60
>>> s.score = 1000
Traceback (most recent call last):
  ...
ValueError: invalid score
˵���� score ��ֵʵ�ʵ��õ��� set������
'''