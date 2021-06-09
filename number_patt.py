"""
Problem:-Your Given A Number N.Based On This Number You Should Create A Matrix Shown Below Of Order 2*N-1.
I/p:-
2
O/p:-
2 2 2
2 1 2
2 2 2
I/p:-
5
5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 5
5 4 3 3 3 3 3 4 5
5 4 3 2 2 2 3 4 5
5 4 3 2 1 2 3 4 5
5 4 3 2 2 2 3 4 5
5 4 3 3 3 3 3 4 5
5 4 4 4 4 4 4 4 5
5 5 5 5 5 5 5 5 5
Constraints:-
1<=N<=100
"""
"""
Approach:
This Approach Is Explained in two parts
Part-1
If We Observe All The Numbers From 1 to N are Repeated 2*i+1 times.
For Example Let us Take N as 5
So From 1-5
1 is repeated 1 time
2 is repeated 3 times
3 is repeated 5 times
4 is repeated 7 times
5 is repeated 9 times
So We Will Obtain this and store in a list called rowlist
Part-2
As We Got The Above List What Remains Is We Need To Add The Remaining Numbers To Form The Matrix.
So To Obtain Those Values Take A List Called Numlist  Containing Numbers 1-N in reverse and use Slice these values in a for loop.
So for Row 1 There is no need to numbers since 5 is repeated 9 times.i=0 
can be obtained by numlist[:i]+rowlist[i]+numlist[:i][::-1]
For Row 2 We Need to Add 5 two times at front and back of 4 which is repeated 7 times.i=1
can be obtained by numlist[:i]+rowlist[i]+numlist[:i][::-1]
For Row 2 We Need to Add 5,4 two times at front and back of 3 which is repeated 5 times.i=2
can be obtained by numlist[:i]+rowlist[i]+numlist[:i][::-1]
For Row 2 We Need to Add 5,4,3 two times at front and back of 2 which is repeated 3 times.i=3
can be obtained by numlist[:i]+rowlist[i]+numlist[:i][::-1]
For Row 2 We Need to Add 5,4,3,2 two times at front and back of 1 which is repeated 1 times.i=4
can be obtained by numlist[:i]+rowlist[i]+numlist[:i][::-1]
This Will Print Rows Upto N.
Similarly We Repeat Part2 in reverse To print remaining pattern.
"""
nums=list(range(1,101))#Storing Values from 1-100
n=int(input())#Taking N input
k,z=nums[:n][::-1],[]#k is used to gen values upto n and z to store rows of partone
for i in range(n):
	l=[]
	for _ in range(2*i+1):
		l.append(nums[i])
	z=[l]+z#Stores Part one values
for i in range(n):
	print(*(k[:i]+list(z[i])+k[:i][::-1]))#Printing Pattern Upto N rows
for i in range(n-1,0,-1):
	print(*(k[:i-1]+list(z[i-1])+k[:i-1][::-1]))#Printing Remaining Pattern