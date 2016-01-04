#coding=utf-8
#author: sloop
'''
����
+-Person
  +- Student
  +- Teacher

��һ��̳�����

+- SkillMixin
   +- BasketballMixin
   +- FootballMixin

��һ��̳�����

ͨ�����ؼ̳У��붨�塰��������ѧ�����͡������������ʦ����
'''

class Person(object):
    pass

class Student(Person):
    pass

class Teacher(Person):
    pass

class SkillMixin(object):
    pass

class BasketballMixin(SkillMixin):
    def skill(self):
        return 'basketball'

class FootballMixin(SkillMixin):
    def skill(self):
        return 'football'

class BStudent(Student, BasketballMixin):
    pass

class FTeacher(Teacher, FootballMixin):
    pass

s = BStudent()
print s.skill()

t = FTeacher()
print t.skill()

'''
���ؼ̳�
���˴�һ������̳��⣬Python����Ӷ������̳У���Ϊ���ؼ̳С�

���ؼ̳еļ̳����Ͳ���һ�����ˣ�����������

class A(object):
    def __init__(self, a):
        print 'init A...'
        self.a = a

class B(A):
    def __init__(self, a):
        super(B, self).__init__(a)
        print 'init B...'

class C(A):
    def __init__(self, a):
        super(C, self).__init__(a)
        print 'init C...'

class D(B, C):
    def __init__(self, a):
        super(D, self).__init__(a)
        print 'init D...'
����ͼ:



��������D ͬʱ�̳��� B �� C��Ҳ���� D ӵ���� A��B��C ��ȫ�����ܡ����ؼ̳�ͨ�� super()����__init__()����ʱ��A ��Ȼ���̳������Σ���__init__()ֻ����һ�Σ�

>>> d = D('d')
init A...
init C...
init B...
init D...
���ؼ̳е�Ŀ���Ǵ����ּ̳����зֱ�ѡ�񲢼̳г����࣬�Ա���Ϲ���ʹ�á�

�ٸ����ӣ�Python�������������TCPServer��UDPServer��UnixStreamServer��UnixDatagramServer��������������ģʽ�� �����ForkingMixin �� ���߳�ThreadingMixin���֡�

Ҫ���������ģʽ�� TCPServer��

class MyTCPServer(TCPServer, ForkingMixin)
    pass
Ҫ�������߳�ģʽ�� UDPServer��

class MyUDPServer(UDPServer, ThreadingMixin):
    pass
���û�ж��ؼ̳У�Ҫʵ���������п��ܵ������Ҫ 4x2=8 �����ࡣ
'''