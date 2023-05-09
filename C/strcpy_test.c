#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main() {
  //有问题的程序
  // char* arr="abcd";
  // char* arr2="123";
  // strcpy(arr,arr2);
  // printf("%s",arr);

  return 0;
}

//目标必须是可变的
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
 
int main()
{
	char* str1 = "hello world";
	char str2[10] = "*********";
	printf("%s\n", strcpy(str1,str2));
 
	return 0;
}
  system("pause");
  // str1指向的是常量字符串， char* 是常量字符串!!!!!!!!!
  // 是不可以被修改掉的，
  // 目标空间必须是可以被修改的，
  // 因为要将拷贝的字符串放在目标空间中。
  // 而源字符串可以是能够修改的、也可以是不能修改的，
  // 因为strcpy函数的第二个参数已经用const关键字修饰了，保证了拷贝过程中不会被修改。


//目标空间必须足够大以确保能放源字符串
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
 
int main()
{
	char arr1[5] = "*****";
	char arr2[] = "hello world";
	printf("%s\n", strcpy(arr1,arr2));
 
	return 0;
}

//源字符串必须以\0结尾.
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
 
int main()
{
	char arr1[10] = "**********";
	char arr2[] = { 'a','b','c','d' };
	printf("%s\n", strcpy(arr1,arr2));
 
	return 0;
}



#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
 
int main()
{
	char str1[] = "helloworld";
	char str2[10] = "*****";
    printf("%s%d\n", strncpy(str1,str2,3),1);
	printf("%s%d\n", strncpy(str1,str2,7),1);
    printf("%ld",strlen(str1)); 
	return 0;
}



// 参数说明：
// 第一个参数void* mem_loc：已开辟内存空间的首地址，通常为数组名或指针，由于其为void*，故函数能为任何类型的数据进行初始化。

// 第二个参数int c：初始化使用的内容，取器低字节部分。

// 第三个参数size_t n：需要初始化的字节数。

// 函数功能： 将已开辟内存空间 mem_loc 的首 n 个字节的值设为值 c。

#include<stdio.h>
#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int main()
{
	char char_arr[5];
	int int_arr[10];
	int* int_malloc_ptr = (int*)malloc(sizeof(int) * 15);

	memset(char_arr, 0, sizeof(char_arr));			// 数组名可以使用sizeof(arrName), 1 * 5 = 5
	memset(int_arr, 0, sizeof(int_arr));			// 4 * 10 = 40
	memset(int_malloc_ptr, 0, sizeof(int) * 15);	// 4 * 15 = 60

// 注意 2: 对于 char 类型的内存块，初始化为任何字符都没有问题。但对于其他类型的内存块，初始化的数值为 0 或 -1 时没有问题，初始化值为其他时，
// 由于取低字节进行初始化，并按照字节进行初始化，会出现与业务逻辑不符的情况。
// #include<stdio.h>
// #include<string.h>

// int main()
// {
// 	int int_arr[10];

// 1 的十六进制为0x0000000000000001 (4个字节)，低字节为0x0001。
// 使用 1 进行初始化 int 时，一个 int 会被初始化为0x0001000100010001 (4个字节)
// 	memset(int_arr, 1, sizeof(int_arr));

// 	return 0;
// }

	return 0;
}
