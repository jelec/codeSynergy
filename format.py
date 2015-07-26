import os
import sys

# Format a block with string substitutions
def block(data, formatter):
  args = formatter.split(':')
  length = len(args)
  newData = data

  if( len(args)%2 != 0):
    # Remove the last argument
    length = length - 1

  # Replace substrings
  for i in range(0,length-1):
    if( i%2 == 0): # On every even number
      newData = newData.replace(args[i], args[i+1])

  # Check out the new data stream
  return newData
