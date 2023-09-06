#Guess the number using while loop
number = 10

while True:
    user_consent= input("Would you like to play? (Y/n)")
    
    if user_consent == "n":
        break
    user_guess = int(input(" Guess the number: "))
    if(user_guess == number):
        print(" You have guessed it correct")
    elif (abs(user_guess - number) == 1):
        print("You were off by one")
    else:
        print( " Sorry you guessed it wrong")

# For loop
friends = ["Joey", "Chandler", "Ross"]

for friend in friends:
    print(f"{friend} is my friend.")
   
#Even numbers
even_num_sets = set() 
even_num_list = []
even_num_tuple = ()
for x in range(10):
    if x%2 == 0:
        even_num_sets.add(x)
        even_num_list.append(x)
        even_num_tuple += (x,)
        
print(even_num_sets, even_num_list, even_num_tuple)

#Average grade
grades = [90, 85, 75, 50, 95]

total_grades = 0
counter = 0
for x in grades:
    total_grades += x
    counter += 1

average_grade = total_grades/counter
print(f"average grade is using for loop: {average_grade}")
    
total = sum(grades)
amount = len(grades)
average = total/amount
print(f" Average grade is: {average}")

