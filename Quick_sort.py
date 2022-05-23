def quick_sort(list):                       #function declaration
    #this in-built function count the length of list
    length = len(list)
    #if length of list is 1 or less than one list will return
    if length <= 1:
        return list
    #the last value is pop and become pivot
    else:
        pivot = list.pop()
    print(pivot)
    # the greater value than pivot stored
    items_greater = []
    # the samller value than pivot stored
    items_lower = []

    for item in list:
        #append the greater value in item_greater
        if item > pivot:
            items_greater.append(item)
            print("Greater:",items_greater)
        #append the samller value in item_greater
        else:
            items_lower.append(item)
            print("Lower:",items_lower)

    # arrangement of list in sorted form
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

print('Sorted :',quick_sort([78,34,92,12,56,89,67,10,23,]))    #function call