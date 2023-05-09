#include <bits/stdc++.h>
using namespace std;
int bit_size(int num){
    int ans=0;
    while(num){
        num/=10;
		//>>是/2
        ans++;
    }
    return ans;
}

void radixxSort(vector<int> & source,int bits_size)//别忘了用引用
{
	
	vector<int> buckets[10];
 
	//外层循环是根据数字的位数确定的。因为是三位数，所以从2到0
	for (int pos = 0; pos < bits_size ; pos++)
	{
		//pos = 0, 表示个位数
		//pos = 1, 表示十位数
		//pos = 2, 表示百位数
		int denominator =pow(10, pos); // 取某一位数的时候需要用的分母
		for (int tmp=0;tmp< source.size();tmp++) // 按数字放入桶中
			buckets[(source[tmp] / denominator) % 10].push_back(source[tmp]);
 
		int index = 0; 
		// 从桶中取出来，放入原来的source序列中，以备下次遍历时使用 
        for(int i=0;i<10;i++){
        	//注意一个桶里面可能有多个元素所以要用vector和双重循环 
            for(int j=0;j<buckets[i].size();j++){
                source[index]=buckets[i][j];
                index++;
            }
            buckets[i].clear();//一定要清空桶中数据
        }
		
	}
}
 
 
int main()
{
	
    int n,k;//最多n位数，一共k个数据
    cin>>n>>k;
	cout<<bit_size(n);

	vector <int> sources[n+1];
	
//把数据按位数分类，把位数相同的数放入同一个桶内 
	for (int i = 0; i < k; i++)
	{
        int num;
        cin>>num;
		sources[bit_size(num)].push_back(num);
	}
 
// //每个桶内部排序 
    for(int i=1;i<n+1;i++){
    	if(sources[i].size()) 
        radixxSort(sources[i],i);
    }

//把桶连起来输出 
    for(int i=1;i<n+1;i++){
        for(int j=0;j<sources[i].size();j++){
            cout<<sources[i][j]<<" ";
        }

    }
    system ("pause");
	return 0;
}


