import os
from util import log, error

# Remove a block
def deleteBlock(args, flag, data):
  if( args[1] in os.listdir("blocks")):
    os.remove("blocks/"+args[1])
    log("Block deleted.")
  else:
    error("Error: No such block.")

def deleteFile(args, flag, data):
  if( args[1] in os.listdir("files")):
    os.remove("files/"+args[1])
    log("File deleted.")
  else:
    error("Error: No such file.")

def deleteProject(args, flag, data):
  if( args[1] in os.listdir("blocks")):
    os.remove("projects/"+args[1])
    log("Project deleted.")
  else:
    error("Error: No such project.")