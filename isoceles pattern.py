#using for loop and range function
def range_func(n):
    for i in range(1,n+1,1):
        for k in range(1,n-i+1):
            print(" ",end="")
        for j in range(1,i+1):
            print(j,end="")
        for s in range(i-1,0,-1):
            print(s,end="")
        print()

#using while function
def while_func(n):
    i=1
    while i<=n:
        #spaces
        j=1
        while j<=n-i:
            print(" ",end="")
            j=j+1
        #stars
        star=1
        while star<=i:
            print(star,end="")
            star=star+1
        s=i-1
        while s>=1:
            print(s,end="")
            s=s-1
        i=i+1
        print()
n=int(input())
while_func(n)
range_func(n)