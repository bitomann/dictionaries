# Instructions
# 1. Define a dictionary that contains information about several members 
# of your family. Use the following example as a template.

my_family = {
    "wife": {
        "name": "Angela",
        "age": 37
    },
    "son": {
        "name": "Phoenix",
        "age": 9
    },
    "oldest daughter": {
        "name": "Madeleine",
        "age": 7
    },
    "youngest daughter": {
        "name": "Lilianna",
        "age": 1.5
    }
}
# 2. Using a dictionary comprehension, produce output that looks like the 
# following example.
# print(my_family.keys())
# print(my_family.values())
# print(my_family.items())

for (key, value) in my_family.items():
    print(f"{value['name']} is my {key} and is {value['age']} years old")
    

# Krista is my sister and is 42 years old
# Helpful hint: To convert an integer into a string in Python, it's 
# str(integer_value)