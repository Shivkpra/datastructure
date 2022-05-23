#Stack operations
# empty list
stack=[]
# this function use to add element in stack
def push(stack):
    i=int(input("Enter the value you want to append"))
    stack.append(i)
    print(stack)
#this function use to delete the element from stack
def pop_item(stack):
    #list is empty
    if not stack:
        print("It is empty string")
    #delete the element if it is not empty
    else:
        p=stack.pop()
        print("removed item",p)
        print(stack)
#this function use to check underflow condition
def under_flow(stack):

    #if length of list is zero than it is underflow condition
    if len(stack)==0:
        print("under flow condition")
    # list is not empty
    else:
        print("Stack is not empty")
#this function use to check the peek

def peek(stack):
    if (len(stack)==0):
        print ("Underflow")
    #this will  give the peek value
    else:
        top=len(stack)-1
        print( stack[top])
# this function use to display the stack value
def display(stack):
    if (len(stack)==0):
        print ("Underflow")
    else:
        top=len(stack)-1
        print( stack[top],'<----top')
        for i in range(top-1,-1,-1):
            print(stack[i])


#this loop is use to choice the which operation you have to perform
while True:
    print("Select the operation :")
    print("1.Push")
    print("2.Pop")
    print("3. Under flow")
    print("4 Peek")
    print("5 Display")
    choice=int(input("Enter the number(1-5)"))
    if choice==1:
        push(stack)
    elif choice==2:
        pop_item(stack)
    elif choice==3:
        under_flow(stack)
    elif choice==4:
        peek(stack)
    elif choice ==5 :
        display(stack)

    else:
        break