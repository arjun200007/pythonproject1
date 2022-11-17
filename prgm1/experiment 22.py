n= (input("enter the limit of string"))
print("enter the number of elements")
count=0
list=[]
for i in (0,n):
    ele=input()
    list.append(ele)
print(list)
for i in list:
     for j in i:
         if j=='a':
             count=count+1
print(count)