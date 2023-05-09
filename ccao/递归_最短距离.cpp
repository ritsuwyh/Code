#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;

struct POINT 
{
	double x,y;
}point[10010],temp[10010];
 
double dis(POINT p1, POINT p2)
{
	return sqrt((p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y));
}
 
bool cmp(POINT a, POINT b)
{

	if (a.x != b.x)
	{
		return a.x > b.x;
	}
	else
		return a.y > b.y;
}
bool cmp1(POINT a, POINT b)
{

	if (a.y != b.y)
	{
		return a.y > b.y;
	}
	else
		return a.x > b.x;
}

 
double findMin(int l, int r)
{
	if (l == r - 1)
	{
		return dis(point[l], point[r]);
	}
	double tmp1 = findMin(l,(l + r) >> 1);
	double tmp2 = findMin(((l + r) >> 1) + 1, r);
	double Mindis,tmp, mid;
	mid = point[(l + r) >> 1].x;
	int i,j,cnt = 0;
	Mindis=min(tmp1,tmp2);
	
	for (i = l; i <= r;  i++ )
	{
		if (fabs(point[i].x - mid) < Mindis)
		{
			temp[cnt ++] = point[i];
		}
	}
	sort(temp, temp+cnt, cmp1);
	for (i = 0; i < cnt - 1;  i++)
	{
		for (j = i + 1; j < i + 7 && j < cnt;  j++)
		{
			tmp = dis(temp[i], temp[j]);
			if (tmp < Mindis)
			{
				Mindis = tmp;
			}
		}
	}
	return Mindis;
 
}

int main()
{
	int n,i,j;
	double minDis;
	cin>>n;

	for (i = 0; i < n;  i++)
	{
        cin>>point[i].x>>point[i].y;
	}
		sort(point, point+n, cmp);
		minDis = findMin(0, n-1);


		cout<<minDis;
	
	return 0;
}