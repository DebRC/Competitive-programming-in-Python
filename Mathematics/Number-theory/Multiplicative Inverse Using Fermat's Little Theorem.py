def power(a,n,m):
    res=1
    while(n):
        if n%2==1:
            res=((res%m)*(a%m))%m
            n-=1
        else:
            a=((a%m)*(a%m))%m
            n//=2
    return res
    

a=int(input("Enter the number:- "))
m=int(input("Enter mod value:- "))
print("a^-1 = ",power(a,m-2,m))