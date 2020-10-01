def insertion_sort(a,n):
    for i in range(1,n):
        key=a[i]
        j=i-1
        while(j>=0 and a[j]>key):
            a[j+1]=a[j]
            j-=1
        a[j+1]=key
n=int(input("Enter the size of the unsorted array:- "))
print("Enter The Array")
a=list(map(int, input().split()))
insertion_sort(a,n)
print("Sorted Array:-", a)
