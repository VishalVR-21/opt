#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int x;
	cin>>x;
	while(x--)
	{
	    int a;
	    cin>>a;
	    vector<int> arr;
	    int sum =0;
	    for(int i =0;i<a;i++)
	    {
	        int x;
	        cin>>x;
	        sum = sum+x;
	        arr.push_back(x);

	    }
	    int key = sum/a;
	    int res = 0;
	    for(int i=0;i<a;i++)
	    {
	        res = abs(res-arr[i]);
	    }
	    cout<<res<<endl;
	}
	return 0;
}
