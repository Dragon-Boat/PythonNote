#coding=utf-8
#author: sloop
'''
����
����Person��Ķ��壺

class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
ϣ������ name��gender �⣬�����ṩ�������Ĺؼ��ֲ��������󶨵�ʵ�������޸� Person �� __init__()�� �壬��ɸù��ܡ�
'''

class Person(object):

    def __init__(self, name, gender, **kw):
        self.name = name
        self.gender = gender
        for k, v in kw.iteritems():
            setattr(self,k,v)

p = Person('Bob', 'Male', age=18, course='Python')
print p.age
print p.course

'''
��ȡ������Ϣ
�õ�һ�������������� isinstance() �ж����Ƿ���ĳ�����͵�ʵ���⣬����û�б�ķ�����ȡ���������Ϣ�أ�

���磬���ж��壺

class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score
    def whoAmI(self):
        return 'I am a Student, my name is %s' % self.name
���ȿ����� type() ������ȡ���������ͣ�������һ�� Type ����

>>> type(123)
<type 'int'>
>>> s = Student('Bob', 'Male', 88)
>>> type(s)
<class '__main__.Student'>
��Σ������� dir() ������ȡ�������������ԣ�

>>> dir(123)   # ����Ҳ�кܶ�����...
['__abs__', '__add__', '__and__', '__class__', '__cmp__', ...]

>>> dir(s)
['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'gender', 'name', 'score', 'whoAmI']
����ʵ��������dir()��������ʵ�����ԣ�����`__class__`������������������ԡ�ע�⵽����`whoAmI`Ҳ�� s ��һ�����ԡ�

���ȥ��`__xxx__`������������ԣ�ֻ���������Լ���������ԣ��ع�һ��filter()�������÷���

dir()���ص��������ַ����б������֪һ���������ƣ�Ҫ��ȡ�������ö�������ԣ�����Ҫ�� getattr() �� setattr( )�����ˣ�

>>> getattr(s, 'name')  # ��ȡname����
'Bob'

>>> setattr(s, 'name', 'Adam')  # �����µ�name����

>>> s.name
'Adam'

>>> getattr(s, 'age')  # ��ȡage���ԣ��������Բ����ڣ�����
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute 'age'

>>> getattr(s, 'age', 20)  # ��ȡage���ԣ�������Բ����ڣ��ͷ���Ĭ��ֵ20��
20
'''