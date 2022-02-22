# importing the module
import sys

# function definition
def concat(s1, s2):
	print(s1 + " " + s2 )

# fetching the arguments
arg1 = sys.argv[1]
arg2 = sys.argv[2]


# calling the function
concat(arg1, arg2)
