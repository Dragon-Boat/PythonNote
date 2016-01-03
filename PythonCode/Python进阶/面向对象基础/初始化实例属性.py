#coding=utf-8
#author: sloop
'''
����
�붨��Person���__init__���������˽��� name��gender �� birth �⣬���ɽ�������ؼ��ֲ������������Ƕ���Ϊ���Ը�ֵ��ʵ����
'''

class Person(object):
    def __init__(self, name, gender, birth, **kw):
        self.name = name
        self.gender = gender
        self.birth = birth
        for k, v in kw.iteritems():
            setattr(self, k, v)

xiaoming = Person('Xiao Ming', 'Male', '1990-1-1', job='Student')

print xiaoming.name
print xiaoming.job

'''
��ʼ��ʵ������
��Ȼ���ǿ������ɵظ�һ��ʵ���󶨸������ԣ����ǣ���ʵ�����У�һ�����͵�ʵ��Ӧ��ӵ����ͬ���ֵ����ԡ����磬Person��Ӧ���ڴ�����ʱ���ӵ�� name��gender �� birth ���ԣ���ô�죿

�ڶ��� Person ��ʱ������ΪPerson�����һ�������__init__()������������ʵ��ʱ��__init__()�������Զ����ã����Ǿ����ڴ�Ϊÿ��ʵ����ͳһ�����������ԣ�

class Person(object):
    def __init__(self, name, gender, birth):
        self.name = name
        self.gender = gender
        self.birth = birth
__init__() �����ĵ�һ������������ self��Ҳ�����ñ�����֣�������ʹ��ϰ���÷����������������������ָ�����Ͷ��庯��û���κ�����

��Ӧ�أ�����ʵ��ʱ���ͱ���Ҫ�ṩ�� self ����Ĳ�����

xiaoming = Person('Xiao Ming', 'Male', '1991-1-1')
xiaohong = Person('Xiao Hong', 'Female', '1992-2-2')
����__init__()������ÿ��Personʵ���ڴ���ʱ�������� name��gender �� birth ��3�����ԣ����ң������費ͬ������ֵ����������ʹ��.��������

print xiaoming.name
# ��� 'Xiao Ming'
print xiaohong.birth
# ��� '1992-2-2'
Ҫ�ر�ע����ǣ���ѧ�߶���__init__()�������������� self ������

>>> class Person(object):
...     def __init__(name, gender, birth):
...         pass
... 
>>> xiaoming = Person('Xiao Ming', 'Male', '1990-1-1')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: __init__() takes exactly 3 arguments (4 given)
��ᵼ�´���ʧ�ܻ����в���������Ϊ��һ������name��Python������������ʵ�������ã��Ӷ��������������ĵ��ò���λ��ȫ��û�ж��ϡ�
'''