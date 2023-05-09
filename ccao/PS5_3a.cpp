// (a) Develop an algorithm that, given n integers in the range 0 to k, preprocesses its input and then
// answers any query about how many of the n integers fall into a range [a, b] in O(1) time. Here, a ∈ N
// and a ∈ N. Your algorithm should use O(n + k) time for preprocessing.
#include <iostream>
using namespace std;
int main(){
    int k;
    cin>>k;
    int nums[k+1]={0};
    int n;
    cin>>n;
    //计数
    for(int i=0;i<n;i++){
        int num;
        cin>>num;
        nums[num]++;//索引代表存的数的值，而数组里面村的是这个数出现的次数
    }
    //前缀和 sum[b]-sum[a-1]   sum[i]是代表前i个数的1和
    int sum[k+1]={0};
    for(int i=1;i<k+1;i++){
        sum[i]=sum[i-1]+nums[i-1];
    }

    int a,b;
    cin>>a>>b;
    //注意sum[i]代表的是数字0到i-1的个数，
    cout<<sum[b+1]-sum[a+1-1];
    system("pause");
    return 0;
}