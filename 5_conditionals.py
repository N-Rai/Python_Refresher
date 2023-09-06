day_of_month = input ("what is the day?: ").lower()
if (day_of_month == "monday"):
    print("Have a great start")
else:
    print("Your week has already started")

friends = ["Joey", "Chandler", "Ross"]
print ("Joey" in friends)

movies_watched ={"Forest Gum", "3 Idiots", "Jab tak hain jan", "taitanic"}
user_movie = input("Enter the movie you recently watched: ").lower()

if (user_movie in movies_watched):
    print("watched!!")
else:
    print("Not watched!")

#Guess the number
number = 10
user_consent= input("Enter 'Y' if you want to play:").lower()

if (user_consent == 'y'):
    user_guess = int(input(" Guess the number: "))
    if(user_guess == number):
        print(" You have guessed it correct")
    elif (abs(user_guess - number) == 1):
        print("You were off by one")
        user_second_guess= int(input("Last guess"))
        if user_second_guess == number:
            print(" Great, you guessed it right")
        else:
            print("SORRRY!!")
    else:
        print( " Sorry you guessed it wrong")
