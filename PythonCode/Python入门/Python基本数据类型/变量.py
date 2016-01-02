#coding=utf-8
x1 = 1
d = 3
n = 100
x100 = x1+(100-1)*d
s = (x1+x100)*n/2
print s
'''
任务
等差数列可以定义为每一项与它的前一项的差等于一个常数，可以用变量 x1 表示等差数列的第一项，用 d 表示公差，请计算数列

1 4 7 10 13 16 19 ...

前 100 项的和。
'''

'''
什么是变量
在Python中，变量的概念基本上和初中代数的方程变量是一致的。

例如，对于方程式 y=x*x ，x就是变量。当x=2时，计算结果是4，当x=5时，计算结果是25。

只是在计算机程序中，变量不仅可以是数字，还可以是任意数据类型。

在Python程序中，变量是用一个变量名表示，变量名必须是大小写英文、数字和下划线（_）的组合，且不能用数字开头，比如：

a = 1
变量a是一个整数。

t_007 = 'T007'
变量t_007是一个字符串。

在Python中，等号=是赋值语句，可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量，例如：

a = 123    # a是整数
print a
a = 'imooc'   # a变为字符串
print a
这种变量本身类型不固定的语言称之为动态语言，与之对应的是静态语言。

静态语言在定义变量时必须指定变量类型，如果赋值的时候类型不匹配，就会报错。例如Java是静态语言，赋值语句如下（// 表示注释）：

int a = 123; // a是整数类型变量
a = "mooc"; // 错误：不能把字符串赋给整型变量
和静态语言相比，动态语言更灵活，就是这个原因。

请不要把赋值语句的等号等同于数学的等号。比如下面的代码：

x = 10
x = x + 2
如果从数学上理解x = x + 2那无论如何是不成立的，在程序中，赋值语句先计算右侧的表达式x + 2，得到结果12，再赋给变量x。由于x之前的值是10，重新赋值后，x的值变成12。

最后，理解变量在计算机内存中的表示也非常重要。当我们写：a = 'ABC'时，Python解释器干了两件事情：

1. 在内存中创建了一个'ABC'的字符串；

2. 在内存中创建了一个名为a的变量，并把它指向'ABC'。

也可以把一个变量a赋值给另一个变量b，这个操作实际上是把变量b指向变量a所指向的数据，例如下面的代码：

a = 'ABC'
b = a
a = 'XYZ'
print b
最后一行打印出变量b的内容到底是'ABC'呢还是'XYZ'？如果从数学意义上理解，就会错误地得出b和a相同，也应该是'XYZ'，但实际上b的值是'ABC'，让我们一行一行地执行代码，就可以看到到底发生了什么事：

执行a = 'ABC'，解释器创建了字符串  'ABC'和变量 a，并把a指向 'ABC'：

执行b = a，解释器创建了变量 b，并把b指向 a 指向的字符串'ABC'：

执行a = 'XYZ'，解释器创建了字符串'XYZ'，并把a的指向改为'XYZ'，但b并没有更改：

所以，最后打印变量b的结果自然是'ABC'了。
'''