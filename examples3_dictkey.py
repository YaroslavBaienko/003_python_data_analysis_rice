"""
Checking for keys in a dictionary.
"""

print("Using 'in'")
print("==========")

mapping = {1: 5, 8: -3, 7: 22, 4: 13, 22: 17}

# Keys
print(1 in mapping)
print(8 in mapping)

# Values
print(5 in mapping)
print(-3 in mapping)

# Both
print(22 in mapping)

# Neither
print(82 in mapping)

print("")

print("Protecting from Errors")
print("======================")

keys = [8, 14, 22, 25]

# for key in keys:
#    print(key, mapping[key])

for key in keys:
    if key in mapping:
        print(key, mapping[key])
    else:
        print("{} not in mapping".format(key))


print("Issues with Keys")
print("================")

# Be careful with what you use as keys!
# If all keys are of the same type, you won't run
#  into these issues
mapping = {4.0: 2, 'a': 3, True: 'true', False: 9}
print(mapping)

mapping[1] = 7
print(mapping)

mapping[0] = 'false'
print(mapping)

mapping[4] = 7
print(mapping)

mapping['A'] = 'abc'
print(mapping)


def lookup(contacts, name):
    """
    Lookup name in contacts and return phone number.
    If name is not in contacts, return an empty string.
    """
    if name in contacts:
        return contacts[name]
    else:
        return "Контакт не сохранен"


contacts = {
    'Elizabeth': +380665511338,
    'Yaroslav': +380631458976
}

name = input('Введите имя контакта: ')
result = lookup(contacts=contacts, name=name)
print(result)

# Notice that we first need to check if the name is actually a key in the dictionary (line 6).  If you try to index into a dictionary with a key that does not exist, you will get an error.  You could also use the get\color{red}{\verb!get!}get method to provide a default value in the case where the key does not exist in the dictionary:


def lookup2(contacts, name):
    """
    Lookup name in contacts and return phone number.
    If name is not in contacts, return an empty string.
    """
    return contacts.get(name, "")


result2 = lookup2(contacts=contacts, name=name)
print(result2)


def print_contacts(contacts):
    """
    Print the names of the contacts in our contacts list.
    """
    for name in contacts:
        print(name)


print(contacts)


def print_contact_list(contacts):
    """
    Print the names and phone numbers of the contacts in
    our contacts list.
    """
    for name, number in contacts.items():
        print(name, ":", number)


result3 = print_contact_list(contacts)
result3


def print_ordered(contacts):
    """
    Print the names and phone numbers of the contacts
    in our contacts list in alphabetical order.
    """
    keys = contacts.keys()
    names = sorted(keys)
    for name in names:
        print(name, ":", contacts[name])


result3 = print_ordered(contacts=contacts)
result3


def add_contact(contacts, name, number):
    """
    Add a new contact (name, number) to the contacts list.
    """
    if name in contacts:
        print(name, "is already in contacts list!")
    else:
        contacts[name] = number


def update_contact(contacts, name, newnumber):
    """
    Update an existing contact's number in the contacts list.
    """
    if name in contacts:
        contacts[name] = newnumber
    else:
        print(name, "is not in contacts list!")


while True:
    name2 = input("Input name: ")
    newnumber = input("Input number")
    update_contact(contacts=contacts, name=name2, newnumber=newnumber)
    if_continue = input("Continue? ")
    if if_continue == "yes":
        continue
    if if_continue == "no":
        break

print(contacts)
