from timeit import default_timer as timer
import numpy as np

# time complexity O(n**2)
# use of 'set', are a partially immutable collection of items that cannot contain duplicate elements
# from https://wiki.python.org/moin/TimeComplexity set is O(n)
# count in the worst case is O(n)
def find_duplicate_w_set(array):
    return set([x for x in array if array.count(x) > 1])
    #return [x for n, x in enumerate(array) if x in array[:n]]

# time complexity worst case O(2*n) and best case O(n)
def find_duplicate(array):
    d = {}

    for item in array:
        if item not in d:
            d[item] = 0

        d[item] += 1

    result_d = {key: val for key, val in d.items() if val > 1}
    return result_d.keys()

def generate_array(n):
    np.random.seed(22)
    return list(np.random.randint(0, n, n))

#array = [24, '24', 24, 24, 24, 33, 41, 42]
#array = [1, 1, 3, 2, 1, 4, 6, 5, 1, 3] * 100
array = generate_array(10000)

print(len(array))
print(array)

start = timer()
response = find_duplicate_w_set(array)
end = timer()

#print(response)
print("time elapsed for {} duplicates: {}".format(len(response), end - start))

start = timer()
response = find_duplicate(array)
end = timer()
#print(response)
print("time elapsed for {} duplicates: {}".format(len(response), end - start))
