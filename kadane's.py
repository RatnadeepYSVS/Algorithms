"""
Question:
Consider an list  containg n elements.
You should return the maximum sum of the subarrays from the list of n elements
A Quick Note On Subarrays and Subsets.
Subarrays are different than Subsets
Subarrays maintain order where as subsets dosen't maintain the order
example:-
here -2 2 0 can be subset and subarray
here -2 0 7 can't be subarray but can be subset
Example:
I/p:-		
5
-2 2 0 6 7
O/p:-15
Constraints:-
1<=n<=10**5
-10**7<=a[i]<=10**7
Explanation:-
subarrays and their sums:-
-2  sum=-2       2 sum=2      0          6 sum=6   7 sum=7   
-2 2 sum=0       2 0 sum=2    0 6 sum=6  6 7 sum=13
-2 2 0 sum=0     2 0 6 sum=8  0 6 7 sum=13
-2 2 0 6  sum=6  2 0 6 7 sum=15
-2 2 0 6 7 sum=13
As We Can Observe The MaxSum Among All Of These SubArrays is 15
so print 15
"""
# Approach 1:Brute Force technique
# Brute force technique:
# The normal approach we do is that 
# initialize a maxsum = -4792831789437289758924789(random value)
# then create a loop from start value to end value of list
# initiale subsum=0
# then we create  another loop inside this mainloop upto i elements and calculate the subsum
# then we compare subsum with maxsum if subsum is greater than max sum then we update it
# and finally print the maxsum result
# ___
# Time Complexity:-O(n**2)
#Implementation:-
n=int(input())
x=list(map(int,input().split()))
maxsum=-2834920890532890#
for i in range(len(x)):
	cursum=0
	for j in range(i+1,len(x)):
		cursum+=x[j]
	maxsum=max(maxsum,cursum)
print(maxsum)
# Kadane's Algorithm
# The basic idea of this Algorithm is first initialize cursum,maxsum to starting value of the list
# Then Iterate a loop from rest of the elements
# Compute Cursum with i value check if i value is greater than the currsum value if yes update cursum to i
# then if cursum is greater than maxsum and update maxsum
# Approach:-
# Initialize maxsum,cursum to starting value of the list
# cursum=-2 maxsum=-2
# then start the loop from 2nd item to end of the list
# compute the cursum with this i value
# Note:- i values are not indice values they are the values of the elements in list
# cursum=cursum+i
# Now check whether this cursum is greater than i value if it is greater update cursum to i
# i=2
# cursum=0
# here i is greater than cursum so cursum=2
# then check it whether it's greater than maxsum
# maxsum=-2
# cursum=2
# so we have to update maxsum to cursum 
# Therefore maxsum = 2
# for i=0
# cursum=2
# maxsum=2
# cursum is greater than i so no need to update cursum
# maxsum==cursum so no need to update
# for i=6
# cursum=2
# maxsum=2
# now cursum=cursum+i now cursum=8 cursum is greater than i
# so cursum=8
# now maxsum is less than cursum
# so maxsum=8
# for i=7
# cursum=8
# maxsum=8
# now cursum = 15 (cursum=cursum+i where i=7 here)
# check this with i value cursum is greater than i so update cursum
# now maxsum is less than cursum  so we need to update maxsum
# maxsum=15
# traversal is completed
# so we print 15 which is the maximum of all subarray sums
#___
#Time complexity:-O(N)
x=list(map(int,input().split()))
maxsum=cursum=x[0]#as mentioned above
for i in x[1:]:
    cursum=max(cursum+i,i)#checks whether computed cursum is greater than i if this happens it updates cursum to i
    maxsum=max(cursum,maxsum)# updates maxsum if maxsum if greater than the cursum
print(maxsum)
#Code Contributed By RatnadeepYSVS
