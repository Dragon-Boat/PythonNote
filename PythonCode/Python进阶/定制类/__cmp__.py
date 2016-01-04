#coding=utf-8
#author: sloop
'''
����
���޸� Student �� __cmp__ �������������շ����Ӹߵ������򣬷�����ͬ�İ���������
'''

class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return '(%s: %s)' % (self.name, self.score)

    __repr__ = __str__

    def __cmp__(self, s):
        if self.score == s.score:
            return cmp(self.name, s.name)
        return -cmp(self.score, s.score)

L = [Student('Tim', 99), Student('Bob', 88), Student('Alice', 99)]
print sorted(L)


'''
__cmp__
�� int��str ������������������ʱ��Python�� sorted() ����Ĭ�ϵıȽϺ��� cmp ���򣬵��ǣ������һ�� Student ���ʵ������ʱ���ͱ����ṩ�����Լ������ⷽ�� __cmp__()��

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __str__(self):
        return '(%s: %s)' % (self.name, self.score)
    __repr__ = __str__

    def __cmp__(self, s):
        if self.name < s.name:
            return -1
        elif self.name > s.name:
            return 1
        else:
            return 0
���� Student ��ʵ����__cmp__()������__cmp__��ʵ������self�ʹ����ʵ�� s ���бȽϣ���� self Ӧ������ǰ�棬�ͷ��� -1����� s Ӧ������ǰ�棬�ͷ���1����������൱������ 0��

Student��ʵ���˰�name��������

>>> L = [Student('Tim', 99), Student('Bob', 88), Student('Alice', 77)]
>>> print sorted(L)
[(Alice: 77), (Bob: 88), (Tim: 99)]
ע��: ���list���������� Student �࣬�� __cmp__ ���ܻᱨ��

L = [Student('Tim', 99), Student('Bob', 88), 100, 'Hello']
print sorted(L)
��˼����ν����
'''