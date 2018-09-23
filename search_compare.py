#HOW TO: In terminal type 'python search_compare.py' to run program
import timeit
import random
from timeit import Timer

def sequential_search(a_list, item):
    pos = 0
    found = False
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos+1
    return found

def ordered_sequential_search(a_list, item):
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
             if a_list[pos] > item:
                 stop = True
             else:
                 pos = pos+1
    return found

def binary_search_iterative(a_list, item):
    first = 0
    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found


def binary_search_recursive(a_list, item):
    if len(a_list) == 0:
       return False
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            return True
        else:
            if item < a_list[midpoint]:
                return binary_search_recursive(a_list[:midpoint], item)
            else:
                return binary_search_recursive(a_list[midpoint + 1:], item)


def main():
    sequential_search_list = []
    ordered_sequential_search_list = []
    binary_search_iterative_list = []
    binary_search_recursive_list = []

    def generate_lists(total_lists,  list_length):
        input_lists = [random.sample(range(list_length), list_length) for x in range(total_lists)]

        for input_list in input_lists:
            sequential_search_timer = Timer(lambda: sequential_search(input_list, -1))
            sequential_search_results = sequential_search_timer.timeit(number=1)
            sequential_search_list.append(sequential_search_results)

            input_list.sort()
            ordered_sequential_search_timer = Timer(lambda: ordered_sequential_search(input_list, -1))
            ordered_sequential_search_results = ordered_sequential_search_timer.timeit(number=1)
            ordered_sequential_search_list.append(ordered_sequential_search_results)

            binary_search_iterative_timer = Timer(lambda: binary_search_iterative(input_list, -1))
            binary_search_iterative_results = binary_search_iterative_timer.timeit(number=1)
            binary_search_iterative_list.append(binary_search_iterative_results)

            binary_search_recursive_timer = Timer(lambda: binary_search_recursive(input_list, -1))
            binary_search_recursive_results = binary_search_recursive_timer.timeit(number=1)
            binary_search_recursive_list.append(binary_search_recursive_results)


        sequential_search_average = sum(sequential_search_list)/len(input_list)
        ordered_sequential_search_average = sum(ordered_sequential_search_list)/len(input_list)
        binary_search_iterative_average = sum(binary_search_iterative_list)/len(input_list)
        binary_search_recursive_average = sum(binary_search_recursive_list)/len(input_list)


        print("Sequential Search, for a list size of %s took %10.7f seconds to run, on average"% (list_length, sequential_search_average))
        print("Ordered Sequential Search, for a list size of %s took %10.7f seconds to run, on average"% (list_length, ordered_sequential_search_average))
        print("Binary Search Iterative, for a list size of %s took %10.7f seconds to run, on average"% (list_length, binary_search_iterative_average))
        print("Binary Search Recursive, for a list size of %s took %10.7f seconds to run, on average"% (list_length, binary_search_recursive_average))

    generate_lists(100, 500)
    generate_lists(100, 1000)
    generate_lists(100, 10000)



if __name__ == '__main__':
    main()
