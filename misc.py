import os 
import sys
from util import save,load,mkdir,cont,log
from globalVars import set,get

# Commands for information setting
def hello(args, flag):
  if( flag):
    log("hello world")
    cont(0,"hello")
  else:
    log("yolo")
    cont(1,"hello")

def start(args,flag):
  nargs = get("nargs")
  if( nargs > 1):
    mkdir(args[1])