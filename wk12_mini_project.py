import random
import string

instances = int(input("How many instances do you want created? "))
department = input("What is your department? ")
characters = string.ascii_letters + string.digits

for _ in range(instances):
    random_string = ''.join(random.choice(characters) for _ in range(10))
    print(department + random_string)
