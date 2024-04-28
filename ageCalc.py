#get the user input and save it in a variable
print("Welcome to the age in days calculator! Let's get started.")
user_name = input ("Input your name: ")
user_age = input ("Input your age: ")

#print it out to the screen
print("Hey there, " + user_name + "!" + " You are " + user_age + " years old.")

#check out how old they are in days
dayAge = int(user_age) * 365

#print out to the screen
#Apparently python cannot concatenate non string values unless it's an fString so had to print out age separately
print("So, your age in days is: ")
print(dayAge)

#this is how the fstring works
print(f"Just to confirm..., yes you are {dayAge} days old.")
