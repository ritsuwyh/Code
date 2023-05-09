#include <bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin>>n;

    int ans=0;
    int left=1,right=n,mid;
    int valuem;    
    int valuel,valuer;
    int valuemr;
    int valuelr,valuerl;
    
    cout<<"? "<<left<<endl;
    cin>>valuel;
    cout<<"? "<<right<<endl;
    cin>>valuer;
    

    
    if(n==2){
        if(valuel<valuer){
            ans=1;
            

        }else{
            ans=2;

        }
    }else{

    while(left<right){
 
        mid=(left+right)/2;
        
        cout<<"? "<<left<<endl;
        cin>>valuel;
        
        cout<<"? "<<right<<endl;
        cin>>valuer;
        
        cout<<"? "<<left+1<<endl;
        cin>>valuelr;
        
        cout<<"? "<<right-1<<endl;
        cin>>valuerl;
        
        cout<<"? "<<mid<<endl;
        cin>>valuem;

        
        cout<<"? "<<mid+1<<endl;
        cin>>valuemr;
        


        if(valuelr>valuel && valuerl>valuer){//上凸
            if(valuel<valuer){
                ans=left;
            }else{
                ans=right;
            }
            break;

        }else if(valuelr<valuel && valuerl<valuer){//下凹
            if(valuem<valuemr){
                right=mid-1;
                
                continue;
            }else{
                left=mid+1;
                continue;
            }
        }else if(valuelr>valuel && valuerl<valuer){//先高后低
            
            if(valuel<valuer){
                ans=left;
                break;
            }

            if(valuem>valuer){
                left=mid+1;
            }else{
                if(valuem<valuemr){
                    right=mid-1;
                    continue;
                }else{
                    left=mid+1;
                    continue;
                }
            }
        }else{

            if(valuel>valuer){
                ans=right;
                break;
            }

            if(valuem>valuel){
                right=mid-1;
            }else{
                if(valuem<valuemr){
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
    if(left==right){
        ans=left;
    }
    cout<<"! "<<ans<<endl;
    return 0;
}