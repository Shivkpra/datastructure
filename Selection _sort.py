def selection_sort(arr):                            #function declaration
    #assigning  size with -1 to get size according to index
    size=-1
    for i in arr:
        #cout the size of arr
        size+=1
    for i in range (size):
        swap=False

        min=i
        for j in range(i+1,size+1):
            #Swap the arr element according to the condition
            if arr[j]< arr[min]:
                arr[j],arr[min]=arr[min],arr[j]
                swap=True
        if swap==False:
            break
        print(arr)

arr = [1,0,3,5,4]
selection_sort(arr)                                           #function call



















