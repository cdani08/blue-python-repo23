numbers = [0, 1, 2, 3, 4, 5]

print(numbers)

for number in numbers:
    print(number) #prints vertically 

print(type(numbers)) #type: shows the data type

more_numbers = list(range(0,31)) #prints range of numbers in list so you dont have to hardcode numbers

print(more_numbers)

print(more_numbers[-1]) #shows last element of list

#nesting lists
var=[2,4,5],[8,4,9],[7,9,1]

for obj in var:
    print(obj) #prints out neseted lists
    for ele in obj:
        print(ele)
