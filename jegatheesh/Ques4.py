def remove_duplicate():
    name=set()
    return [x for x in list if not(x in name or name.add(x))]
print (remove_duplicate([1 , 2, 4, 5, 6], 5))
