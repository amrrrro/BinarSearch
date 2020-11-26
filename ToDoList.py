ToDo = []
Done = []
flag = 1
while (flag) :
    print("*****************************")
    print("To add new item press 1 ")
    print("To print TODo list press 2 ")
    print("To mark an iteam press 3 ")
    print("To print the done list press 4 ")
    print("To Exit press 0 ")
    print("*****************************")
    x = int(input( "Please enter your choice : "))
     
    if x == 1:
        
        NewTodo = int(input("Enter your number "))
        ToDo.append(NewTodo)
        
        
    elif x == 2:
        for i in range(len(ToDo)) :
            print (ToDo[i])
        
        
    elif x == 3:
        NewDone = int(input("enter the number to move "))
        Do= ToDo[NewDone]
        Done.append(Do)
        
    elif x==4 :
        print(Done)
        
    elif x==0 :
        flag = 0

    else :
        print("Error Not Found")