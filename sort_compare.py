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

    print("After increments of size", sublist_count, "The list is", a_list)

def python_sort():
    pass

def main():
    pass

if __name__ == '__main__':
    main()
