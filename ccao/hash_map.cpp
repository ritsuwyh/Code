#include <iostream>
using namespace std;
int base_hash_func(int k){
    return k;
}
int second_hash_func(int k,int m){
    return 1+k%(m-1);
}
int main(){
    int m;
    cin>>m;
    int nums[m]={0};
    for(int i=0;i<9;i++){
        int num;
        cin>>num;
        int cnt=0;
        while(nums[(base_hash_func(num)+cnt)%m]!=0){
            cnt++;
        }
        nums[(base_hash_func(num)+cnt)%m]=num;
    }
    for(int i=0;i<13;i++){
        cout<<nums[i]<<" ";
    }   
    system("pause");
    return 0;

}