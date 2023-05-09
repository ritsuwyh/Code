
//https://zhuanlan.zhihu.com/p/109541633
#include <bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin>>n;
    int now=1;
    int cnt=1;

    for(int i=2;i<=n;i++){
        int f;
        cout<<"? "<<now<<" "<<i<<endl;
        cin>>f;
        if(f==1){
            cnt++;
        }else{
            cnt--;
        }
        if(cnt==-1){
            now=i;
            cnt=1;
        }

    }
    int sum=0;
    for(int i=1;i<=n;i++){
        int temp;
        cout<<"? "<<now<<" "<<i<<endl;
        cin>>temp;
        sum+=temp;

    }
    if(sum>n/2){
        cout<<"! "<<now;
    }else{
        now=-1;
        cout<<"! "<<now;
    }
    return 0;

}