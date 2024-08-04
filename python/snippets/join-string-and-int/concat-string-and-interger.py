# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 22:40:56 2024

@author: Omar Juvera
"""

# Concatenating a string and an interger
year_message = 'The year is'
year_current = 2018

# Concat via arguments
print("Concat via arguments:", year_message, year_current)

# Concat via arguments with separators
print("Concat via arguments with separators:", year_message, year_current, sep=", ")

# Concat via interpolation
# %s = String
# conversion types documentation: https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting
print("Concat via interpolation: %s %s" % (year_message, year_current))

# Concat via f-string
print(f"Concat via f-string: {year_message} {year_current}")

# Concat via str.format
print("Concat via str.format: {} {}".format(year_message, year_current))
print("Concat via str.format: {m} {y}".format(m=year_message, y=year_current))
