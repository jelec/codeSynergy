import os
import sys

debug = 1

# Create a directory function
def mkdir(dir):
	if not os.path.exists(dir):
	    os.makedirs(dir)
	return

# Load a file function | Add other hooks later
def load(path):
  with open(path, 'r') as content_file:
    content = content_file.read()
  return content

# Write file function 
def save(path, data):
  with open(path,'w') as f:
    f.write(data)

def log(string):
  if(debug):
    print string
