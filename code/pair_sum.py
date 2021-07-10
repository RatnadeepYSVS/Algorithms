"""
Question:-
You Are Given A List Containing N Elements and A Value X
Your Task is to Find a pair Such that PairSum equals Value X
Print Yes If A Pair Exists Else Print -1 
I/p:-           O/p:-
6 16            Yes
1 2 3 4 10 6
I/p:-           O/p:-     
6 20            -1
1 2 3 4 5 7 
Constraints:-
1<=N<=10**4
1<=K<=10**9
1<=A[i]<=10**9
"""
"""
Approach 1:-Brute Force
Assign A flag value to 0
The Simple Technique is Two run two loops 
Outer Loop Starts From i to n
Inner Loop Starts From i+1 to n
if a[i]+a[j]==K we put the flag value to 1
now we check the flag value 
if flag ==1 
we print 'Yes'(Without The Quotes)
else
We print -1
Time Complexity:-O(n**2)
"""
flag=0
n,k=map(int,input().split())
z=[int(i) for i in input().split()]
for i in range(n):
    for j in range(i+1,n):
        if z[i]+z[j]==k:
            flag=1
print('Yes' if flag else -1)
"""
Solving the above problem in Linear Time
Approach: In this Approach We Are Going to Use HashMap.
I'm Going To add List Values in the HashMap
And Check K(given pair sum)-i is there in the HashMap or not
If there in the HashMap i'll be printing 'Yes' and Break the loop
Approach: In this Approach We Are Going to Use HashMap
I'm Going To add List Values in the HashMap
And Check K(given pair sum)-i is there in the HashMap or not
If there in the HashMap i'll be printing 'Yes' and Break the loop
else i'll be printing -1
For better Understanding let's Take Above Example
n=6 k=16
1 2 3 4 10 6
j=values in list
Now I will add j value in HashMap
Then i will check whether k-j is there in HashMap or not
so here j=1
s={}
we are adding j to s
so s={1}
checking k-j in s 
16-1=15 is not there in s
next iteration
here j=2
s={1,2}(added 2)
checking 16-2=14 in s
14 is not there in s
next iteration
here j=3
s={1,2,3}
checking 16-3=13 in s
13 is not there in s
next iteration
here j=4
s={1,2,3,4}
checking 16-4=12 in s
12 is not there in s
next iteration
here j=10 
s={1,2,3,4,10}
checking 16-10=6 in s
6 is not there in s
next iteration
here j=6
s={1,2,3,4,10}
checking 16-6=10 in s
10 is there in s
so we break the loop
print 'yes'
Time Complexity:-O(n)
"""
n,k=map(int,input().split())
z=[int(i) for i in input().split()]
s=dict()
for i in z:
    if k-i in s:
        print('Yes')
        break
    s[i]=0
else:
    print(-1)
#Code Contributed By  RatnadeepYSVS
