#coding=utf-8
#author: sloop
'''
����
�봴���������� Person ���ʵ���� list����������ʵ���� name ��ֵ��Ȼ���� name ��������
'''

class Person(object):
    pass

p1 = Person()
p1.name = 'Bart'

p2 = Person()
p2.name = 'Adam'

p3 = Person()
p3.name = 'Lisa'

L1 = [p1, p2, p3]
L2 = sorted(L1,key=lambda x:x.name)
# L2 = sorted(L1, lambda p1, p2: cmp(p1.name, p2.name))

print L2[0].name
print L2[1].name
print L2[2].name

'''
����ʵ������
��Ȼ����ͨ��Person�ഴ����xiaoming��xiaohong��ʵ����������Щʵ�����ϳ��˵�ַ��ͬ�⣬û��ʲô������ͬ������ʵ�����У�����xiaoming��xiaohongҪ�������Ǹ��Ե����֡��Ա����յ����ԡ�

�����ÿ��ʵ��ӵ�и��Բ�ͬ�����ԣ�����Python�Ƕ�̬���ԣ���ÿһ��ʵ����������ֱ�Ӹ����ǵ����Ը�ֵ�����磬��xiaoming���ʵ������name��gender��birth���ԣ�

xiaoming = Person()
xiaoming.name = 'Xiao Ming'
xiaoming.gender = 'Male'
xiaoming.birth = '1990-1-1'
��xiaohong���ϵ����Բ�һ��Ҫ��xiaoming��ͬ��

xiaohong = Person()
xiaohong.name = 'Xiao Hong'
xiaohong.school = 'No. 1 High School'
xiaohong.grade = 2
ʵ�������Կ�������ͨ����һ�����в�����

xiaohong.grade = xiaohong.grade + 1
'''