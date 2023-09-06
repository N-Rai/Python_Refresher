friend_ages = {"Rachel": 24, "Monika": 30, "Phoebe": 28}
print(friend_ages["Monika"])
friend_ages["Chandler"]=40
print(friend_ages)

#list of dictonaries
friends = [
    {"name": "Joey",  "age": 45, },
    {"name": "Ross",  "age": 40, },
    {"name": "Chandler",  "age": 35, }
    ]

print(friends)
print(friends[1])
print(friends[0]["name"])

for friend in friend_ages:
    print(f"{friend}: {friend_ages[friend]}")
    
for friend, ages in friend_ages.items():
    print(f"{friend}: {ages} ")
    
ages_values = friend_ages.values()
print(sum(ages_values)/len(ages_values))
