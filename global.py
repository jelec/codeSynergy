# Global State engine : for cross communication
import Queue

# For service instantiation
q = Queue.Queue()

def push(item):
  q.put(item)

def isQueueEmpty():
  return q.empty()

def pop(item):
  return q.get()

# For storage

storage = {}

def set(key,value):
  storage[key] = value

def get(key):
  return storage[key]
