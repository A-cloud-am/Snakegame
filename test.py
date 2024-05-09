'''with open("highscore.txt","r") as f:
        data=f.read()
        print((data.split('""')))'''


a=int(input("Enter the terms"))
num1=0                                       
num2=1                                        
if a<=0:
    print("The requested series is",num1)
else:
    print(num1,num2,end=" ")
    for x in range(2,a):
        next=num1+num2                          
        print(next,end=" ")
        num1=num2
        num2=next




def duplicator(val, max_repeats):
    count = 0
    while True:
        if count < max_repeats:
            count +=1
            yield val
        else:
            return

duplicates_2 = duplicator(5,3)
for duplicate in duplicates_2:
    print(duplicate)




def custom_gen():
    a,b = 0, 1
    while True:
        yield a
        a, b = b, a+b

a = custom_gen()
n=1
while n<10:
    n+=1
    print(next(a))

