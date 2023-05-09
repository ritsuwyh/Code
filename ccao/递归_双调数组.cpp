#include <iostream>

using namespace std;

int main(){
    int n;
    cin>>n;

    int ans=0;

    int left=1,right=n,mid=(left+right)/2;
    int valuem;    
    int valuel,valuer;
    int valuemr;
    int valuelr,valuerl;
    
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

    if(n==2){
        if(valuel<valuer){
            ans=1;
            

        }else{
            ans=2;

        }
    }
    else{
        int x=0;
    while(left<=right){
        
        if(left==right){
            ans=left;
            break;
        }
 
        mid=(left+right)/2;
        

        


        switch (x)
        {
        case 0:break;
        case 1:valuer=valuem;        
        cout<<"? "<<right-1<<endl;
        cin>>valuerl;
        
        cout<<"? "<<mid<<endl;
        cin>>valuem;
            
        cout<<"? "<<mid+1<<endl;
        cin>>valuemr;
        break;

        case 2:valuel=valuemr;
        cout<<"? "<<left+1<<endl;
        cin>>valuelr;
        cout<<"? "<<mid<<endl;
        cin>>valuem;
            
        cout<<"? "<<mid+1<<endl;
        cin>>valuemr;
        break;

        }
        x=0;
        

        if(valuelr>valuel && valuerl>valuer){//上凸
            if(valuel<valuer){
                ans=left;
            }else{
                ans=right;
            }
            break;

        }else if(valuelr<valuel && valuerl<valuer){//下凹
            if(valuem<valuemr){
                x=1;
                right=mid;
                
                
            }else{
                x=2;
                left=mid+1;
                
            }
        }else if(valuelr>valuel && valuerl<valuer){//先高后低
            
            if(valuel<valuer){
                ans=left;
                break;
            }

            if(valuem>valuer){
                x=2;
                left=mid+1;
            }else{
                if(valuem<valuemr){
                    x=1;
                    right=mid;
                    
                }else{
                    x=2;
                    left=mid+1;
                    
                }
            }
        }else{

            if(valuel>valuer){
                ans=right;
                break;
            }

            if(valuem>valuel){
                x=1;
                right=mid;
            }else{
                if(valuem<valuemr){
                    x=1;
                    right=mid;
                    
                }else{
                    x=2;
                    left=mid+1;
                    
                }            
            }
        }

    }

    }
    cout<<"! "<<ans<<endl;
    return 0;
}