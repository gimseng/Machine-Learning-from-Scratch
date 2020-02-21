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
            (0,1),(0,3),(1,2),(2,7),(3,4),(3,5),
            (3,6),(3,8),(3,9),(4,7),(4,8),(5,6),(6,8),
            (7,8)
            }

# add another key:item in users' dic 
# initize everyone's friends to be empty
for user in users:
    user["friends"]=[]

# add everyone's friend's name to a list call 'friends'
for i,j in friendship:
    users[i]["friends"].append(users[j]["name"])
    users[j]["friends"].append(users[i]["name"])

# let's count how many friends each person has, then sum them all to get average # of friends
def number_of_friends(user):
    print (user["name"]," has friends: ",user["friends"])
    return len(user["friends"])

total_connection=sum(number_of_friends(user) for user in users)    
num_user=len(users)
avg_connection=total_connection/len(users)
print (avg_connection,total_connection,num_user)