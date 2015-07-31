import os 
import sys
from util import save,load,mkdir,cont,log, keyExists, loadJSON, error, printClear
from globalVars import set,get
import json
import format

# Code Generation Functions : Proct through command line

# Generation functions for key value stores can be maintained here
# Description : Outputs a codeblock either through a chat or something
# @Params : Key - Name of the codeblock
# @Params : File - Name of the file we want to insert it to (if stdout)
# @Params : Line - Line in the file 
# @Params : Specified Replacements - Name of the command [GET:PUT]
def codeBlock(args,flag,data):
  PARAM_KEY = 1
  PARAM_FORMATTER = 2
  PARAM_FILE = 3
  PARAM_LINE = 4
  ARGUMENTS = len(args)-1

  # Ability to add a block of code through copy and paste and have it formatted correctly!
  if( keyExists("blocks",args[PARAM_KEY])):
    block = load("blocks/"+args[PARAM_KEY])
    # Format these blocks
    if(ARGUMENTS == PARAM_FORMATTER): # Format blocks
      block = format.block(block, args[PARAM_FORMATTER])
    if(ARGUMENTS <= PARAM_FORMATTER): # No file specified
      log(block)
    else:
      if(ARGUMENTS == PARAM_FILE): 
        log("Saving to file "+ args[PARAM_FILE] )
        save(args[PARAM_FILE],block)
      elif(ARGUMENTS >= PARAM_LINE): # Argument for line 
        save(args[PARAM_FILE],block,args[PARAM_LINE])
  else:
    error("Error: Block does not exist")

def createFile(_file, formating, formatFlag):
  out = "" # Output string
  for x in _file:
      block = str(load("blocks/"+ x))
      if(formatFlag): # Alter all the blocks in said fashion
        block = format.block(block, formating)     
      out += block
      out += "\n" # Adds some spacing between blocks

  return out


# Generation of a file with accordance of a JSON map 
# Description: Outputs the file into a directory
# Also allows blocks to be substituted inside blocks
# @Params : Key - Name of the code File
# @Params : File - Name of the file we want to out (e.g. stdout or text.txt)
def codeFile(args,flag,data): 
  PARAM_KEY = 1;
  PARAM_FILE = 2; # Output file location
  PARAM_FORMATTER = 3
  ARGUMENTS = len(args)-1
  # Ability to add a block of code through copy and paste and have it formatted correctly!
  if( keyExists("files",args[PARAM_KEY])):
    _file = json.loads(load("files/"+args[PARAM_KEY]));
    out = ''

    # loadJSON 
    for x in _file:
      block = str(load("blocks/"+ x))
      if(ARGUMENTS == PARAM_FORMATTER): # Alter all the blocks in said fashion
        block = format.block(block, args[PARAM_FORMATTER])     
      out += block
      out += "\n" # Adds some spacing between blocks

    # No file specified
    if(len(args) < 3 ): 
      log(out)
    else:
      log("Saving to file "+ args[PARAM_FILE] )
      save(args[PARAM_FILE],out)
  else:
    error("Error: File does not exist")

# Generation of a project with a set of files
# Description: Outputs the entire project
# @Params : Key - Name of the code Project
# @Params : Directory - Name of the directory used
def codeProject(args,flag,data):
  PARAM_KEY = 1
  PARAM_PATH = 2
  PARAM_FORMATTER = 3
  ARGUMENTS = len(args)-1

  # JSON mapping files and storage of this
  if( keyExists("projects",args[1])):
    if( "stdout" in args[2]):
      project = json.loads(load("projects/"+args[PARAM_KEY])); # Uses key value storage
      directory = args[PARAM_PATH] + "/" + args[PARAM_KEY]
      
      mkdir(directory)
      for x in project.keys(): # Reflect that with here
        _file = json.loads(load("files/"+x));
        out = '';
        for y in _file:
          block = str(load("blocks/"+ y))
          if(ARGUMENTS == PARAM_FORMATTER): # Alter all the blocks in said fashion
            block = format.block(block, args[PARAM_FORMATTER])     
          out += block
        # Output the file with the correct file name
        save(directory + "/" + project[x],out)

  else:
    error("Error: Project does not exist")

