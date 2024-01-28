# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 22:58:44 2024

@author: Omar Juvera
"""

# Calculate the wholesale price of a book
book_price = 24.95
discount = 0.40
shipping_cost_first_copy = 3
shipping_cost_additional_copy = 0.75
copies = 60

total_wholesale_cost = (book_price * (1 - discount) * copies) + (shipping_cost_first_copy + (shipping_cost_additional_copy * (copies - 1)))
total_wholesale_cost = round(total_wholesale_cost, 2)

print(f"What is the total wholesale cost for {copies} copies? {total_wholesale_cost}")

# We can do better!
# Fotmat output without using round)() function and extra variable
print("%s %.2f" % ("What is the total wholesale cost for 60 copies?", total_wholesale_cost))
print(f"What is the total wholesale cost for 60 copies? {total_wholesale_cost:.2f}")
print("What is the total wholesale cost for 60 copies? {wholesale:.2f}".format(wholesale=total_wholesale_cost))
