#coding=utf-8
#author: sloop
'''
����
����import ... as ...�������Զ�̬���벻ͬ���Ƶ�ģ�顣

Python 2.6/2.7�ṩ��json ģ�飬��Python 2.5�Լ�����汾û��jsonģ�飬�������԰�װһ��simplejsonģ�飬������ģ���ṩ�ĺ���ǩ���͹��ܶ�һģһ����

��д������json ģ��Ĵ��룬����Python 2.5/2.6/2.7���������С�

�ȳ��Ե���json�����ʧ�ܣ��ٳ��Ե���simplejson as json
python�Ĳ����쳣��ʽ������java��try catch
'''

try:
    import json
except ImportError:
    import simplejson as json

print json.dumps({'python':2.7})

'''
��̬����ģ��
��������ģ�鲻���ڣ�Python�������ᱨ ImportError ����

>>> import something
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named something
�е�ʱ��������ͬ��ģ���ṩ����ͬ�Ĺ��ܣ����� StringIO �� cStringIO ���ṩ��StringIO������ܡ�

������ΪPython�Ƕ�̬���ԣ�����ִ�У����Python���������ٶ�����

���Ҫ���Python����������ٶȣ���򵥵ķ����ǰ�ĳЩ�ؼ������� C ������д���������ܴ�����ִ���ٶȡ�

ͬ���Ĺ��ܣ�StringIO �Ǵ�Python�����д�ģ��� cStringIO ���ֺ����� C д�ģ���� cStringIO �����ٶȸ��졣

����ImportError�������Ǿ�����Python�ж�̬����ģ�飺

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO
���������ȳ��Դ�cStringIO���룬���ʧ���ˣ�����cStringIOû�б���װ�����ٳ��Դ�StringIO���롣���������cStringIOģ����ڣ������ǽ���ø���������ٶȣ����cStringIO�����ڣ��򶥶���������ٶȻ������������Ӱ����������ִ�С�

try �������ǲ�����󣬲��ڲ���ָ������ʱִ�� except ��䡣
'''