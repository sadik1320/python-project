x=int(input('enter tthe value:'))
l=[]
if x==1:
    l.append(x)
else :
    if x%2!=0:
        for x in range (1,x*2):
            if x%2!=0:
                l.append(x)
    else:
        for x in range (1,(x-1)*2):
            if x%2!=0:
                l.append(x)
print(l)