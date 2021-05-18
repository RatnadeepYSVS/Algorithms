"""
Problem:-
Given A List Of Elements.You are also given quries consisting of two numbers.
Now You Need To Calculate Mean Of Elements With in These two Numbers.
Look At The Example Below For Clear Understanding of the problem.
Note:- Here the List is Following 0 Based Indexing 
I/p:-       O/p:-
5 3         2
1 2 3 4 5   3
0 2         3
1 3
1 4
Explanation:-
Our List 1 2 3 4 5
Here 5 is List Size 3 is Number Of Quries Given
0 2,1 3,1 4 are quries need to be performed to given List
Now From index 0 to 2 The Sum Of Elements is 6
No of Elements From index 0 to 2 are 3
So 6//3 is 2
Similarly for other cases
"""
"""
Approach 1:-
Brute Force:
Iterate A loop for The quries 
inside this loop start from index start query to end query and Calculate The Sum
To Know The Number Of Elements:-right query - left query +1
Time Complexity:-O(N^2)
"""
#Implementation
x,y=map(int,input().split())
z=[int(i) for i in input().split()]
for i in range(y):
    l,r=map(int,input().split())
    s=0
    for k in range(l-1,r):
        s+=z[k]
    print(s//(r-l+1))
"""
Approach 2:-
Linear Time 
To Do This We Will Calculate The Prefix Sum of The List
Prefix Sum Of the List 1 2 3 4 5 is 1 3 6 10 15
l=left query
r=right query
We will access the l and r indexes to the prefix sum List
and calculate the mean
The Problem With this solution is if l==0 then we just need
to divide l[r] with l-r+1(Mentioned Above)
if l is a number other than 0 then we need to adjust l value to l-1
and calculate the difference b/w List[r] and List[l-1]
Let's Take An example 
for the list let's take query number 2 which is 1,3 l=1,r=3
value at index 1 is 3
value at index 3 is 10
so l-r+1==3 so
so prefix[r]-prefix[l]=2 
so the answer is 2(7//3) which is incorrect
So the left query value must be adjusted to l-1
l=1,r=3 
so l-1=0 and List[l-1]=1
so r=3   and List[r]=10
so l-r+1=3
so List[r]-List[l-1]=10-1=9
so mean is 9//3 which is 3
Time Complexity:-O(N)
"""
#Implementation
x,y=map(int,input().split())
z=[int(i) for i in input().split()]
prefixsum=[z[0]]
for i in range(1,x):
    prefixsum.append(prefixsum[i-1]+z[i])
for i in range(y):
    l,r=map(int,input().split())
    if l==1:
        print((prefixsum[r-1])//(r-l+1))
    else:
        print((prefixsum[r-1]-prefixsum[l-2])//(r-l+1))
#Code Contributed By RatnadeepYSVS