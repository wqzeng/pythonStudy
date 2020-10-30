#!/usr/bin/env python3
# -*- coding:utf-8 -*-
' a test module'               #表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；
__author__ = "moke.tsang"

import sys
import numbers


def hello():
    args = sys.argv
    if len(args) == 1:
        print('hello world!%s' % args[0])
    elif len(args) == 2:
        print("hello,%s!" % args[1])
    else:
        print("too many arguments")


if __name__ == '__main__':
    hello()
