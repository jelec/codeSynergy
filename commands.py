import os 
import sys
from util import save,load,mkdir
from globalVars import set,get
import gen
import misc

# Get arguments
def getArgs(data):
  numArgs = data.count(' ') + 1
  set("nargs", numArgs)
  data = data.rstrip('\n')
  # print numArgs
  s = data.split(' ');
  return s

# Command Routing 
routes = { "hello" : misc.hello,
            "start" : misc.start}

# Route commands as shown
def commands(data):
  # Process the user command
  args = getArgs(data)
  contFlag = get("continued")
  if args[0] in routes:
    routes[args[0]](args, contFlag)
  else:
    print "Error: Command Unavaliable" 
  


