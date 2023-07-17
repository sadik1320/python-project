x=input('enter the values:')
l=list(x.split())
y=map(int,l)
a=[num for num in range(1,10)]
dic={}
for i in y:
    count=0
    for j in a:
        if j%i==0 :
            count+=1
    dic[i]=count
print(dic)