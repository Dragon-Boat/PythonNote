#coding=utf-8
#author: sloop
'''
����
��� Person �����һ�������� count��ÿ����һ��ʵ����count ���Ծͼ� 1�������Ϳ���ͳ�Ƴ�һ�������˶��ٸ� Person ��ʵ����
'''

class Person(object):
    count = 0
    def __init__(self,name):
        self.name = name
        Person.count += 1

p1 = Person('Bob')
print Person.count

p2 = Person('Alice')
print Person.count

p3 = Person('Tim')
print Person.count

'''
����������
����ģ�壬��ʵ�����Ǹ����ഴ���Ķ���

����һ��ʵ���ϵ����Բ���Ӱ������ʵ�������ǣ��౾��Ҳ��һ��������������ϰ�һ�����ԣ�������ʵ�������Է���������ԣ����ң�����ʵ�����ʵ������Զ���ͬһ����Ҳ����˵��ʵ������ÿ��ʵ������ӵ�У����������������������ֻ��һ�ݡ�

���������Կ���ֱ���� class �ж��壺

class Person(object):
    address = 'Earth'
    def __init__(self, name):
        self.name = name
��Ϊ��������ֱ�Ӱ������ϵģ����ԣ����������Բ���Ҫ����ʵ�����Ϳ���ֱ�ӷ��ʣ�

print Person.address
# => Earth
��һ��ʵ�������������Ҳ�ǿ��Է��ʵģ�����ʵ�������Է��ʵ���������������ԣ�

p1 = Person('Bob')
p2 = Person('Alice')
print p1.address
# => Earth
print p2.address
# => Earth
����Python�Ƕ�̬���ԣ�������Ҳ�ǿ��Զ�̬��Ӻ��޸ĵģ�

Person.address = 'China'
print p1.address
# => 'China'
print p2.address
# => 'China'
��Ϊ������ֻ��һ�ݣ����ԣ���Person���address�ı�ʱ������ʵ�����ʵ��������Զ��ı��ˡ�
'''