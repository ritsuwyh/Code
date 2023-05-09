#include <iostream>
using namespace std;
struct Node
{
    int lc,rc;
};
Node tree[1000001];
int in_order[1000001];//为了简化函数的参数，使用全局变量，声明的大小依据题干的数据范围
int pre_order[1000001];
void construct_tree(int s1,int e1,int s2,int e2){//注意到没有左节点那么就必然没有右节点。这句话是错的！！！！
    // cout<<s1<<" "<<e1<<" "<<s2<<" "<<e2<<endl;
    int find=pre_order[s1];
    if(s2==e2){
        tree[find].lc=-1;
        tree[find].rc=-1;
        return;

    }


    int index=0;
    for(int i=s2;i<=e2;i++){
        if(in_order[i]==find){
            index=i;
        }
    }
    int left_len=index-s2;
    int right_len=e2-index;


//左右孩子都没有
    if(left_len==0 && right_len==0){
        tree[find].lc=-1;
        tree[find].rc=-1;
        return;
    }
//只有左孩子没有右孩子
    if(right_len==0){
        tree[find].lc=pre_order[s1+1];
        tree[find].rc=-1;
        construct_tree(s1+1,e1-right_len,s2,index-1);
        return;
    }
    if(left_len==0){
        tree[find].lc=-1;
        tree[find].rc=pre_order[s1+1];
        construct_tree(s1+1+left_len,e1,index+1,e2);
        return;
    }


    tree[find].lc=pre_order[s1+1];
    tree[find].rc=pre_order[s1+1+left_len];

    construct_tree(s1+1,e1-right_len,s2,index-1);
    construct_tree(s1+1+left_len,e1,index+1,e2);
    return;


}
int main(){
    int n;
    cin>>n;
    //in-order 中序

    for(int i=0;i<n;i++){
        cin>>in_order[i];
    }

    //pre_order 前序
    for(int i=0;i<n;i++){
        cin>>pre_order[i];
    }


    construct_tree(0,n-1,0,n-1);

    for(int i=1;i<=n;i++){
        cout<<tree[i].lc<<" "<<tree[i].rc<<endl;
    }
    system ("pause");
    return 0;
}