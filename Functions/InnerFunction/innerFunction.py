#!/usr/bin/python

import time
import os

def Func1():
    print("Func1")

def Func2():
    print("First Func2")
    
    def InnerFunc2():
        print("Inner Func2")

    InnerFunc2()
    print("Second Func2")


Func1()
Func2()
