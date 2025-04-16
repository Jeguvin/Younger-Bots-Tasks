from collections import Counter

def frequently_requested_element(lst):
    return Counter(lst).most_common(1)[0][0]

print(frequently_requested_element([1, 2, 2, 3, 3, 4, 2, 5]))
