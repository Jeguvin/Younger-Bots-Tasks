name_input = input("Enter the name: ")

def name_count(s):
    return sum(1 for char in s.lower() if char in 'jegatheesh')

print(name_count(name_input))
