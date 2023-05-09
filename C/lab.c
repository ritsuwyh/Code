#include <stdint.h>
#include <stdio.h>
uint64_t modx(uint64_t x,uint64_t q){
    while(x>=q){
        x-=q;
    }
    return x;
}

uint64_t multimod(uint64_t a, uint64_t b, uint64_t m) {

    uint64_t ans=0;
    uint64_t temp=0;
    while(a){
    if(a&1){
        ans=modx(ans+b,m);

    }
        a>>=1;
        b<<=1;
    }
    // if(a<b){// let b smaller
    //   temp=a;
    //   a=b;
    //   b=temp;
    // }
    // while(b)
    // {
    //     if(b&1)     //&操作是判断b的每一位是0还是1，是1的话就要加上
    //         ans=(ans+a)%m;
    //     a<<=1;
    //     a%=m;    //每次乘以2，实现2^i操作
    //     b>>=1;        //对b的每一位操作
    // }
    return ans;

}

int main(){
    printf("%ld",multimod(123,456,789));
    return 0;
}
