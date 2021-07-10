"""
Problem:-
Given an List of elements sort the elements based on their frequency count...
Input:-
1
13
10 20 40 40 40 40 20 30 30 10 10 10 10
constraints:-
1<=T<=70
30<=N<=130
0<=A[i]<=100
O/p:-
10 10 10 10 10 40 40 40 40 20 20 30 30
Note:- If two or more than two numbers are having same freq count then they should follow non decreasing order
See the example above for better Understanding
"""
"""
 This is a Straight Forward Question
Approach:-
Create an List(Frequency List) of Zeros of Size 100.(Since he is not giving the list elements greater than that value)
Calculate The Frequencies of values given by the user and update in those values in the Frequency list.
Sort based on the Freq count and elements and print it
For Sorting We Are gonna use Custom Sort
"""
# Implementation:-
t=int(input())#Test Case Input
for _ in range(t):
    n=int(input())# List Size Input
    k=list(map(int,input().split()))#List Input
    z=[0]*100#mentioned above
    kk=[]
    for i in k:
        z[i-0]+=1
    for i in k:
        kk.append([z[i],i])
    kk.sort(key=lambda x:[-x[0],x[1]]) #Custom Sort Function This Directly compares freq count of that element and also that corresponding element
    print(*[j for i,j in kk])
"""
Time Complexity:-O(nlogn)
As Builtin Sort Complexity is O(nlogn) And For Three Other loops is 3*n neglecting constant it's n
So Totally Time Complexity is O(nlogn+n) which is O(nlogn)
"""
#Code Contributed By RatnadeepYSVS
