#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 19:02:21 2023

@author: kauan
"""
from collections import Counter

from collections import defaultdict

    # not loaded by default
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
    
    users[i]["friends"].append(users[j]) # add i as a friend of j
    users[j]["friends"].append(users[i]) # add j as a friend of i


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

#SORTED THE VALUES BY CRESCENT ORDER about AXYS 1 IN TUPLE 
a = sorted(num_friends_by_id, key = lambda x: x[1], reverse=True)

# get it sorted
# by num_friends
# largest to smallest
# each pair is (user_id, num_friends)
# [(1, 3), (2, 3), (3, 3), (5, 3), (8, 3),"
# (0, 2), (4, 2), (6, 2), (7, 2), (9, 1)]



#-------EXPLAIN SESSION------------------
c = [["d", "e", "f"], ["A", "B", "C"]]
#THIS CODE MODEL READ THE VLAUES IN A MULTIDIMENSIONAL LIST
#REPLCE THE VALUE C TO MULTIFIMENSIONAL LIST
#REPLACE THE VALUE V TO FIEL/LABEL/INDEX OF THE MULTIDIMENSIONAL LIST 
#THAT WANT READ
mtd_list = [z for v in c for z in v]
#OUTPUT : ['d', 'e', 'f', 'A', 'B', 'C']
# IN THE OUTPUT EACH VALUE OF THE EACH LIST DIMENSION WAS READ END PRINTED

#-------EXPLAIN SESSION------------------



# TAKE A LOOK THE FRIENDS OF FRIENDS
def friends_of_friend_ids_bad(user):
    # "foaf" is short for "friend of a friend"
    return [foaf for friend in user["friends"]for foaf in friend["friends"]]


a3 = friends_of_friend_ids_bad(users[1])





def not_the_same(user, other_user):
    """two users are not the same if they have different ids"""
    return user["id"] != other_user["id"]


def not_friends(user, other_user):
    """other_user is not a friend if he's not in user["friends"];
    that is, if he's not_the_same as all the people in user["friends"]"""
    return all(not_the_same(friend, other_user) for friend in user["friends"])


def friends_of_friend_ids(user):
    return Counter(foaf["id"]
                   for friend in user["friends"]
                   for foaf in friend["friends"]
                   if not_the_same(user, foaf)
                   and not_friends(user, foaf))
                        # for each of my friends
                        # count *their* friends
                        # who aren't me
                        # and aren't my friends
print(friends_of_friend_ids(users[0]))# Counter({0: 2, 5:  1})




interests = [
    (0, "Hadoop"), 
    (0, "Big Data"),
    (0, "HBase"), 
    (0, "Java"),
    (0, "Spark"), 
    (0, "Storm"), 
    (0, "Cassandra"),
    (1, "NoSQL"), 
    (1, "MongoDB"), 
    (1, "Cassandra"),
    (1, "HBase"),
    (1, "Postgres"),
    (2, "Python"), 
    (2, "scikit-learn"), 
    (2, "scipy"),
    (2, "numpy"), 
    (2, "statsmodels"), 
    (2, "pandas"), 
    (3, "R"),
    (3, "Python"),
    (3, "statistics"), 
    (3, "regression"), 
    (3, "probability"),
    (4, "machine learning"), 
    (4, "regression"), 
    (4, "decision trees"),
    (4, "libsvm"),
    (5, "Python"), 
    (5, "R"), 
    (5, "Java"),
    (5, "C++"),
    (5, "Haskell"), 
    (5, "programming languages"), 
    (6, "statistics"),
    (6, "probability"), 
    (6, "mathematics"), 
    (6, "theory"),
    (7, "machine learning"), 
    (7, "scikit-learn"), 
    (7, "Mahout"),
    (7, "neural networks"), 
    (8, "neural networks"), 
    (8, "deep learning"),
    (8, "Big Data"), 
    (8, "artificial intelligence"), 
    (9, "Hadoop"),
    (9, "Java"), 
    (9, "MapReduce"), 
    (9, "Big Data")
    ]


def data_scientists_who_like(target_interest):
    return [user_id
            for user_id, user_interest in interests
            if user_interest == target_interest]


# keys are interests, values are lists of user_ids with that interest
user_ids_by_interest = defaultdict(list)
for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)
        
# keys are user_ids, values are lists of interests for that user_id
interests_by_user_id = defaultdict(list)
for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)

