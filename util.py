import os
import sys
from globalVars import set,get
import json

debug = 1

# Create a directory function
def mkdir(dir):
	if not os.path.exists(dir):
	    os.makedirs(dir)
	return

# Load a file function | Add other hooks later
def load(path):
  with open(path, 'r') as content_file:
    content = content_file.read()
  return content

# Write file function 
def save(path, data, line=0):
  with open(path,'w+') as f:
    f.seek(int(line)) #Save this information to a particular line
    f.write(data)

def loadJSON(path):
  data = []
  with open(path) as f:
    for line in f:
        data.append(json.loads(line))

  return data

def printHeader():
  log("---------------------------------------------")
  log("--------- Code Synergy: By jelec  -----------")
  log("---------------------------------------------")
  printBlue("Enter commands or type \"help\"")

def printClear():
  os.system('cls' if os.name == 'nt' else 'clear')

def cont(state, cmd):
  set("continued", state)
  set("prev", cmd)

def keyExists(path, key):
  return os.path.isfile(path+"/"+key) 

# Printing out colours
class bcolors:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'

def printGreen(data):
  print bcolors.OKGREEN + data + bcolors.ENDC

def printBlue(data):
  print bcolors.OKBLUE + data + bcolors.ENDC

def printYellow(data):
  print bcolors.WARNING + data + bcolors.ENDC

def printPink(data):
  print bcolors.HEADER + data + bcolors.ENDC

def error(data):
  print bcolors.FAIL + data + bcolors.ENDC

def log(string):
  if(debug):
    printGreen(string)

def clear(a,b,c):
  printClear()
  printHeader()
