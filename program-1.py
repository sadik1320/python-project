print('please chose the operation in the follwing\nadd\nsub\nmul\ndivd and enter the input as 10 20 operation')
x=input('enter the values:')
l=list(x.split())
num1= float(l[0])
num2=float(l[1])
if (l[2])=='add':
     y=num1+num2
     print(y)

elif l[2]=='sub':
    y=num1-num2
    print(y)

elif l[2]=='mul':
    y=num1*num2
    print(y)
elif l[2]=='divd':
    y=num1/num2
    print(y)