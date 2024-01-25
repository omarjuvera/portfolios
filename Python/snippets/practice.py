# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#How to concat a string and a number
year_message = 'The year is'
year_current = 2018

print("Concat via arguments:", year_message, year_current)
print("Concat via arguments with separators:", year_message, year_current, sep=", ")
print("Concat via interpolation: %s %s" % (year_message, year_current))
print(f"Concat via f-string: {year_message} {year_current}")
print("Concat via str.format: {m} {y}".format(m = year_message, y = year_current) )



#Multiple vaariable assignments is LEGAL
a = b = c = 2
print("%s%s" % ("Variable value: ", b) )


#Calculate the radius of a sphere
#The volume of a sphere with radius r is 4/3 π r3. What is the volume of a sphere with radius 5?
import math
pi = math.pi
r = int(input("What is the radius?: "))
radius = (4/3) * pi * r**3
radiusRounded = round(radius, 2)

# Notice the suttle difference in the string, between the first print and the rest
print("%s%s" % ("Your Radius is ", radiusRounded) )
print("%s %.2f" % ("Your Radius is", radius) )

# % interpolation documentation: https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting


#calculate the wholesale price of a book 
#Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?
book_price = 24.95
discount = 0.40
Shipping_Cost1 = 3
Shipping_Cost2 = .75
copies = 60

wholesale = ( (book_price * discount) *60) + (Shipping_Cost1 + (Shipping_Cost2 * (copies -1) ) )
wholesale = round(wholesale, 2)
print("%s%s" % ("What is the total wholesale cost for 60 copies? A: ", wholesale))

x = "awesome"

def myfunc():
  print("Python is", x)

myfunc()