names_string = "Jamie, Ben, Jenny, Michael, Cloe"

import random

names = names_string.split(", ")

num_items = len(names)

random_choice = random.randint(0, num_items -1)

#print(random_choice)

payee = names[random_choice]

print(payee + " is going to buy the meal today!")
