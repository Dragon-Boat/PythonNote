#coding=utf-8
#author: sloop
'''
����
����Ͻڵ� Person ������ count ��Ϊ __count���������ܷ��ʵ��������ʸ����ԡ�
'''

class Person(object):
    __count = 0

    def __init__(self, name):
        self.name = name
        Person.__count += 1
        print Person.__count

p1 = Person('Bob')
p2 = Person('Alice')

print Person.__count

'''
�����Ժ�ʵ���������ֳ�ͻ��ô��
�޸������Իᵼ������ʵ�����ʵ���������ȫ������Ӱ�죬���ǣ������ʵ���������޸������Իᷢ��ʲô�����أ�

class Person(object):
    address = 'Earth'
    def __init__(self, name):
        self.name = name

p1 = Person('Bob')
p2 = Person('Alice')

print 'Person.address = ' + Person.address

p1.address = 'China'
print 'p1.address = ' + p1.address

print 'Person.address = ' + Person.address
print 'p2.address = ' + p2.address
������£�

Person.address = Earth
p1.address = China
Person.address = Earth
p2.address = Earth
���Ƿ��֣��������� p1.address = 'China' ��p1���� address ȷʵ����� 'China'�����ǣ�Person.address��p2.address��Ȼ��'Earch'����ô���£�

ԭ���� p1.address = 'China'��û�иı� Person �� address�����Ǹ� p1���ʵ������ʵ������address ����p1��˵������һ��ʵ������address��ֵ��'China'����������������PersonҲ��һ��������address������:

���� p1.address ʱ�����Ȳ���ʵ�����ԣ�����'China'��

���� p2.address ʱ��p2û��ʵ������address��������������address����˷���'Earth'��

�ɼ�����ʵ�����Ժ�����������ʱ��ʵ���������ȼ��ߣ��������ε��������Եķ��ʡ�

�����ǰ� p1 �� address ʵ������ɾ���󣬷��� p1.address ���ַ��������Ե�ֵ 'Earth'�ˣ�

del p1.address
print p1.address
# => Earth
�ɼ���ǧ��Ҫ��ʵ�����޸������ԣ���ʵ���ϲ�û���޸������ԣ����Ǹ�ʵ������һ��ʵ�����ԡ�
'''