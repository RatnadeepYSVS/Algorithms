"""
Problem:-Given A List Of Integers.Your Task is to display list consisting of products except that current number.
Example : 
Input:-             Output: 
N=5(size)           120 60 40 30 24
1 2 3 4 5
"""
"""
Approach 1
The simplest approach is to calculate the product of List Given.And Dividing it with each element in the list.
for given example 
product of List is 120
120//1 =120,120//2=60,120//3=40,120//4=30,120//5=24
"""
#Implementation
from functools import reduce
x=int(input())#Size input
l=[int(i) for i in input().split()]#List Input
product=int(reduce(lambda x,y:x*y,l))#Calculating the product
print([product//i for i in l])#The product list
"""
But the problem with above approach is that if the given list contains number 0.
Then it fails because the product of entire list will be 0
And Two problems may arise
1.0 divided by anything is 0(Logical Error)
2.As the list contains number 0 0//0 will also throw an error.
let's consider the example below
N=2                           O/p:-12 0
0 12                                 
But with above approach
Product of entire list is 0 And
0//12==0.
0//0 will throw an error.
"""
"""
Another Approach Overcoming the above problem.
Approach 2:-
1.Calculate all the left products of the list and store it.
2.Calculate all the right products of the list and store it and reverse the list.
3.Muitiply both the lists which are stored.This is the resultant list.
let us take the above example
list = [1,2,3,4,5]
left of 1 is nothing so we take that as 1 and add it in the left list.
left_list=[1]
left of 2 is 1 so we take that and multiply it with last value of left list which is 1 and store it
left_list=[1,1]
left of 3 is 2 so we take that and multiply it with last value of left list which is 1 and store it
left_list=[1,1,2]
left of 4 is 3 so we take that and multiply it with last value of left list which is 2 and store it
left_list=[1,1,2,6]
left of 5 is 4 so we take that and multiply it with last value of left list which is 6 and store it
left_list=[1,1,2,6,24]
Now we need to get the right product list of input list
So there is no right side element to 5. so we append 1 in right list.
right_list=[1]
The right side element of 4 is 5.So we multiply that with last element in right list and add it to right list.
right_list=[1,5]
The right side element of 3 is 4.So we multiply that with last element in right list and add it to right list.
right_list=[1,5,20]
The right side element of 2 is 3.So we multiply that with last element in right list and add it to right list.
right_list=[1,5,20,60]
The right side element of 1 is 2.So we multiply that with last element in right list and add it to right list.
right_list=[1,5,20,60,120]
so reversing the right_list we get that as [120,60,20,5,1].
so multiplying both lists we get:-
1.120*1=120
2.60*1=60
3.20*2=40
4.6*5=30
5.1*24=24
so resultant_list=[120,60,40,30,24] which is equivalent o/p.
"""
#Implementation
x=int(input())#Size input
l=[int(i) for i in input().split()]#List Input
left_list=[1]#storing left product values
right_list=[1]#storing right product values
for i in l[:x-1]:
    left_list.append(left_list[-1]*i)#calculating the left product values
rev=l[::-1]
for i in rev[:x-1]:
    right_list.append(right_list[-1]*i)#calculating the right product values
print([i*j for i,j in zip(left_list, right_list[::-1])])#resultant_list
#Implementation without right_list
x=int(input())
l=[int(i) for i in input().split()]
left_list=[1]
for i in l[:x-1]:
    left_list.append(left_list[-1]*i)
c=1
for i in range(1,x+1):
    left_list.append(c)
    c*=l[-i]
for i in range(x):
    last_val=left_list.pop()
    left_list[i]*=last_val
print(left_list)
