#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 14:32:50 2021

@author: carolyndavis
"""

# =============================================================================
# How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
# How many different combinations are there of 2 letters from "abcd"?
# How many different permutations are there of 2 letters from "abcd"?
# =============================================================================


# from itertools import combinations
import itertools
  
x = 'abc'    #1st list of combo

y = '123'

z = [letter+num for letter, num in itertools.product(x,y)]



# How many different combinations are there of 2 letters from "abcd"?

x= ['a', 'b', 'c', 'd']


combs = list(itertools.combinations(x, 2))

# How many different permutations are there of 2 letters from "abcd"?

perms = list(itertools.permutations(x, 2))


#3.)

import json

json.load(open('profiles.json'))

import pandas as pd

all_data = pd.read_json('profiles.json')

# =============================================================================
# Total number of users
# =============================================================================

users = all_data["_id"]


# =============================================================================
# Number of active users
# =============================================================================
active = all_data[all_data["isActive"] == True]


# =============================================================================
# Number of inactive users
# =============================================================================
in_active = all_data[all_data["isActive"] == False]


# =============================================================================
# Grand total of balances for all users
# =============================================================================
all_data['balance'] = all_data['balance'].str.replace(r'\$', '')
all_data['balance'] = all_data['balance'].str.replace(r'\,', '')
all_data['balance'] = all_data['balance'].astype(float)



total_balance = all_data["balance"].sum()

#Average balance per user
import statistics
avg_balance = all_data["balance"].mean()


# =============================================================================
# User with the lowest balance
# =============================================================================
min_balance = all_data["balance"].min()

# =============================================================================
# User with the highest balance
# =============================================================================

max_balance = all_data["balance"].max()

# =============================================================================
# Most common favorite fruit
# =============================================================================
import pandas as pd
fav_fruit = all_data["favoriteFruit"].value_counts(). idxmax()
#strawberry is the most favorite fruit
#9
# =============================================================================
# Least most common favorite fruit
# =============================================================================
unfav_fruit = all_data["favoriteFruit"].value_counts(). idxmin()   #apple
#4
# =============================================================================
# Total number of unread messages for all users
# =============================================================================
#greeting is string with ints 
output = ''
for letter in all_data["greeting"]:
  if letter isdigit():
            output += letter
    
output = int(output)
return output

       

