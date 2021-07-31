# time complexity O(n), fo n = carrot_types
def get_max_value(carrot_types, capacity):
    maximum = 0
    for carrot in carrot_types:
        value = carrot['price'] * (capacity / carrot['kg'])
        if value > maximum:
            maximum = value
    return int(maximum)


print(get_max_value([{'kg': 5, 'price': 100}, {'kg': 7, 'price': 150}, {'kg': 3, 'price': 70}], 36)) # optimal value of question
print(get_max_value([{'kg': 5, 'price': 100}, {'kg': 7, 'price': 150}, {'kg': 3, 'price': 70}], 1000))
print(get_max_value([{'kg': 5, 'price': 100}, {'kg': 7, 'price': 150}, {'kg': 3, 'price': 70}], 12000))
print(get_max_value([{'kg': 5, 'price': 100}, {'kg': 7, 'price': 150}, {'kg': 3, 'price': 70}], 50000))