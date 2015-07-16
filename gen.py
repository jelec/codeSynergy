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
  # First establish the code base
  # Ability to add a block of code through copy and paste and have it formatted correctly!
  if( keyExists("blocks",args[1])):
    if( "stdout" in args[2]):
      print load("blocks/"+args[1])
    # Else save the information inside the file itself
  else:
    

# Generation of a file with accordance of a JSON map 
# Description: Outputs the file into a directory
# @Params : Key - Name of the code File
# @Params : File - Name of the file we want to out (e.g. stdout or text.txt)
def codeFile(args,flag): 
  # JSON mapping files using key value stores



# Generation of a project with a set of files
# Description: Outputs the entire project
# @Params : Key - Name of the code Project
# @Params : Directory - Name of the directory used
def codeProject(args,flag):
  # JSON mapping files and storage of this

