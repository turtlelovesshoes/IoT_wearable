from collections import defaultdict
phonebook = defaultdict(list)
contact = {}
n = 1

while(n==1):
    number1 = input("Enter the first Name: ")
    contact["First_name"] = number1
    number2 = input("Enter the Last Name: ")
    contact["Last_name"] = number2
    phone = float(input("Enter the phone number: "))
    contact["phone"] = phone

    print("The new entry of contacts looks like{}".format(contact))

    store = input("Store it in your phonebook? y/n: ")
    if store == 'y':
        phonebook['contacts'].append(contact.copy())
        print("contact added")
        print(phonebook)
    else:
        contact = []
        print("Contact removed")
        print(phonebook)
