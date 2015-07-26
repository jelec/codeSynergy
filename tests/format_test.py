import sys
sys.path.insert(0, '../')
import format

def test(entry, outcome, tests, testspassed):
	tests = tests + 1
	if( entry == outcome):
		testspassed = testspassed + 1

def hello():
	print "hello world"

def main():
  tests = 0
  testspassed = 0
  print "-------- Welcome to the format test ----------"
  print "----------------------------------------------"
  test("world world world",format.block("hello world hello", "hello:world"),tests, testspassed)
  print "Test Result " + str(testspassed) + "/" + str(tests) + " have passed."


if __name__ == '__main__':
	main()