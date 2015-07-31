import os
import sys
from util import save,load,mkdir, log, printClear, printBlue, printHeader
from commands import commands # Library to keep all the command directing
from globalVars import get,set

#Initialization
def init():
  set("continued",0)
  set("tag","unset")
  mkdir("blocks") # Storage of these projects
  mkdir("files")
  mkdir("projects")
  printClear()
  printHeader()
  

# Command Line interface
def main():
  init()
  while 1:
    if(get("continued") == 0):
      try:
          line = sys.stdin.readline()
      except KeyboardInterrupt:
          break
      if not line:
          break
      commands(line)
    # Allow the copying of all information to the commands line
    else: 
      try:
          line = sys.stdin.read()
      except KeyboardInterrupt:
          break
      if not line:
          break
      commands(line)

# Create a command line thread as well
if __name__ == "__main__":
  main()




