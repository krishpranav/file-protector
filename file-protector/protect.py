#!/usr/bin/env python 

from sys import argv
from os.path import expanduser as expu, expandvars as expv
from os.path import basename, dirname, abspath, exists
from builtins import input
from config import Config 


c = Config()

def pprint(msg):
    global c
    print(c.protect_prefix + msg)
    

