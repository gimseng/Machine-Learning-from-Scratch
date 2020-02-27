users=[
    {"id": 0, "name": "John"},
    {"id": 1, "name": "James"},
    {"id": 2, "name": "Smith"},
    {"id": 3, "name": "Sue"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Odin"},
    {"id": 6, "name": "Athena"},
    {"id": 7, "name": "Maisel"},
    {"id": 8, "name": "Andrew"},
    {"id": 9, "name": "Juan"},
]

friendship={
            (0,1),(0,3),(1,3),(2,7),(3,4),(3,5),
            (1,4),(4,5)
            }

# add another key:item in users' dic 
# initize everyone's friends to be empty
for user in users:
    user["friends"]=[]

#print (users,"YYY \n")
# add everyone's friend's name to a list call 'friends'
for i,j in friendship:
    users[i]["friends"].append(users[j]["id"])
    users[j]["friends"].append(users[i]["id"])
    

#print (users[0])
#print ("\n")
# let's count how many friends each person has, then sum them all to get average # of friends
def number_of_friends(user):
    #print (user["name"]," has friends: ",user["friends"])
    return len(user["friends"])

total_connection=sum(number_of_friends(user) for user in users)    
num_user=len(users)
avg_connection=total_connection/len(users)
#print (avg_connection,total_connection,num_user)

num_friends_by_id=[(user["id"],number_of_friends(user)) for user in users]
#print(num_friends_by_id)

# Note the key of the sorted involves a slightly different implementation to unpack due to Python 3.0
new_sorted=sorted(num_friends_by_id, key=lambda x: x[1], reverse=True)
#print(new_sorted)
#print (friendship)
def friends_of_friend(user):
    return [foaf
            for friend in user["friends"] 
            for foaf in users[friend]["friends"]
            ]
#print(friends_of_friend(users[1]))

from collections import Counter, defaultdict

def not_the_same(user,other_user):
    return user!= other_user

def not_friends(user, other_user):
    return all(not_the_same(friend,other_user) for friend in users[user]["friends"])

##print ("TEST:",users[1]["friends"])
#print(not_friends(0, 2))
def friends_of_friend_ids(user):
    return Counter(foaf
                    for friend in users[user]["friends"]
                    for foaf in users[friend]["friends"]
                    if not_the_same(user,foaf)
                    and not_friends(user,foaf))
#print (friends_of_friend_ids(1))
interests=[(0,"Hadoop"),(0,"Big data"),(0,"Spark"),(1,"Spark"),(2,"Big data"),(3,"Hadoop"),(4,"Spark")]

def data_scientist_who_like(target_interest):
    return [user_id for user_id, user_interest in interests if user_interest==target_interest]

#print (data_scientist_who_like("Spark"))
user_ids_by_interest=defaultdict(list)

for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)

#print(user_ids_by_interest['Big data'])
salaries_and_tenure=[(83000,8.7),(75000,7.3),(50000,5.0),(50200,5.2),(54000,5.4),(18000,1.5),(20500,2.3)]
salary_by_tenure=defaultdict(list)

for salary, tenure in salaries_and_tenure:
    salary_by_tenure[tenure].append(salary)


def tenure_bucket(tenure):
    if tenure<2:
        return "less than two"
    elif tenure <5:
        return "between two and five"
    else:
        return "more than 5"


salary_by_bucket = defaultdict(list)
for salary, tenure in salaries_and_tenure:
    bucket = tenure_bucket(tenure)
    #print(tenure, bucket)
    salary_by_bucket[bucket].append(salary)
print (salary_by_bucket)
