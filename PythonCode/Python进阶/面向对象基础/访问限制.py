#coding=utf-8
#author: sloop
'''
����
���Person���__init__���������name��score����������score�󶨵�__score�����ϣ������ⲿ�Ƿ��ܷ��ʵ���
'''

class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score

p = Person('Bob', 59)

print p.name
print p.__score

'''
��������
���ǿ��Ը�һ��ʵ���󶨺ܶ����ԣ������Щ���Բ�ϣ�����ⲿ���ʵ���ô�죿

Python������Ȩ�޵Ŀ�����ͨ����������ʵ�ֵģ����һ��������˫�»��߿�ͷ(__)�������Ծ��޷����ⲿ���ʡ������ӣ�

class Person(object):
    def __init__(self, name):
        self.name = name
        self._title = 'Mr'
        self.__job = 'Student'
p = Person('Bob')
print p.name
# => Bob
print p._title
# => Mr
print p.__job
# => Error
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Person' object has no attribute '__job'
�ɼ���ֻ����˫�»��߿�ͷ��"__job"����ֱ�ӱ��ⲿ���ʡ�

���ǣ����һ��������"__xxx__"����ʽ���壬�����ֿ��Ա��ⲿ�����ˣ���"__xxx__"�����������Python�����б���Ϊ�������ԣ��кܶ�Ԥ������������Կ���ʹ�ã�ͨ�����ǲ�Ҫ����ͨ������"__xxx__"���塣

�Ե��»��߿�ͷ������"_xxx"��ȻҲ���Ա��ⲿ���ʣ����ǣ�����ϰ�ߣ����ǲ�Ӧ�ñ��ⲿ���ʡ�
'''