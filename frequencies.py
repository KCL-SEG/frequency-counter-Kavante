"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}

    for current in items:
        #checks if current is not a string 
        check = type(current) == str
        if check == False:
            current = str(current)
        frequencies[current] = frequencies.get(current,0) + 1

    return frequencies
