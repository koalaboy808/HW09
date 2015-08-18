#!/usr/bin/env python# Exercise: Presidents  # Write a program to:# (1) Load the data from presidents.txt into a dictionary.# (2) Print the years the greatest and least number of presidents were alive.#     (between 1732 and 2015 (inclusive))#     Ex. #       'least = 2015'#       'most = 2015'# Bonus: Confirm there are no ties.############################################################################### Imports# Bodydef presidents_read():	president_list = []	with open("presidents.txt") as f_in:		# read and split by new line, then list within list seperated by commas		data = f_in.read()		data = data.split("\r")		for line in data:			president_list.append(line.split(","))		# take out the president name		for line in president_list:			line.pop(0)		# convert string to number		for line in president_list:			for string in range(len(line)):				if line[string] == 'None':					line[string] = 2015				else:					line[string] = int(line[string])					#print type(string)		# inputing numbers for whole range within list		for line in president_list:			for number in range(min(line)+1,max(line)):				line.append(number)		#return president_list[0:10]		long_list = []		# one long list		for line in president_list:			for number in line:				long_list.append(str(number))		#return long_list[0:10]		president_dict = dict()		for number in long_list:			president_dict[number] = president_dict.get(number,0) + 1    	#return president_dict    	#return (president_dict)		for key, value in president_dict.items():		    if value == president_dict[min(president_dict, key=president_dict.get)]:		        #print (str(value) + "years for these years: "),		        print key,		print "\n"		for key, value in president_dict.items():		    if value == president_dict[max(president_dict, key=president_dict.get)]:		        #print (str(value) + "years for these years: "),		        print key,##############################################################################def main():  # CALL YOUR FUNCTION BELOW	(presidents_read())if __name__ == '__main__':    main()