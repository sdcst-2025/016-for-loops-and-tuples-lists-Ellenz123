# Task 4
# Access list values

"""
Ask the user to enter in a number less than 10
Print out the list element that corresponds to that
position in the tuple
"""

people=("John","Tyler","Dash","Kieran","Jayson","Tomoki","Minji","Dawson","Hewitt","Josh","Anson","Cole")

for i in people:
    x=input("Enter an integer less than 10: ")
    x=int(x)
    if x <= 10:
        print(people[x])
        break
else:
    print("Try again and enter a number less than 10.")