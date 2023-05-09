#include <bits/stdc++.h>
using namespace std;
struct node
{
    int x;
    int l;
    int r;
    bool f;
    /* data */
};
int nums[10000];

void func(node &father,int l,int r){//必须要注意函数不能改变参数的值 所以要用引用！！！！！
    if(l==r){
        father.f=true;
        father.x=nums[l];
        //cout<<"----"<<endl;
        return;//别忘了
    }

    node temp;
    int mid=(l+r)/2;
    temp.l=l;
    temp.r=mid;
    temp.f=false;

    func(temp,l,mid);
    //cout<<temp.x;
    if(temp.f){//如果左侧部分有众数temp.x 
        int cnt=0;
        for(int i=l;i<=r;i++){
            if(nums[i]==temp.x){
                cnt++;
            }
        }
        if(cnt>(r-l+1)/2){//是众数
            father.f=true;
            father.x=temp.x;
            return;
        }//如果不是就接着找右边
    }else{

        node tempx;
        tempx.l=mid+1;
        tempx.r=r;
        tempx.f=false;
        func(tempx,mid+1,r);
        if(tempx.f){//如果右侧部分有众数tempx.x 
            int cnt=0;
            for(int i=l;i<=r;i++){
                if(nums[i]==tempx.x){
                    cnt++;
                }
            }
            if(cnt>(r-l+1)/2){//是众数
                father.f=true;
                father.x=tempx.x;
                return;
            }else{//如果不是众数 那么父节点必然没有众数
                return;
            }
        }else{
            return;
        }

    }

}
int main(){
    int n;
    cin>>n;
    for(int i=0;i<n;i++){
        cin>>nums[i];
    }
    node head;
    head.f=false;
    head.l=0;
    head.r=n-1;
    func(head,0,n-1);

    if(head.f){
        cout<<"yes we have majority number:"<<head.x;
    }else{
        cout<<"there is no such number";
    }
    return 0;
}