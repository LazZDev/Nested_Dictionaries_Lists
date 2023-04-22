x = [[5, 2, 3], [10, 8, 9]]
students = [
    {"first_name": "Michael", "last_name": "Jordan"},
    {"first_name": "John", "last_name": "Rosales"},
]
sports_directory = {
    "basketball": ["Kobe", "Jordan", "James", "Curry"],
    "soccer": ["Messi", "Ronaldo", "Rooney"],
}
z = [{"x": 10, "y": 20}]
# Changing the value in the nested list x
x[1][0] = 15
print(x)
# Updating the 'last_name' value in the first dictionary of students list
students[0]["last_name"] = "Bryant"
print(students)
# Updating the first element of the "soccer" list in sports_directory dictionary
sports_directory["soccer"][0] = "Andres"
print(sports_directory)
# Updating the value of the "y" key in the first dictionary of z list
z[0]["y"] = 30
print(z)
# Function to iterate through a list of dictionaries and print key-value pairs


def iterate_dictionary(some_list):
    for dictionary in some_list:
        for key, value in dictionary.items():
            print(f"{key} - {value}", end=", ")
        print()


students = [
    {"first_name": "Michael", "last_name": "Jordan"},
    {"first_name": "John", "last_name": "Rosales"},
    {"first_name": "Mark", "last_name": "Guillen"},
    {"first_name": "KB", "last_name": "Tonel"},
]
iterate_dictionary(students)

# Function to iterate through a list of dictionaries and print the value of a specified key


def iterate_dictionary2(key_name, some_list):
    for dictionary in some_list:
        print(dictionary[key_name])


students = [
    {"first_name": "Michael", "last_name": "Jordan"},
    {"first_name": "John", "last_name": "Rosales"},
    {"first_name": "Mark", "last_name": "Guillen"},
    {"first_name": "KB", "last_name": "Tonel"},
]
iterate_dictionary2("first_name", students)

iterate_dictionary2("last_name", students)

# Function to print the number of items and the items themselves for each key in a dictionary


def print_info(some_dict):
    for key, value in some_dict.items():
        print(f"{len(value)} {key.upper()}")
        for item in value:
            print(item)
        print()


dojo = {
    "locations": ["San Jose", "Seattle", "Dallas", "Chicago", "Tulsa", "DC", "Burbank"],
    "instructors": [
        "Michael",
        "Amy",
        "Eduardo",
        "Josh",
        "Graham",
        "Patrick",
        "Minh",
        "Devon",
    ],
}
print_info(dojo)
