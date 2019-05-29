#!/usr/bin/python3
# -*- coding: utf-8 -*-
# _author_  : KainHuck

import time

#-----------------装饰器-------------------#
def decorator(func):
    def wraper():
        print("---增加的业务---")
        func()
    return wraper

@decorator
def a():
    print("---a---")
#----------------------------------------#


#---------------生成器--------------------#
def gen():
    for i in range(1000000):
        pass

def genPlus():
    for i in range(100000000000000):
        yield i


if __name__ == '__main__':
    # a()
    start = time.time()
    gen()
    end = time.time()
    print("耗时%s" % (end - start))