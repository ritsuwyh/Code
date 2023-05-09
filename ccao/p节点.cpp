// 这道题应该用邻接矩阵来做
// 邻接表也可以
// 注意是有向还是无向
#include <iostream>
#include <vector>
#include <cstring>

using namespace std;
int calculate_deg(int a[],int n){
    int sum=0;
    for(int i=0;i<n;i++){
        sum+=a[i];
    }
return sum;
}

int main(){
   // freopen("p.in","r",stdin);
   // freopen("p.out","w",stdout);
    
    int t;
    cin>>t;
    vector<int> ans;
    
    for(int i=0;i<t;i++){
    	
        int n;
        cin>>n;
        int matrix[n][n]; //注意统一脚标和第几个
        memset(matrix,0,sizeof(matrix));
        for(int i=0;i<n-1;i++){
            int x,y;
            cin>>x>>y;
            matrix[x-1][y-1]=1;
        }
        //注意到父节点唯一 
        //求父度 自己度 孩子max度
        //int a=0,b=0,c=0;
        int cnt=0;
        for(int i=0;i<n;i++){
            int a=0,b=0,c=0;

            //求父度
            for(int j=0;j<n;j++){
                if(matrix[j][i]==1){
                    a=calculate_deg(matrix[j],n);
                    break;
                }
            }
            //求自己度
            b=calculate_deg(matrix[i],n);
            //求孩子最大度
            int temp=0;
            for(int k=0;k<n;k++){
                if (matrix[i][k]==1){
                    temp=calculate_deg(matrix[k],n);
                    if(temp>c){
                        c=temp;
                    }
                }
            }
            
            /*if(b>=a &&b>=c){
                ans.push_back(b);
            }*/
            
            if(b>=a && b>=c){
            	cnt++;
			}
        }
    
        ans.push_back(cnt);


    }





    for(int i=0;i<ans.size();i++){
        cout<<ans[i]<<endl;
    }
    return 0;
    } 