"""
Question:You are given an array arr[] of N integers including 0.
         The task is to find the smallest positive number missing from the array.
    Example 1:
    Input:
    N = 5
    arr[] = {1,2,3,4,5}
    Output: 6
    Explanation: Smallest positive missing number is 6.
    
    Example 2:
    Input:
    N = 5
    arr[] = {0,-10,1,3,-20}
    Output: 2
    Explanation: Smallest positive missing number is 2.
    Your Task:
    The task is to complete the function missingNumber() which returns the smallest positive missing number in the array.

    Expected Time Complexity: O(NLogN).


    Constraints:
    1 <= N <= 106
    -106 <= arr[i] <= 106
Approach:
     step 1:we can filter the given array in a way that it should contain only positive elements(excluding 0).
     step 2:sort the resultant array.
     step 3:loop over the array to find the missing element."""
def findMissingElement(arr,n):
    res=-1
    arr=list(filter(lambda x:x>0,arr))
    arr.sort()
    arr.insert(0,0)#adding 0 to the array such that we can find minimum missing element
    #print(arr)
    if len(arr)>0:
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i]>1:#difference between two consecutive elements should be <=1.
                res=arr[i]+1
                break
        if res==-1:
            res=arr[-1]+1
    else:#if length of the array containing positive elements in 0 then the minimum missing element is 1
        res=1
    return res
n=int(input())
l=list(map(int,input().split()))
print(findMissingElement(l,n))
#Code is contributed by bsandeep137
