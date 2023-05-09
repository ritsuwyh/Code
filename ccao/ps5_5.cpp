#include <cmath>
#include <iostream>
#include <algorithm>
using namespace std;
struct Node
{
    int content;
    Node* lchild;
    Node* rchlid;
};
int ans=1;
Node* target_node;
//按照前序顺序建立二叉树
void createBiTree(Node* &T) 
{//输入需要将二叉树补成满二叉树  ABD##E##CH###  或者 AB##C##
	int c;
	cin >> c;
	if (c == 0)             //当遇到#时，令树的根节点为NULL，从而结束该分支的递归
		T = NULL;
	else
	{
		T = new Node;
		T->content = c;
		createBiTree(T->lchild);
		createBiTree(T->rchlid);
	}
}


int largest_complete_subtree(Node *root){
    
    if(!(root->lchild) || !(root->rchlid)){//如果这个节点有缺失的孩子，那么到达递归终点.
        return 1;
    }
    int left_max_height=largest_complete_subtree(root->lchild),right_max_height=largest_complete_subtree(root->rchlid);
    int temp=min(left_max_height,right_max_height)+1;
    
    if(temp>ans){//更新最大值
        ans=temp;
        target_node=root;
    }

    return temp;
}
int main(){
    Node* root=NULL;
    createBiTree(root);
    largest_complete_subtree(root);
    cout<<ans;
    system("pause");
    return 0;
}