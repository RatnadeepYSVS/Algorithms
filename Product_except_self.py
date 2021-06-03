"""
Question:-
Given A List Of Elements Print The Product of Elements except self for each element in List
Input               Output
5                   120 60 40 30 24
1 2 3 4 5
2                   12 0
0 12
"""
"""
Approach 1:
Calculate Total product of list
divide this total product with each and every element in list
This can be done easily with reduce and map 
"""
from functools import reduce
size=int(input())
elems=list(map(int,input().split()))
product=reduce(lambda x,y:x*y,elems)#Calculates Product of Entire List
print(*list(map(lambda x:product//x,elems)))#Divides Calculated Product With Entire List and Prints Result
"""
The Problem With Above Code Is It Won't Work for Case 2 It Throws An Error So we Need To perform This Without Division Operation
Approach 2:-
The Idea Is We Take Left Elements Of Element in the main List and Compute Product and Store It in a List
And Take Right Elements of ELement in main list And Compute Product and Store It List
Multiplying These two Lists we get the o/p required.
So What We Are Gonna Do Is:-
1.Take Two Lists Left And Right.
2.Make All The Left Elements of List in Left list And Calculate The Prefix Product
For Above Case 1 2 3 4 5
Since There Are No Left Elements for 1
Let's Add 1 in Left List
Left=[1]
1 is Left element for 2
lets compute product with 1 in Left List and 1 in main List and add this value in Left
So Left=[1,1]
2 is Left element for 3
Lets Compute Product with 1 in left List and 2 in main List and add this value in Left
So Left=[1,1,2]
3 is Left element for 4
Lets Compute Product with 2 in left List and 3 in main List and add this value in Left
So Left=[1,1,2,6]
4 is Left element for 5
Lets Compute Product with 6 in left List and 4 in main List and add this value in Left
So Left=[1,1,2,6,24]
3.Find All Elements To Right 
So main list is 1 2 3 4 5
Since There Are No Right Elements for 5
Let's Add 1 in Right List
Right=[1]
5 is Right element for 4
lets compute product with 1 in Right List and 5 in main List and add this value in Right
So Right=[1,5]
Right=[1,5]
4 is Right element for 3
lets compute product with 5 in Right List and 4 in main List and add this value in Right
So Right=[1,5,20]
3 is Right element for 2
Lets Compute Product with 20 in Right List and 3 in main List and add this value in Right
So Right=[1,5,20,60]
2 is Right element for 1
Lets Compute Product with 60 in Right List and 2 in main List and add this value in Right
So Right=[1,5,20,60,120]
Right=[1,5,20,60,120]
we need to reverse this list 
so Right=[120,60,20,5,1]
4.Multiply Elements in this Right and Left list and Print the Multiplied Element
Left=[1,1,2,6,24] Right=[120,60,20,5,1]
So O/p List By Multiplying Elements in both Lists is 
[120,60,40,30,24] which is the required O/p List Above...
"""
#Implementation
size=int(input())
elems=[int(i) for i in input().split()]
left=[1]
right=[1]
for i in range(1,size):
    left.append(left[i-1]*elems[i-1])
rev=elems[::-1]
for i in range(1,size):
    right.append(right[i-1]*rev[i-1])
print(*[i*j for i,j in zip(right[::-1],left)])
#Implementation With One Single List
size=int(input())
elems=[int(i) for i in input().split()]
left=[1]
for i in range(1,size):
	left.append(left[i-1]*elems[i-1])
left.insert(0,1)
for i in range(size-1,0,-1):
	left.insert(0,left[0]*elems[i])
for i in range(size):
	print(left[i]*left[size+i],end=" ")
# Code Contributed by RatnadeepYSVS..
