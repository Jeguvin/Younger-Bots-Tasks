def second_largest_number(game):
    unique_numbers = list(set(game))  
    unique_numbers.sort()             
    
    if len(unique_numbers) >= 2:
        return unique_numbers[-2]     
    else:
        return None

print(second_largest_number([10, 20, 30, 40, 50, 77, 98, 2, 765]))
