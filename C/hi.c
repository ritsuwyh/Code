#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>
char buf[128]="********************";
int numtochar(char* out,int idx,unsigned long num, int base){
  if(num==0){
    out[idx++]='0';
    return idx;
  }

  char table[]="0123456789abcdef";
  int cnt=0;
  int nums[100];
  while(num!=0){
    nums[cnt++]=num%base;
    num=num/base;
  }
  int i;
  for(i=cnt-1;i>=0;i--){
    out[idx++]=table[nums[i]];
  }
  return idx;
}
int Decitochar(char* out,int idx,int num){
  if(num<0){
    out[idx++]='-';
    num=-num;
  }
  int now_idx;

  now_idx=numtochar(out,idx,num,10);
  return now_idx;

}

int Strtochar(char* out,int idx,char* str){
  int i=0;
  while(str[i]!='\0'){
    out[idx++]=str[i++];
  }
  return idx;
}


//https://baike.baidu.com/item/sprintf/9703430?fr=kg_general
int my_sprintf(char *out, const char *fmt, ...) {
      int i = 0;
      int j = 0;
	/* 可变参第一步 */
    va_list va_ptr;

	/* step2 */
    va_start(va_ptr, fmt);

	/* 循环打印所有格式字符串 */
    while (fmt[i] != '\0')
    {
		/* 普通字符正常打印 */
		if (fmt[i] != '%')
		{
    	out[j++]=fmt[i++];
			continue;
		}
		
		/* 格式字符特殊处理 */
		switch (fmt[++i])   // i先++是为了取'%'后面的格式字符
		{
		    /* 根据格式字符的不同来调用不同的函数 */
			case 'd':j= Decitochar(out,j,va_arg(va_ptr,int));           
			  		  break; 
		    // case 'o': printOct(va_arg(va_ptr,unsigned int));  
			  // 		  break;
		    // case 'x': printHex(va_arg(va_ptr,unsigned int));  
			  // 		  break;
		    // case 'c': putchar(va_arg(va_ptr,int));            
			  // 		  break;
		    // case 'p': printAddr(va_arg(va_ptr,unsigned long));
			  // 		  break;
		    // case 'f': printFloat(va_arg(va_ptr,double));      
			  // 		  break;
		    case 's': j=Strtochar(out,j,va_arg(va_ptr,char *));
					  break;
			default : break;
		}

		i++; // 下一个字符
    }

	/* 可变参最后一步 */
  va_end(va_ptr);

 	out[j]='\0';//j shi suo yin
  return j;

}
int main() {
	char sx[]="hehehehehe";
	my_sprintf(buf+5,"%d + + + 12 23131 + %s%d",0,sx,45454);
	//my_sprintf(buf,"%d=%d",12,1334);
	printf(buf);
    system("pause");
	return 0;
}