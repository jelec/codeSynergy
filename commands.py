import os 
import sys
from util import save,load,mkdir, error
from globalVars import set,get
from routes import routes

# Get arguments
def getArgs(data):
  numArgs = data.count(' ') + 1
  set("nargs", numArgs)
  data = data.rstrip('\n')
  # print numArgs
  s = data.split(' ');
  return s
  

# Route commands as shown
def commands(data):
  # Process the user command
  args = getArgs(data)
  contFlag = get("continued")
  if(contFlag == 1):
    routes[get("prevCmd")](args, contFlag, data)
  elif args[0] in routes:
    routes[args[0]](args, contFlag, data)
  else:
    error("Error: Command Unavaliable") 
  


