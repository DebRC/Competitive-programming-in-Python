def fibo(n):

    #0th Fibonacci Number
    if n==-2:
        return 0
        
    #1th Fibonacci Number
    if n==-1:
        return 1
    
    #ith Fibonacci Number 
    a=[[1,1],[1,0]]
    res=[[1,0],[0,1]]
    while(n):
        if n%2==1:
            res=matrixmulti(res,a)
            n-=1
        else:
            a=matrixmulti(a,a)
            n=n//2
    return res[0][0]+res[0][1]

#matrix multiplication
def matrixmulti(m1,m2):
    mul=[[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                mul[i][j]+=m1[i][k]*m2[k][j]
    return mul

def main():
    n=int(input("Enter the nth value- "))
    print("The "+str(n)+"th fibonacci number is- ",fibo(n-2))

main()

