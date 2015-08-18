#!/usr/bin/env python
# Exercise 1
# Many of the built-in functions use variable-length argument tuples. 
# For example, max and min can take any number of arguments:
# >>> max(1,2,3)
# 3
# But sum does not.
# >>> sum(1,2,3)
# TypeError: sum expected at most 2 arguments, got 3
# (1) Write a function called sumall that takes any number of arguments and 
#     returns their sum.
###############################################################################
# Imports

# Body
def sumall(*t):
	if len(t)==1:
		return t[0]
	else:
		temp = t[0]
		for count in range(len(t)-1):
			#temp = sum(t[count] + temp)
			to_add = count + 1
			temp = (t[to_add] + temp)
		return temp



###############################################################################
def main():   # DO NOT CHANGE BELOW
    print sumall(1,2,3,4,5)  # Perfect score in a cross-country meet.
    print sumall(1)
    print sumall(1,2)


if __name__ == '__main__':
    main()
