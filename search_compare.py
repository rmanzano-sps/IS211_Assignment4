import time
import random

def sequential_search(a_list, item):
    pos = 0
    found = False
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos+1
    return found

def ordered_sequential_search(test_list, num):
    start = time.time()
    test_list.sort()

    results = sequential_search(test_list, num)
    end_time = time.time()

    return results, end_time


def binary_search_iterative():
    pass

def binary_search_recursive():
    pass

def main():
    for x in xrange(1):
        five_hundered_input = [random.randrange(1,500) for i in list(range(500))]
        five_hundred_results = ordered_sequential_search(five_hundered_input, -1)
        print(five_hundered_input, x)
        # print(five_hundred_results[1], x)
    # for x in range (1000):
    #     thousand_input = [random.randrange(1, 101) for i in list(range(100))]
    #     ordered_sequential_search(thousand_input)
    #
    # for x in range (10000):
    #     ten_thousand_input = [random.randrange(1, 101) for i in list(range(100))]
    #     ordered_sequential_search(ten_thousand_input)

if __name__ == '__main__':
    main()


#
# test_list = [1, 2, 32, 8, 17, 19, 42, 13, 0]
# print(ordered_sequential_search(test_list, 3))
# print(ordered_sequential_search(test_list, 13))
#
