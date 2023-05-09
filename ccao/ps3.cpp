#include <bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin>>n;
    int a[n];
    int ans=0;
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    int left=0,right=n-1;
    
    if(n==2){
        if(a[0]<a[1]){
            ans=1;
            

        }else{
            ans=2;

        }
    }else{

    while(left<right){
 
        int mid=(left+right)/2;
        
        if(a[mid-1]>a[mid]&&a[mid]<a[mid+1]){
            ans=mid+1;
            break;
        }

        if(a[left+1]>a[left] && a[right-1]>a[right]){//上凸
            if(a[left]<a[right]){
                ans=left+1;
            }else{
                ans=right+1;
            }
            break;

        }else if(a[left+1]<a[left] && a[right-1]<a[right]){//下凹
            if(a[mid-1]<a[mid]&& a[mid]<a[mid+1]){
                right=mid-1;
                continue;
            }else{
                left=mid+1;
                continue;
            }
        }else if(a[left+1]>a[left] && a[right-1]<a[right]){//先高后低
            
            if(a[left]<a[right]){
                ans=left+1;
                break;
            }

            if(a[mid]>a[right]){
                left=mid+1;
            }else{
                if(a[mid-1]<a[mid]&& a[mid]<a[mid+1]){
                    right=mid-1;
                    continue;
                }else{
                    left=mid+1;
                    continue;
                }
            }
        }else{

            if(a[left]>a[right]){
                ans=right+1;
                break;
            }

            if(a[mid]>a[left]){
                right=mid-1;
            }else{
                if(a[mid-1]<a[mid]&& a[mid]<a[mid+1]){
                    right=mid-1;
                    continue;
                }else{
                    left=mid+1;
                    continue;
                }            
            }
        }

    }
    }
    cout<<ans;
    return 0;
}