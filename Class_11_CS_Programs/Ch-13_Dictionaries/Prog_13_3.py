# Program 13.3: Search Key in Dictionary
# KEYWORD EXPLANATION:
# Key Lookup (dict[key]) retrieves corresponding value stored under given key.

phonebook = {"Aman": "9876543210", "Neha": "8765432109", "Rohan": "7654321098"}

name = input("Enter name to search in phonebook: ")

if name in phonebook:
    print(f"Phone number for {name} is {phonebook[name]}")
else:
    print(f"Contact '{name}' not found in phonebook.")
