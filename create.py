import os 
import sys
from util import save,load,mkdir,cont,log, printBlue
from globalVars import set,get

# Handle insertions for code, saves code blocks
def insertCodeBlock(args,flag, data):
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
def insertFile(key,data):
  # Creates a smart JSON file to keep all the information necessary
  save("files/"+key,data)

# Handles insertions for complete projects
def insertProject(key,data):
  # Creates a project based on file jsons on the layout of the code block
  save("projects/"+key,data)