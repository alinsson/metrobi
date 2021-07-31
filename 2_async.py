import asyncio
from timeit import default_timer as timer

async def print_async(array):
    for x in range(0, len(array)):
        start = timer()
        await printed_delayad(2**x, array[x])
        end = timer()
        print("time elapsed: {}".format(end - start))

async def printed_delayad(delay, element):
    # test if delay is correct, comment next line
    await asyncio.sleep(delay)
    #print(delay)
    print("{} - {}s".format(element, delay))

array = ['a', 'b', 'c', 'd']
#array = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
asyncio.run(print_async(array))