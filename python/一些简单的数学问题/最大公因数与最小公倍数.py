
#! lcm是最小公倍数     gcd是最大公因数
#! gcd 和 lcm 的性质 lcm(a,b)*gcd(a,b)=a*b 等
#! 辗转相除法求最大公因数 gcd(a,b)=gcd(b,a mod b)
#! 如果 af1=bf2+cf3 那么f2和f3的公因式也是f1的因式 
def gcd(a,b):#! 传入的顺序无所谓
    if b==0:
        return a
    return gcd(b,a%b)
print(gcd(3,9))
#! 凭此可以写一个互质判断
