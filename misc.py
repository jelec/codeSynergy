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

def setTag(args,flag,data):
	set("tag", args[1])
	log("Tag has been set to " + args[1])

def clearTag(args,flag,data):
	set("tag", "unset")
	log("Tag has been unset")

# Online search : 
def useOnline(args,flag,data):
	# Use online code blocks
	set("online", "true")
	print "We will now search online repos as well"

def _mkdir(args,flag,data):
	mkdir(args[1])

def start(args,flag):
  nargs = get("nargs")
  if( nargs > 1):
    mkdir(args[1])