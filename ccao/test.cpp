#include <iostream>
#include <unordered_map>

using namespace std;
int main(){
    unordered_map<int,int> Hash;
    int x[5]={1,2,2,3,3};
    for(int i=0;i<5;i++){
        Hash[i]++;
    }
    cout<<Hash[2];
    system("pause");
    return 0;
}