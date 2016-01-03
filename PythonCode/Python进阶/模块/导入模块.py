#coding=utf-8
#author: sloop
'''
����
Python��os.pathģ���ṩ�� isdir() �� isfile()�������뵼���ģ�飬�����ú����ж�ָ����Ŀ¼���ļ��Ƿ���ڡ�

ע��: 
1. �������л�����ƽ̨�����������Բ��Ե�Ҳ�Ƿ������е��ļ��к��ļ����÷���������/data/webroot/resource/python�ļ��к�/data/webroot/resource/python/test.txt�ļ�����ҿ��Բ����¡�
2. ��Ȼ����ҿ����ڱ����ϲ����Ƿ������Ӧ���ļ��к��ļ���

import os
print os.path.isdir(r'C:\Windows')
print os.path.isfile(r'C:\Windows\notepad.exe')
'''

import os
print os.path.isdir(r'C:\Windows')
print os.path.isfile(r'C:\Windows\notepad.exe')

'''
ע�⵽os.pathģ������������ַ�ʽ���룺

import os
import os.path
from os import path
from os.path import isdir, isfile
ÿһ�ַ�ʽ���� isdir �� isfile ��������ͬ��

�ο�����:

import os
print os.path.isdir(r'/data/webroot/resource/python')
print os.path.isfile(r'/data/webroot/resource/python/test.txt')
'''

'''
����ģ��
Ҫʹ��һ��ģ�飬���Ǳ������ȵ����ģ�顣Pythonʹ��import��䵼��һ��ģ�顣���磬����ϵͳ�Դ���ģ�� math��

import math
�������Ϊmath����һ��ָ���ѵ���ģ��ı�����ͨ���ñ��������ǿ��Է���mathģ��������������й����ĺ������������ࣺ

>>> math.pow(2, 0.5) # pow�Ǻ���
1.4142135623730951

>>> math.pi # pi�Ǳ���
3.141592653589793
�������ֻϣ�������õ���mathģ���ĳ�������������������к������������������䣺

from math import pow, sin, log
����������ֱ������ pow, sin, log ��3����������math����������û�е��������

>>> pow(2, 10)
1024.0
>>> sin(3.14)
0.0015926529164868282
����������ֳ�ͻ��ô�죿����mathģ����һ��log������loggingģ��Ҳ��һ��log���������ͬʱʹ�ã���ν�����ֳ�ͻ��

���ʹ��import����ģ���������ڱ���ͨ��ģ�������ú���������˲����ڳ�ͻ��

import math, logging
print math.log(10)   # ���õ���math��log����
logging.log(10, 'something')   # ���õ���logging��log����
���ʹ�� from...import ���� log �������Ʊ������ͻ����ʱ�����Ը�����������������������ͻ��

from math import log
from logging import log as logger   # logging��log���ڱ����logger
print log(10)   # ���õ���math��log
logger(10, 'import from logging')   # ���õ���logging��log
'''