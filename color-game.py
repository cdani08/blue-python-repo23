favorite_color = 'pink'

user_input = input('Can you guess my favorite color?')

while user_input != favorite_color:
    print ("Try again...")
    user_input = input('Can you guess my favorite color?')
print ('Correct!')