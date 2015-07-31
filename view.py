import os 
import sys
from util import save,load,mkdir,cont,log
from globalVars import set,get

def allBlocks(args,flag,data):
	if( len(args) >= 2):
		_list = os.listdir("blocks")
		for x in _list:
			# We could also parse N number of arguments
			flag = 1
			for a in args[1:]:
				if( a.lower() not in x.lower()):
					flag = 0
			if( flag == 1):
				print x
	else:
		print os.listdir("blocks")
		
def allFiles(args,flag,data):
	if(len(args) > 2):
		_list = os.listdir("files")
		for x in _list:
			if( args[1] in _list):
				print x
	else:
		print os.listdir("files")
def allProjects(args,flag,data):
	print os.listdir("projects")
