"""
Problem:-You are given a range.And Print all the Modified kaprekar numbers in the given range
Modified Kaprekar numbers:-
It's a number if u square it and split if the sum of the numbers splitted is given number Then it's said to be
kaprekar number.
example:- 9
9^2 = 81 splitting 81 we get 8,1 sum of these is 9
hence 9 is kaprekar
But Modified kaprekar number having d digits is a number and square of this number 
is divided into 2 parts left and right.
the right part contains d digits long and left part is remaining digits.
example:-45 d=2 
45**2==2025
right part must be 2 digits so right=25
left part consists remaining digits=20
so left + right =20+25 =45
so 45 is a modified kaprekar number.
I/p:-               O/p:-
1                   1 9 45 55 99
100
"""
"""
Approach
We square the number and typecast to string
store d digits of this string in right part
and remaining digits of this string in left part
using -ve indexing and type cast these both parts
to int and check the sum to i value.
"""
x=[int(input()) for _ in range(2)]#Taking Range Input
xx,kk=x[0],x[1]
mfkp=[]#Initializing modified kaprekars number list
for i in range(xx,kk+1):
    k=list(str(i**2))#Typecast square of i to string 
    c=str(i)
    cc=len(c)#To get no of digits of i
    """
    k[-cc:] this stores values of d digits long in rig
    k[:-cc] this stores values of remaining digits in lef if empty 
    taking lef as 0.
    """
    try:
        lef=int("".join(k[:-cc]) or "0")
        rig=int("".join(k[-cc:]))
        if lef+rig==i:#Checking the sum of both lef and rig is equal to i 
            mfkp.append(i)#adding to modified kaprekars list if true
    except:
        pass
if len(mfkp):
    print(*mfkp)#Printing all modified kaprekar numbers

#Code Contributed by RatnadeepYSVS. 