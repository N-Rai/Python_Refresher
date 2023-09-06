numbers = [1,3,5]
doubled =[]
doubled_list = [num*2 for num in numbers]

for num in numbers:
    doubled.append(num * 2)
    
print(doubled, doubled_list)

#["Your desired output", "For Loop", "Condition"]

friends = ["Joey", "Chandler", "Ross", "Rachel", "Monika", "Phoebe"]
friends_with_R = []

for friend in friends:
    if friend.startswith("R"):
        friends_with_R.append(friend)
print(friends_with_R)

friends_starts_R = [friend for friend in friends if friend.startswith("R")]
print(friends_starts_R)

print(friends is friends_starts_R) # is FALSE because a new list is created while using list comprehension
print("friends: ",id(friends), "starts_R: " ,id(friends_starts_R))