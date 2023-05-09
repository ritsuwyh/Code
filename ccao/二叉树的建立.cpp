#include<iostream>
using namespace std;
 
//定义节点   
typedef struct node
{
	struct node *left;
	struct node *right;
	char data;
}BiTreeNode, *BiTree; 
//BiTreeNode 就等价于 struct node 
//Bitree 等价于 struct node* 

//按照前序顺序建立二叉树
void createBiTree(BiTree &T) 
{//输入需要将二叉树补成满二叉树  ABD##E##CH###  或者 AB##C##
	char c;
	cin >> c;
	if ('#' == c)             //当遇到#时，令树的根节点为NULL，从而结束该分支的递归
		T = NULL;
	else
	{
		T = new BiTreeNode;
		T->data = c;
		createBiTree(T->left);
		createBiTree(T->right);
	}
}
 
//前序遍历输出
void preTraverse(BiTree T)
{
	if (T)
	{
		cout << T->data << " ";
		preTraverse(T->left);
		preTraverse(T->right);
	}
}
//中序遍历输出
void midTraverse(BiTree T)
{
	if (T)
	{
		midTraverse(T->left);
		cout << T->data << " ";
		midTraverse(T->right);
	}
}
//后续遍历输出
void postTraverse(BiTree T)
{
	if (T)
	{
		postTraverse(T->left);
		postTraverse(T->right);
		cout << T->data << " ";
	}
}
int main()
{
	BiTree T;               //声明一个指向二叉树根节点的指针               
	createBiTree(T);
	cout << "二叉树创建完成！" << endl;
	cout << "前序遍历：" << endl;
	preTraverse(T);
	cout << endl;
	cout << "中序遍历：" << endl;
	midTraverse(T);
	cout << endl;
	cout << "后序遍历：" << endl;
	postTraverse(T);
	return 0;
}