import gen
import create
import misc
import view
from util import save,load,mkdir, log

# Command Help
def help(args,flag,data):
  if(len(args) < 2):
    log("List of avaliable commands (shortcuts) :\n create (c), block (b). \n Type in 'help [command]' for more information");  
  else:
    if args[1] in routes:
      log(helpGuide[args[1]])

# Command routing 
routes = {  "b" : gen.codeBlock,
            "c" : create.insertBlock,
            "rm" : create.deleteBlock,
            "help": help,
            "block" : gen.codeBlock,
            "create" : create.insertBlock,
            "ls" : view.allBlocks,
            "lb" : view.allBlocks,
            "lf" : view.allFiles,
            "lp" : view.allProjects,
            "rb" : create.deleteBlock,
            "rp" : create.deleteProject,
            "rf" : create.deleteFile,}

helpGuide = {"b" : "\"b\" - Write out code block \n Description: Output a code block.\n Parameters:\n 1. Key of Codeblock \n 2. File [Optional] \n 3. Line [Optional]",
             "block": "\"block\" - write out code block \n Description: Output a code block.\n Parameters:\n 1. Key of CB \n 2. File [Optional] \n 3. Line [Optional]",
             "c" : "\"c\" - Create a code block \n Binds recallable key to code segement.\n Parameters:\n 1. Key ",
             "create" : "\"create\" - Create a code block \n Binds recallable key to code segement.\n Parameters:\n 1. Key "}
