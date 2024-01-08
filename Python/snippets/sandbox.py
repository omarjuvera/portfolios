# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#How to concat a string and a number
current_year_message = 'Year is '
current_year = 2018

print("%s%s" % (current_year_message, current_year))

#Multiple vaariable assignments is LEGAL
a = b = c = 2
print("%s%s" % ("Variable value: ", b) )

#Calculate the radius of a sphere
import math
pi = math.pi
r = int(input("What is the radius?: "))
radius = round( (4/3) * pi * r**3, 2)
print("%s%s" % ("Your Radius is ", radius) )

#calculate the wholesale price of a book 
book_price = 24.95
discount = 0.40
Shipping_Cost1 = 3
Shipping_Cost2 = .75
copies = 60

wholesale = ( (book_price * discount) *60) + (Shipping_Cost1 + (Shipping_Cost2 * (copies -1) ) )
wholesale = round(wholesale, 2)
print("%s%s" % ("What is the total wholesale cost for 60 copies? ", wholesale))

