#HOW TO: In terminal type 'python sort_compare.py' to run program

import timeit
import random
from random import shuffle
from timeit import Timer

def insertion_sort(a_list):
  for index in range(1, len(a_list)):
    current_value = a_list[index]
    position = index
    while position > 0 and a_list[position - 1] > current_value:
       a_list[position] = a_list[position - 1]
       position = position - 1

    a_list[position] = current_value

def shell_sort(a_list):
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)

        sublist_count = sublist_count // 2

def gap_insertion_sort(a_list, start, gap):
  for i in range(start + gap, len(a_list), gap):
    current_value = a_list[i]
    position = i
    while position >= gap and a_list[position - gap] > current_value:
        a_list[position] = a_list[position - gap]
        position = position - gap
        a_list[position] = current_value

def python_sort(a_list):
    a_list.sort()


def main():

    insertion_sort_list = []
    shell_sort_list = []
    python_sort_list = []

    def generate_lists(total_lists,  list_length):
        input_lists = [random.sample(range(list_length), list_length) for x in range(total_lists)]

        for input_list in input_lists:
            insertion_sort_timer = Timer(lambda: insertion_sort(input_list))
            insertion_sort_results = insertion_sort_timer.timeit(number=1)
            insertion_sort_list.append(insertion_sort_results)

            shuffle(input_list)

            shell_sort_timer = Timer(lambda: shell_sort(input_list))
            shell_sort_results = shell_sort_timer.timeit(number=1)
            shell_sort_list.append(shell_sort_results)

            shuffle(input_list)

            python_sort_timer = Timer(lambda: python_sort(input_list))
            python_sort_results = python_sort_timer.timeit(number=1)
            python_sort_list.append(python_sort_results)

        insertion_sort_average = sum(insertion_sort_list)/len(input_list)
        shell_sort_average = sum(shell_sort_list)/len(input_list)
        python_sort_average = sum(python_sort_list)/len(input_list)

        print("Insertion sort, for a list size of %s took %10.7f seconds to run, on average"% (list_length, insertion_sort_average))
        print("Shell sort, for a list size of %s took %10.7f seconds to run, on average"% (list_length, shell_sort_average))
        print("Python sort, for a list size of %s took %10.7f seconds to run, on average"% (list_length, python_sort_average))


    generate_lists(10, 500)
    generate_lists(100, 1000)
    generate_lists(100, 10000)


if __name__ == '__main__':
    main()
