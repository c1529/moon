#include<iostream>
using namespace std;
void sort_1(int a[], int n)   //冒泡
{
	int i, j, temp;
	for (i = 0; i < n - 1; i++)
	{
		for (j = 0; j < n - i - 1; j++)
		{
			if (a[j] > a[j + 1])
			{
				temp = a[j];
				a[j] = a[j + 1];
				a[j + 1] = temp;
			}
		}
	}
}
void sort_2(int num[], int n)  //选择
{
	int i, j, k,min,temp;
	for (i = 0; i < n-1; i++)
	{
		min = i;
		for (j = i; j < n; j++)
		{
			if (num[i] > num[j ])  //不能把i换成min，因为这个是为索引为i的地址选择合适的值，循环里的min记录着最小值的索引
			{
				min = j;
				temp = num[i];
				num[i] = num[j];
				num[j] = temp;
			}
		}
	}
}
void print(int num[], int n)
{
	int i;
	for (i = 0; i < n; i++)
	{
		cout << num[i] << endl;
	}
}
int main()
{
	int n;
	int num[5] = { 5,16,3,18,17 };
	n = sizeof(num) / sizeof(int);
	sort_2(num, n);
	print(num, n);
	return 0;
}




