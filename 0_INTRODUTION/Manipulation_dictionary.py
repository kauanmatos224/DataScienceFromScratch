#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 19:02:21 2023

@author: kauan
"""

# DICTIONARY ABOUT ID AND NAMES
users = [
{ "id": 0, "name": "Hero" },
{ "id": 1, "name": "Dunn" },
{ "id": 2, "name": "Sue" },
{ "id": 3, "name": "Chi" },
{ "id": 4, "name": "Thor" },
{ "id": 5, "name": "Clive" },
{ "id": 6, "name": "Hicks" },
{ "id": 7, "name": "Devin" },
{ "id": 8, "name": "Kate" },
{ "id": 9, "name": "Klein" }
]

print(users)


# CONECTIONS OF FRIENDS IN DATAFRAME
friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
(4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)] 

#PUT NEW KEY IN LIST OF THE DICTIONARY - KEY --> "FRIENDS"
for user in users:
    user["friends"] = []

print(users)


#POPULATE THE KEY FRIENDS WITH VALUES OF THE FRIENDSHIPS
for i, j in friendships:
    # this works because users[i] is the user whose id is i
    
    users[i]["friends"].append(users[j]["id"]) # add i as a friend of j
    users[j]["friends"].append(users[i]["id"]) # add j as a friend of i


#----CALCULATION OF THE AVERAGE OF THE FRINDSHIP AMONG PEOPLE IN DATAFRAME------

#FUNCTION - RETURN THE USER["FRIENDS"] SIZE 
def number_of_friends(user):
    """how many friends does _user_ have?"""
    return len(user["friends"])# length of friend_ids list


#LOOP - SOME CALCULATION OF THE FRIENDS FOR EACH PEOPLE IN DATAFRAME USERS
total_connections = sum(number_of_friends(user) for user in users)    

#RECEIVE THE AMOUNT OF PEOPLE IN DATAFRAME
num_users = len(users)

#AVERAGE - AMOUNT OF PEOPLE DIVIDED BY AMOUNT OF FRIENDSHIPS
avg_connections = total_connections / num_users

#----CALCULATION OF THE AVERAGE OF THE FRINDSHIP AMONG PEOPLE IN DATAFRAME------

# CREATE THE LIST WITH NUMBER FRIENDS VALUES BY PEOPLE ID VALUES
num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]

#SORTED THE VALUES BY CRESCENT ORDER
a = sorted(num_friends_by_id, key = lambda x: x[1], reverse=True)

# get it sorted
# by num_friends
# largest to smallest
# each pair is (user_id, num_friends)
# [(1, 3), (2, 3), (3, 3), (5, 3), (8, 3),
# (0, 2), (4, 2), (6, 2), (7, 2), (9, 1)]