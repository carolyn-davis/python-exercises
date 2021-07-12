#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 14:51:06 2021

@author: carolyndavis
"""
# =============================================================================
# #You have rented some movies for your kids: The little mermaid (for 3 days), 
# Brother Bear (for 5 days, they love it), and Hercules (1 day, you don't know yet if they're going to like it). 
# If price for a movie per day is 3 dollars, how much will you have to pay?
# =============================================================================


b = 5
l = 3
h = 1

x = [b, l, h]
print(sum(x))

# =============================================================================
# Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, 
# they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, 
# and Facebook 350. How much will you receive in payment for this week? You worked 10 hours 
# for Facebook, 6 hours for Google and 4 hours for Amazon.
# =============================================================================

goog = 400
amaz = 380
face = 350

x = (goog * 6) + (amaz * 4) + (face * 10)
print(x)


# =============================================================================
# A student can be enrolled to a class only if the class is not full and the class schedule 
# does not conflict with her current schedule.
# =============================================================================

if capacity != "full" and sched_time not in enrolled_time:
    print("class available")





# =============================================================================
# A product offer can be applied only if people buys more than 2 items, 
# and the offer has not expired. Premium members do not need to buy a 
# specific amount of products.
# =============================================================================

if membership != "premium":
    
    if purchase >= 2 and offer != "expired":
    
        print("Congrats")
        
else: print("Congrats Premium Member")


# =============================================================================
# Create a variable that holds a boolean value for each of the following conditions:
# 
# the password must be at least 5 characters
# the username must be no more than 20 characters
# the password must not be the same as the username
# bonus neither the username or password can start or end with whitespace
# =============================================================================

username = 'codeup'
password = 'notastrongpassword'

good_password = False

if len(password) >= 5 and len(username) <= 20:
    if password != username:
        if len(username) == len(username.strip()) and len(password) == len(password.strip()):
            good_password = True 




