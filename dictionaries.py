import json
import random

faves = {"tv genre": "sci-fi", "guilty pleasure": "tik tok", "color": "pink"}
print(faves)

print(json.dumps(faves, indent=4)) #prints in json, indents, and makes easier to read. make sure to import json

print(faves["color"]) 

faves["scent"] = "floral" # adds new key/value pair
print(faves)

print(dir(faves))

print(list(faves.keys()))  

print(list(faves.values()))

for k, v, in faves.items():
    print(k, v)
    
var3 = {
    1: [random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)],
    2: [random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)],
    3: [random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)]
}

print(json.dumps(var3, indent=4))  # Pretty prints the dictionary var3

for key, value in var3.items():  # Iterates over the key-value pairs in var3
    print(key, value)
    for obj in value:  # Iterates over the elements in each sublist
        print(obj)  # Prints each element