from quick_sort_hoare_partition import swap


def quick_sort(elements, start, end):
    if len(elements)== 1:
        return

    if  start < end:
        pi = partition(elements, start, end)

        quick_sort(elements, start, pi-1) # left partition
        quick_sort(elements, pi+1, end) #right partition

def partition(elements, start, end):
    pivot = elements[end]
    i = start

    for j in range(start, end):
        if elements[j] <= pivot:
            swap(j, i, elements)
            i = i+1

    swap(i, end, elements)

    return i



if __name__ == "__main__":
    elements = [11,9, 29, 7,2,15,28]
    quick_sort(elements, 0, len(elements)-1)
    print(elements)