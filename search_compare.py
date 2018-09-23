import timeit
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
    for x in xrange(100):
        five_hundered_input = [range(1,500) for i in list(range(500))]

        sequential_search_timer = Timer(lambda: sequential_search(five_hundered_input, -1))
        sequential_search_results = sequential_search_timer.timeit(number=1)
        sequential_search_list.append(sequential_search_results)

        ordered_sequential_search_timer = Timer(lambda: ordered_sequential_search(five_hundered_input, -1))
        ordered_sequential_search_results = ordered_sequential_search_timer.timeit(number=1)
        ordered_sequential_search_list.append(ordered_sequential_search_results)

        binary_search_iterative_timer = Timer(lambda: binary_search_iterative(five_hundered_input, -1))
        binary_search_iterative_results = binary_search_iterative_timer.timeit(number=1)
        binary_search_iterative_list.append(binary_search_iterative_results)

        binary_search_recursive_timer = Timer(lambda: binary_search_recursive(five_hundered_input, -1))
        binary_search_recursive_results = binary_search_recursive_timer.timeit(number=1)
        binary_search_recursive_list.append(binary_search_recursive_results)

    sequential_search_five_hundred_average = sum(sequential_search_list)/len(five_hundered_input)
    ordered_sequential_search_five_hundered_average = sum(ordered_sequential_search_list)/len(five_hundered_input)
    binary_search_iterative_five_hundred_average = sum(binary_search_iterative_list)/len(five_hundered_input)
    binary_search_recursive_five_hundred_average = sum(binary_search_recursive_list)/len(five_hundered_input)

    print("Sequential Search for a list size of 500 took %10.7f seconds to run, on average"% sequential_search_five_hundred_average)
    print("Ordered Sequential Search for a list size of 500 took %10.7f seconds to run, on average"% ordered_sequential_search_five_hundered_average)
    print("Binary Search Iterative for a list size of 500 took %10.7f seconds to run, on average"% binary_search_iterative_five_hundred_average)
    print("Binary Search Recursive for a list size of 500 took %10.7f seconds to run, on average"% binary_search_recursive_five_hundred_average)
    print('Loading 1000 results......')

    del sequential_search_list[:]
    del ordered_sequential_search_list[:]
    del binary_search_iterative_list[:]
    del binary_search_recursive_list[:]

    for x in xrange(100):
        thousand_input = [range(1,1000) for i in list(range(1000))]

        sequential_search_timer = Timer(lambda: sequential_search(thousand_input, -1))
        sequential_search_results = sequential_search_timer.timeit(number=1)
        sequential_search_list.append(sequential_search_results)

        ordered_sequential_search_timer = Timer(lambda: ordered_sequential_search(thousand_input, -1))
        ordered_sequential_search_results = ordered_sequential_search_timer.timeit(number=1)
        ordered_sequential_search_list.append(ordered_sequential_search_results)

        binary_search_iterative_timer = Timer(lambda: binary_search_iterative(thousand_input, -1))
        binary_search_iterative_results = binary_search_iterative_timer.timeit(number=1)
        binary_search_iterative_list.append(binary_search_iterative_results)

        binary_search_recursive_timer = Timer(lambda: binary_search_recursive(thousand_input, -1))
        binary_search_recursive_results = binary_search_recursive_timer.timeit(number=1)
        binary_search_recursive_list.append(binary_search_recursive_results)

    sequential_search_results_thousand_average = sum(sequential_search_list)/len(thousand_input)
    ordered_sequential_search_thousand_average = sum(ordered_sequential_search_list)/len(thousand_input)
    binary_search_iterative_thousand_average = sum(binary_search_iterative_list)/len(thousand_input)
    binary_search_recursive_thousand_average = sum(binary_search_recursive_list)/len(thousand_input)
    
    print("Sequential Search for a list size of 1000 took %10.7f seconds to run, on average"% sequential_search_results_thousand_average)
    print("Ordered Sequential Search for a list size of 1000 took %10.7f seconds to run, on average"% ordered_sequential_search_thousand_average)
    print("Binary Search Iterative for a list size of 1000 took %10.7f seconds to run, on average"% binary_search_iterative_thousand_average)
    print("Binary Search Recursive for a list size of 1000 took %10.7f seconds to run, on average"% binary_search_recursive_thousand_average)
    print('Loading 10000 results......')

    del sequential_search_list[:]
    del ordered_sequential_search_list[:]
    del binary_search_iterative_list[:]
    del binary_search_recursive_list[:]

    for x in xrange(100):
        ten_thousand_input = [range(1,10000) for i in list(range(10000))]

        sequential_search_timer = Timer(lambda: sequential_search(ten_thousand_input, -1))
        sequential_search_results = sequential_search_timer.timeit(number=1)
        sequential_search_list.append(sequential_search_results)

        ordered_sequential_search_timer = Timer(lambda: ordered_sequential_search(ten_thousand_input, -1))
        ordered_sequential_search_results = ordered_sequential_search_timer.timeit(number=1)
        ordered_sequential_search_list.append(ordered_sequential_search_results)

        binary_search_iterative_timer = Timer(lambda: binary_search_iterative(ten_thousand_input, -1))
        binary_search_iterative_results = binary_search_iterative_timer.timeit(number=1)
        binary_search_iterative_list.append(binary_search_iterative_results)

        binary_search_recursive_timer = Timer(lambda: binary_search_recursive(ten_thousand_input, -1))
        binary_search_recursive_results = binary_search_recursive_timer.timeit(number=1)
        binary_search_recursive_list.append(binary_search_recursive_results)

    sequential_search_results_ten_thousand_average = sum(sequential_search_list)/len(ten_thousand_input)
    ordered_sequential_search_ten_thousand_average = sum(ordered_sequential_search_list)/len(ten_thousand_input)
    binary_search_iterative_ten_thousand_average = sum(binary_search_iterative_list)/len(ten_thousand_input)
    binary_search_recursive_ten_thousand_average = sum(binary_search_recursive_list)/len(ten_thousand_input)

    print("Sequential Search for a list size of 10000 took %10.7f seconds to run, on average"% sequential_search_results_ten_thousand_average)
    print("Ordered Sequential Search for a list size of 10000 took %10.7f seconds to run, on average"% ordered_sequential_search_ten_thousand_average)
    print("Binary Search Iterative for a list size of 10000 took %10.7f seconds to run, on average"% binary_search_iterative_ten_thousand_average)
    print("Binary Search Recursive for a list size of 10000 took %10.7f seconds to run, on average"% binary_search_recursive_ten_thousand_average)


if __name__ == '__main__':
    main()
