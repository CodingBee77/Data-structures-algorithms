from insertion_sort import insertion_sort


def calculate_median(elements):
    insertion_sort(elements)
    middle_index = int(len(elements)/2)

    if len(elements) == 0 :
        return "This list is empty"

    if len(elements)%2==0:
        print("List has even number of elements! ")
        return (elements[middle_index-1] + elements[middle_index])/2


    print("List has uneven number of elements! ")
    return elements[middle_index]


def running_median(elements):
    active_list = []
    for elem in elements:
        active_list.append(elem)
        print(calculate_median(active_list))



if __name__ == "__main__":
    elements = [2,1,5,7,2,0,5]
    running_median(elements)
    # median = calculate_median(elements)
    # print(median)