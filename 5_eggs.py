# i can drop the egg from floor 1 and go until the first one broken, but request many trials
# with a binary search we have only 2 eggs, its not a good idea

# if start in 20 floor, and broken, we have more 19 trials in the worst case (1 - 19)
# in worst case broken in 100 (5 trials from 20 - 100) more 19 trials in the last 20, more (1 - 19)
# so we have x + (x - 1) drops, making this linear to less drops we have a sum of an arithmetic progression:
# x + (x-1) + (x-2) + (x-3) + ... + 1 = x*(x+1)/2
# For this problem he have in the worst case for the last floor to be tried is 100'th, so to optimal value of x, for we don't go beyond x attempts:
# x*(x+1)/2 = 100 -> x2 + x - 200 = 0, x = 13.651 or -14.651
# So we need to init in 14, next drop jump more 13 floors, the next jump 12 floors and so on, the worst case will be 14 drops
 
# time complexity O(eggs*floors^2)
# time complexity O(eggs * floors**2). spce complexity for 2D array O(eggs * floors)


# drops needed in worst case with number egg and number floors
def eggs(number_egg, number_floors):
    if (number_egg == 1 or number_egg == 0):
        return number_floors if number_egg == 1 else 0
    
    # number of trials needed for i eggs and j floors.
    optimal = [[0 for x in range(number_floors + 1)] for x in range(number_egg + 1)]
    
    # need 1 trial for one floor and 0 trials for 0 floors
    for i in range(1, number_egg + 1):
        optimal[i][1] = 1
        optimal[i][0] = 0
 
    # only one egg we have number floors of tries
    for j in range(1, number_floors + 1):
        optimal[1][j] = j
 
    # fill rest of the entries in table using optimal substructure property
    for i in range(2, number_egg + 1):
        for j in range(2, number_floors + 1):
            optimal[i][j] = 10000
            for x in range(1, j + 1):
                res = 1 + max(optimal[i-1][x-1], optimal[i][j-x])
                if res < optimal[i][j]:
                    optimal[i][j] = res
 
    return optimal[number_egg][number_floors]

# optimal number of trials in worst case with number eggs and number floors
print(eggs(2, 100)) # optimal value for question
print(eggs(0, 100))
print(eggs(1, 100))
print(eggs(2, 500))
print(eggs(3, 1000))
