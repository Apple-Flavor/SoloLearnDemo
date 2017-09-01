'''
读取一个合法的 python 表达式，即你输入字符串的时候必须使用引号将它括起来，否则它会引发一个 SyntaxError 。
input() 本质上还是使用 raw_input() 来实现的，只是调用完 raw_input() 之后再调用 eval() 函数，
所以，你甚至可以将表达式作为 input() 的参数，并且它会计算表达式的值并返回它。

input([prompt])

    Equivalent to eval(raw_input(prompt)) 
'''
#!encoding=utf8
inpt = input("请输入：")
print inpt
