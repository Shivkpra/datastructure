Queue=[]

f=None
r=None
#function  use to check Queue is empty or not
def isEmpty(Queue):
    if (Queue==[]):
        print("Queue is Empty")
    else:
        print("Queue is not Empty")

#fucntion use to add element in Queue
def enqueue(Queue):
    i = int(input("Enter the value you want to append"))
    Queue.append(i)

    print(Queue)
    #length of queue is one than f and r value will zero
    if (len(Queue)==1):
        f=r=0
    #length of queue is not one than r is length -1
    else:
        r=len(Queue)-1

#fucntion use to delete element from Queue

def dequeue(Queue):
    #checking queue is empty or not
    if(isEmpty(Queue)):
        return("Underflow")
    #not empty queue is  elemnet is delete
    else:
        i=Queue.pop(0)
        print("Removed value",i)
    if (len(Queue)==0):
        f=r=None
#function use to display peek poingt
def peek(Queue):
    #checking queue is empty or not

    if (isEmpty(Queue)):
        return ("Underflow")
    #f is present at first place that is peek value
    else:
        f=0
        print(Queue[f])
#function use to display Queue

def display(Queue):
    #checking queue is empty or not

    if (len(Queue)==0):
        print("Queue is Empty")
    #length of queue is one that front and rear is same
    if(len(Queue)==1):
        print(Queue[0],'<----front<----rear')
    #length of queue is greater than one front is at first place and last value is rear
    else:
        f=0
        r=len(Queue)-1
        print(Queue[f],'<----front')
        for i in range(1,r):
            print(Queue[i])
        print(Queue[r],'<---- rear')
#this loop is use to choice the which operation you have to perform

while True:
    print("Select the operation :")
    print("1.underflow")
    print("2.push")
    print("3.Pop")
    print("4 Peek")
    print("5 Display")
    choice=int(input("Enter the number(1-5)"))
    if choice==1:
        isEmpty(Queue)
    elif choice==2:
        enqueue(Queue)
    elif choice==3:
        dequeue(Queue)
    elif choice==4:
        peek(Queue)
    elif choice ==5 :
        display(Queue)

    else:
        break