"""
Question:-
Given A list of N elements
You Should Print The First Duplicate of The List If Exists Else Print -1
I/p:-                 O/p:-                    
7                     3
1 5 3 4 3 5 6
I/p:-                 O/p:-                    
5                     -1
1 2 3 4 5
Constraints:-
1<=n<=10**6
1<=A[i]<=10**6
"""
"""
Approach:-
For This We Can Use Either HashMap(Dictionary) or Set.
Here we are using hashmap or set because they perform operations very fast compared to list.
run a loop add values in this hashmap by default hashmap or set.
if value is existing in set or hashmap break the loop print the value.
else print -1 
"""
x=int(input())#Size input
k=list(map(int,input().split()))#Integers Input
z=set()#Intialize Set
for i in k:
    if i in z:
        print(i)
        break
    z.add(i)
else:
    #This only gets Printed If The Above Loop Runs Successfully without Break
    print(-1)
#Code Contributed By  RatnadeepYSVS
