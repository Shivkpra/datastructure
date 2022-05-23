# without any in built function
def Bubble_sort(arr):                       #function declaration
    #assigning  size with -1 to get size according to index
    size=-1
    #iterate the arr varible
    for i in arr:
        #cout the size of arr
        size+=1

    for i in range (size):
        swap=False
        for i in range(size-i):
            #Swap the arr element according to the condition
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]

                swap=True

        # if swap variable is false then the loop will be break
    if swap==False:
        break;

    print (arr)
arr=[23,45,67,89,34,12,56,31,45,82,78,34]
Bubble_sort(arr)                                        #function call





































