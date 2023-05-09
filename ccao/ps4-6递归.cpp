#include<bits/stdc++.h>
using namespace std;

struct couple
{
    long x,y;
};

long cnt=0,ans=0;
long nums[1000001],temp[1000001];

bool cmp(couple a,couple b){
    return a.x<b.x;
}
//交点就是组内交点加组间交点，组内在基础情况已经被算完了排序之后不再相交
void mergex(int l,int r){
    long mid=(l+r)/2;
    long p1=l,p2=mid+1,k=l;
    cnt=0;
    while(p1<=mid && p2<=r){
        if(nums[p1]<=nums[p2]){//这条线没有潜能了 所以加
            ans+=cnt;
            temp[k++]=nums[p1++];
        }else{
            cnt++;//累积的交点，为什么要累计？因为之前交过的点后边的线一定也会交上(因为已经排序了)
            temp[k++]=nums[p2++];
        }

    }
    while(p1<=mid){
        temp[k++]=nums[p1++];
        ans+=cnt;
    }
    while(p2<=r){
        temp[k++]=nums[p2++];
    }
    for(int i=l;i<=r;i++){
        nums[i]=temp[i];
    }
    return;
}
void merge_sort(int l ,int r){
    if(l==r){
        // cout<<1;
        return;
    }
    long mid=(l+r)/2;
    merge_sort(l,mid);
    merge_sort(mid+1,r);
    mergex(l,r);
    return;
}


int main(){
    ios::sync_with_stdio(false);
    cin.tie(0), cout.tie(0);
    long n;
    cin>>n;
    couple pairs[n];
    for (long i=0;i<n;i++){
        cin>>pairs[i].x;
    }
    for (long i=0;i<n;i++){
        cin>>pairs[i].y;
    }
    sort(pairs,pairs+n,cmp);

    for(long i=0;i<n;i++){
        nums[i]=pairs[i].y;
        
    }

    merge_sort(0,n-1);

    // for(int i=0;i<n;i++){
    //     cout<<nums[i];
    // }
    cout<<ans;
    return 0;
}