import os 
import sys
from util import save,load,mkdir,cont,log, keyExists
from globalVars import set,get

# Code Generation Functions : Proct through command line

# Generation functions for key value stores can be maintained here
# Description : Outputs a codeblock either through a chat or something
# @Params : Key - Name of the codeblock
# @Params : File - Name of the file we want to insert it to (if stdout)
# @Params : Line - Line in the file 
def codeBlock(args,flag):
  PARAM_KEY = 1;
  PARAM_FILE = 2;
  PARAM_LINE = 3;
  # Ability to add a block of code through copy and paste and have it formatted correctly!
  if( keyExists("blocks",args[PARAM_KEY])):
    block = load("blocks/"+args[PARAM_KEY]);
    if(len(args) < 3 ): # No file specified
      print block
    else:
      if( len(args) < 3): 
        save(args[PARAM_FILE],block)
      elif( len(args) > 3): # Argument for line 
        save(args[PARAM_FILE],block,args[PARAM_LINE])
  else:
    print "Error: Block does not exist"

# Generation of a file with accordance of a JSON map 
# Description: Outputs the file into a directory
# @Params : Key - Name of the code File
# @Params : File - Name of the file we want to out (e.g. stdout or text.txt)
def codeFile(args,flag): 
  # JSON mapping files using key value stores
  if( keyExists("files",args[1])):
    if( "stdout" in args[2]):
      print load("files/"+args[1])
  else:
    print "Error: File does not exist"

# Generation of a project with a set of files
# Description: Outputs the entire project
# @Params : Key - Name of the code Project
# @Params : Directory - Name of the directory used
def codeProject(args,flag):
  # JSON mapping files and storage of this
  if( keyExists("projects",args[1])):
    if( "stdout" in args[2]):
      print load("projects/"+args[1])
  else:
    print "Error: Project does not exist"

