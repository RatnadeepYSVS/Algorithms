"""
Problem:-
Given an array of integers, sort the array into a wave like array and return it,
In other words, arrange the elements into a sequence such that a1 >= a2 <= a3 >= a4 <= a5.....
I/p:-      O/p:-
4           2 1 4 3 (or) 4 1 3 2
1 4 2 3
Note : There Can Be Other Orders Return One Of The Order
"""
"""
Approach:-
Sort the Array And Swap The Elements By Increasing Step Count of 2
Let's Take An Example:-
l=1 4 3 2
after sorting this would be
1 2 3 4
Loop i from 0 to n-1(if u loop to n the program raises index out of range error)
Swap Elements By Increasing Step Size of 2
i(step)=0
swap(a[i],a[i+1])
a[i]=1
a[i+1]=2
now after swap a[i]=2 a[i+1]=1
now increment step size by units i=i+2
i=2
a[i]=3 a[i+1]=4
after swaping a[i+1]=4 a[i]=3
so the list is 2 1 4 3
"""
#Implementation
n=int(input())
k=sorted(list(map(int,input().split())))#Directly Sorting The Input List
for i in range(0,n-1,2):#range(start value,end value,step value)format of range function in Python
    k[i],k[i+1]=k[i+1],k[i]#Swaping Elements
print(k)
#Code Contributed By RatnadeepYSVS