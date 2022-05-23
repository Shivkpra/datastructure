def insertion_sort( arr ):                                  #function declaration
    #assigning  size with -1 to get size according to index

    size=-1
    #iterate the arr varible

    for i in arr:
        size+=1

    for i in range(1,size):
        #assigning arr first value as a min value
        temp = arr[i]
        # count of j is decrease by  1
        j = i -1
        #if the while condition become ture assign j valie to j+1
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            #count of j is decrease by  1
            j = j - 1


        arr[j + 1] = temp


arr=[12,11,67,89,15,56]
insertion_sort(arr)                 #fucntion call
print(arr)

