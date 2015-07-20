import os 
import sys
from util import save,load,mkdir,cont,log, printBlue
from globalVars import set,get

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

# Remove a block
def deleteBlock(args, flag, data):
  os.remove("blocks/"+args[1])
  log("Block deleted.")

def deleteFile(args, flag, data):
  os.remove("file/"+args[1])
  log("File deleted.")

def deleteProject(args, flag, data):
  os.remove("project/"+args[1])
  log("Project deleted.")

# Handles insertions for files
# Method of check all of the inserts
# @Params - Key
# @Params - Constructor format ["json", "custom1"] [Allows for different parsers]
# @Params - Block consistency [1,2,3,4 ... n]
# Example Usage: file util 1 helloworld hello s1
def insertFile(args,flag,data):
  # Creates a smart JSON file to keep all the information necessary
  # Compiled with a sequence of arguments
  PARAM_KEY = 1
  PARAM_CONSTRUCT = 2
  PARAM_BLOCKS_BASE = 3

  # Default output is JSON
  # Prepare to push the JSON format
  data = []
  for x in args[PARAM_BLOCKS_BASE:]:
    # Check that we have valid blocks!
    data.append(x)

  # Save into json files
  save("files/"+key,data)
  #save("files/"+key,data)

# Handles insertions for complete projects
# @Params - Key
# @Params - Constructor format ["json", "custom1"]
# @Params - File consistency [1,2,3,4 .. n]
# Example Usage: project util 
def insertProject(args,flag,data):
  # Creates a project based on file jsons on the layout of the code block
  save("projects/"+key,data)

