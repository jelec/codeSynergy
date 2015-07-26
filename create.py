import os 
import sys
from util import save,load,mkdir,cont,log, printBlue,error
from globalVars import set,get
import json
import view

# Handle insertions for code, saves code blocks
def insertBlock(args,flag, data):
  if(flag == 1):
    log("Creating Block \"" + get("key") + "\"")
    save("blocks/"+get("key"),data)
    set("continued",0)
    printBlue("Block Creation Complete.")
  else:
    set("continued",1)
    set("prevCmd", "create")
    set("key",args[1])
    log("Enter Block Information and press Ctrl+D when done!")

# Handles insertions for files
# Method of check all of the inserts
# @Params - Key
# @Params - Constructor format ["json", "custom1"] [Allows for different parsers]
# @Params - Block consistency [1,2,3,4 ... n]
# Example Usage: file util 1 helloworld hello s1
def insertFile(args,flag,data):
  # PARAM_CONSTRUCT = 2
  PARAM_KEY = 1
  PARAM_BLOCKS_BASE = 2
  data = []
  files = os.listdir("blocks")

  for x in args[PARAM_BLOCKS_BASE:]:
    if x in files:
      data.append(x)
    else :
      print "Error: Invalid Block"

  save("files/" + args[PARAM_KEY], json.dumps(data))  


# Handles insertions for complete projects
# @Params - Key
# @Params - Constructor format ["json", "custom1"]
# @Params - File consistency [1,2,3,4 .. n]
# Example Usage: project util 
def insertModule (args,flag,data):
  # Creates a project based on file jsons on the layout of the code block
  # PARAM_CONSTRUCT = 2
  log("Creating module!")
  PARAM_KEY = 1
  PARAM_NAME_DIR = 2
  PARAM_FILES_BASE = 3
  data = []
  files = os.listdir("files")
  ARGUMENTS = len(args[PARAM_FILES_BASE:]) - 1
  print ARGUMENTS

  # Another method of constructing a project
  for x in args[PARAM_FILES_BASE:]:
    # Split the arguments here
    s = x.split(":")
    # For each odd one we will iterate through those!
    if x in files:
      data.append(x)
    else :
      print "Error: Invalid File"
 
  save("projects/" + args[PARAM_KEY], json.dumps(data))

