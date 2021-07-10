"""
Question:-
You are given a number of cases
For each case u are given an integer input 
U need to print factorial of that given input
Input:-       O/p:-
5             1
1             2432902008176640000   
20            3628800
10            6 
3             24
4
Constraints:
1<=T<=100000000000000
0<=N<=100
"""
"""
Approach 1:-Brute Force 
The Normal Brute Force Solution is to find the factorial of input using a recursion 
or from math module importing factorial method
"""
x=int(input())#Test Case Input()
fact=lambda x:1 if x<=1 else x*fact(x-1)
for _ in range(x):
    n=int(input())
    print(fact(n))
"""
Approach Two:-Using DP
The Problem With Above Solution is That Test case constraints are very high
So What happens is that we calculate factorial every time
This leads timeout
Consider the example below
let us say that testcase input is 1000000
and for all these 1000000 test cases the input is 100
So by above code we performing factorial of 100 1000000 times.
So to avoid this problem we are going to use Dynamic Programming.
Here in the constraints he is mentioning that the input value dosen't go above 100
so what we are going to do find factorials of all numbers from 0 to 100 in one single loop and store these in a list
rather than performing factorial of number for every test_case.
"""
#Implementation:-
fact=[1]#storing factorial of 0 and finding factorials of numbers by this 
for i in range(1,100):
    fact.append(i*fact[i-1])
#now the fact list stores factorial of numbers from 0 to 100
t=int(input())#testcase input
for _ in range(t):
    k=int(input())#number input
    print(fact[k])#factorial
# Code Contributed By RatnadeepYSVS
