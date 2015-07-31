import gen
import create
import misc
import view
import delete
from util import save,load,mkdir,log,clear

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
            "p" : create.insertModule,
            "f" : gen.codeFile,
            "cf" : create.insertFile,
            "rm" : delete.deleteBlock,
            "clear": clear,
            "help": help,
            "block" : gen.codeBlock,
            "create" : create.insertBlock,
            "ls" : view.allBlocks,
            "lb" : view.allBlocks,
            "lf" : view.allFiles,
            "lp" : view.allProjects,
            "rb" : delete.deleteBlock,
            "rp" : delete.deleteProject,
            "rf" : delete.deleteFile,
            "setTag" : misc.setTag,
            "clearTag": misc.clearTag,
            "mkdir": misc._mkdir}

helpGuide = {"b" : "\"b\" - Write out code block \n Description: Output a code block.\n Parameters:\n 1. Key of Codeblock \n 2. File [Optional] \n 3. Line [Optional]",
             "block": "\"block\" - write out code block \n Description: Output a code block.\n Parameters:\n 1. Key of CB \n 2. File [Optional] \n 3. Line [Optional]",
             "c" : "\"c\" - Create a code block \n Binds recallable key to code segement.\n Parameters:\n 1. Key ",
             "create" : "\"create\" - Create a code block \n Binds recallable key to code segement.\n Parameters:\n 1. Key "}
