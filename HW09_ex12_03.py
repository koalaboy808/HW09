#!/usr/bin/env python
# Exercise 3  
# (1) Write a function called most_frequent that takes a string and prints the
#     chars in decreasing order of frequency. (compare and print in lowercase)
# Ex. >>> most_frequent("aaAbcc")
#     a  
#     c
#     b
###############################################################################
# Imports

# Body

def most_frequent(s):
   
    # convert string s into tuple... also remove spaces and make all chars lowercase
    s = list(s.lower().replace(" ",""))
    for char in s:
        if ord(char) not in range(97,123):
            s.remove(char)

    # create dictionary with value being the frequency of char
    dict_list = {}
    for char in s:
        dict_list[char] = dict_list.get(char,0) + 1

    # convert dictionary to a list of tuples with freq being first of the pair
    tuple_list = []
    for key, value in dict_list.items():
        tuple_list.append((value, key))

    # order tupe_list
    tuple_list.sort(reverse=True)

    # only list the chars
    final_list = []
    for chars, freq in tuple_list:
        final_list.append(freq)

    print tuple_list
    print final_list

###############################################################################
def main():   # DO NOT CHANGE BELOW
    print("Example 1:")
    most_frequent("abcdefghijklmnopqrstuvwxyz")
    print("\nExample 2:")
    most_frequent("The quick brown fox jumps over the lazy dog")
    print("\nExample 3:")
    most_frequent("Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
    "sed do eiusmod tempor incididunt ut labore et dolore magna "
    "aliqua. Ut enim ad minim veniam, quis nostrud exercitation "
    "ullamco laboris nisi ut aliquip ex ea commodo consequat. "
    "uis aute irure dolor in reprehenderit in voluptate velit "
    "esse cillum dolore eu fugiat nulla pariatur. Excepteur sint "
    "occaecat cupidatat non proident, sunt in culpa qui officia "
    "deserunt mollit anim id est laborum.")
    print("\nExample 4:")
    most_frequent("Squdgy fez, blank jimp crwth vox!")

if __name__ == '__main__':
    main()
