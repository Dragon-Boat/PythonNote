#coding=utf-8
#author: sloop

import functools
'''
��ӡlog����
�������: �ַ���
'''
def log(perfix):
    def log_decorator(f):
        @functools.wraps(f) #��ɺ����Զ����ƹ��ܣ���ֹ�ı亯��ԭ�е�����
        def wrapper(*args, **kw):
            print '[%s] %s...' %(perfix, f.__name__)
            return f(*args, **kw)
        return wrapper
    return log_decorator

@log('DEBUG')
def test():
    pass
print test()
print test.__name__