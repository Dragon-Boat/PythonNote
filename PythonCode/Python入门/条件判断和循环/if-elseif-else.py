#coding=utf-8
#author: sloop
'''
����
������շ������������

    90�ֻ����ϣ�excellent

    80�ֻ����ϣ�good

    60�ֻ����ϣ�passed

    60�����£�failed

���д������ݷ�����ӡ�����
'''

#����
score = 85

if score>=90:
    print 'excellent'
elif score>=80:
    print 'good'
elif score>=60:
    print 'passed'
else:
    print 'failed'

'''
if-elif-else
�е�ʱ��һ�� if ... else ... �������á����磬��������Ļ��֣�

����1��18������ϣ�adult
����2��6������ϣ�teenager
����3��6�����£�kid
���ǿ�����һ�� if age >= 18 �ж��Ƿ��������1����������ϣ���ͨ��һ�� if �ж� age >= 6 ���ж��Ƿ��������2������ִ������3��

if age >= 18:
    print 'adult'
else:
    if age >= 6:
        print 'teenager'
    else:
        print 'kid'
����д���������Ǿ͵õ���һ������Ƕ�׵� if ... else ... ��䡣����߼�û�����⣬���ǣ����������������������3�������� baby��

if age >= 18:
    print 'adult'
else:
    if age >= 6:
        print 'teenager'
    else:
        if age >= 3:
            print 'kid'
        else:
            print 'baby'
��������ֻ��Խ��Խ�࣬����Ҳ��Խ��Խ�ѿ���

Ҫ����Ƕ�׽ṹ�� if ... else ...�����ǿ����� if ... ���elif ... else ... �Ľṹ��һ��д�����еĹ���

if age >= 18:
    print 'adult'
elif age >= 6:
    print 'teenager'
elif age >= 3:
    print 'kid'
else:
    print 'baby'
elif ��˼���� else if������һ�������Ǿ�д���˽ṹ�ǳ�������һϵ�������жϡ�

�ر�ע��: ��һϵ�������жϻ���ϵ��������жϣ����ĳ���ж�Ϊ True��ִ�����Ӧ�Ĵ���飬����������жϾ�ֱ�Ӻ��ԣ�����ִ���ˡ�

��˼������Ĵ��룺

age = 8
if age >= 6:
    print 'teenager'
elif age >= 18:
    print 'adult'
else:
    print 'kid'
�� age = 8 ʱ�������ȷ���� age = 20 ʱ��Ϊʲôû�д�ӡ�� adult��

���Ҫ�޸���Ӧ������޸���
'''