str1=str(input("enter the text"))
dict1={}
word=str1.split()
for i in word:
    if i in dict1:
        dict1[i]=dict1[i]+1
    else:
        dict1[i]=1
for m,n in dict1.items():
    print(m,n)
