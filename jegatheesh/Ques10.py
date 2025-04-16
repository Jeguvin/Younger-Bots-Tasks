def non_repeating_character(name):
    for char in name:
        if name.count(char) == 1: 
            return char
    return None  

print(non_repeating_character("jegatheesh"))
