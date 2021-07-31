def get_max_value(carrot_types, capacity):  
    values = [0] * (capacity + 1)
    for max_capacity in range(1, capacity + 1):
        for carrot in carrot_types:
            if carrot['kg'] <= max_capacity:
                values[max_capacity] = max(values[max_capacity], values[max_capacity - carrot['kg']] + carrot['price'])
    return values[capacity]
