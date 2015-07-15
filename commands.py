import os 
import sys
from util import save,load,mkdir, log
import collections
from globalVars import set,get

# Also have the ability to start services here 
def cont(state, cmd):
  set("continued", state)
  set("prev", cmd)

# Get arguments
def getArgs(data):
  numArgs = data.count(' ') + 1
  set("nargs", numArgs)
  data = data.rstrip('\n')
  # print numArgs
  s = data.split(' ');
  return s

def hello(args, flag):
  if( flag):
    print "hello world"
    cont(1,"hello")
  else:
    print "yolo"
    cont(0,"hello")

def start(args,flag):
  nargs = get("nargs")
  if( nargs > 1):
    mkdir(args[1])

routes = { "hello" : hello,
            "start" : start}


# Route commands as shown
def commands(data):
  # Process the user command
  args = getArgs(data)
  contFlag = get("continued")
  print contFlag
  if args[0] in routes:
    routes[args[0]](args, contFlag)
  else:
    print "Error: Command Unavaliable" 
  


