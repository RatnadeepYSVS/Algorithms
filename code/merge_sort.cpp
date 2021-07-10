#include<bits/stdc++.h>
using namespace std;
#define FIO ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);

typedef vector<long> vl;                    // naming the vector<long> as vl so that we can write vl instead of vector<long> :)

void merge_Sort(vl &a,int start,int mid,int end){
    int len=end-start+1;		    //taking length of array after combines
    vl b(len);				    //initializing the array of length=len
    int i=start,j=mid+1,k=0;		    //initializing i with the first index of array part-1 and j with first index of array part-2
    while(k<len){			    //taking a while loop and running it over len times
        if(i>mid) b[k]=a[j++];		    //if the elements of array-1 are over then we should add the array-2 elements directly into array-b 
        else if(j>end) b[k]=a[i++];	    //if the elements of array-2 are over then we should add the array-1 elements directly into array-b
        else if(a[i]<=a[j]) b[k]=a[i++];    //if the element of array-1 at index i is less than element of array-2 at index j,then add array-1 element at i into array-b and increment the i;
        else {
            				    //if the element of array-1 at index i is greaterthan or equal to element of array-2 at index j,then add array-2 element at j into array-b and increment the j;
            b[k]=a[j++];}		
        k++;  				    // increments the k
    }
    for(int i=start;i<=end;i++)
        a[i]=b[i-start];		    //update all the values from start to end of array a with the array b
}

void merge_Help(vl &v,int start,int end){
    if(start>=end) return;
    long mid=start+end;		
    mid/=2;				         //taking the middle index value of the array.
    merge_Help(v,start,mid);	//these function calls were done upto the sub array length not equal to 1.
    merge_Help(v,mid+1,end);	//the functions were called such that the array is split into subarray of into half.
    merge_Sort(v,start,mid,end);	//After the division of array is done this function call is made to merge the divided parts in sorted order.
}

int main(){
FIO
    int t;cin>>t;    	//taking input of count of test cases
    while(t--){
            long n;cin>>n;       	//input array length
            vl v(n);	     	//array initialization
            for(auto i=0;i<n;i++) 
            cin>>v[i];	     	//getting array elements	
            merge_Help(v,0,n-1); 	//calling the helper function which divides the array into sub array upto length=1; 
            for(auto i=0;i<n;i++)	
            cout<<v[i]<<" ";	//printing the array after doing merge sort
            cout<<"\n";
        }
    return 0;
}
//Code Contributed By Im_A_Negative1