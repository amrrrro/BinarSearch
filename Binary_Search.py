##################################################################
#             Name    : Amr Adel                               #
#             Date    : 25 Nov 2020                            #
#             Version : V0                                     #
##################################################################

List = []

Length_List = int(input("Enter the Length Of The List : "))
#Enter The List
for i in range(Length_List):
    New_List = int(input("Enter The List : "))
    List.append(New_List)
    
print(List)

#Sorting the list
List.sort()
print(List)
#The input Search
Input = int(input("Enter the number You Want : "))
#binary Search
start = 0
end = Length_List -1

while(start <= end):
    Center = (start + end)//2
    print(Center)
    if(Input == List[Center]):
        print(Input , "found")
        break
    elif(Input > List[Center]):
        start = Center + 1
    elif(Input < List[Center]):
        end = Center - 1

