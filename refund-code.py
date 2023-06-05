purchase_date = int(input('How many days ago have you purchased the item? '))
used_item = input('Have you used the item at all [y/n]? ')
broken_item = input('Has the item broken down on its own [y/n]? ')

if(broken_item =='y' or (purchase_date <= 10 and used_item == 'n')):
    print('You can get a refund.')
else:
    print('You cannot get a refund.')

