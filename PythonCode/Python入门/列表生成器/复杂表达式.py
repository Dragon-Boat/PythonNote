#coding=utf-8
#author: sloop
'''
����
�����ɵı���У�����û�м����ͬѧ����ѷ������Ϊ��ɫ��

��ʾ����ɫ������ <td style="color:red"> ʵ�֡�
'''

#����
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
def generate_tr(name, score):
    if score < 60:
        return '<tr><td>%s</td><td style="color:red">%s</td></tr>' % (name, score)
    else:
        return '<tr><td>%s</td><td>%s</td></tr>'% (name, score)

tds = [generate_tr(name,score) for name, score in d.iteritems()]
print '<table border="1">'
print '<tr><th>Name</th><th>Score</th><tr>'
print '\n'.join(tds)
print '</table>'

'''
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
def generate_tr(name, score):
    return '<tr><td>%s</td><td>%s</td></tr>'% (name, score) if score >=60 else '<tr><td>%s</td><td style="color:red">%s</td></tr>' % (name, score)

tds = [generate_tr(name,score) for name, score in d.iteritems()]
print '<table border="1">'
print '<tr><th>Name</th><th>Score</th><tr>'
print '\n'.join(tds)
print '</table>'
'''

'''
���ӱ��ʽ
ʹ��forѭ���ĵ����������Ե�����ͨ��list�������Ե���dict��

���������µ�dict��

d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
��ȫ����ͨ��һ�����ӵ��б�����ʽ�������һ�� HTML ���

tds = ['<tr><td>%s</td><td>%s</td></tr>' % (name, score) for name, score in d.iteritems()]
print '<table>'
print '<tr><th>Name</th><th>Score</th><tr>'
print '\n'.join(tds)
print '</table>'
ע���ַ�������ͨ�� % ���и�ʽ������ָ���Ĳ������ %s���ַ�����join()�������԰�һ�� list ƴ�ӳ�һ���ַ�����

�Ѵ�ӡ�����Ľ������Ϊһ��html�ļ����Ϳ�����������п���Ч���ˣ�

<table border="1">
<tr><th>Name</th><th>Score</th><tr>
<tr><td>Lisa</td><td>85</td></tr>
<tr><td>Adam</td><td>95</td></tr>
<tr><td>Bart</td><td>59</td></tr>
</table>
'''