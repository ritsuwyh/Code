
#include <iostream>
#include <algorithm>
using namespace std; 
/* run this program using the console pauser or add your own getch, system("pause") or input loop */
//还有一点很重要，不能在结构体声明中初始化结构体成员，因为结构体声明只是创建一个新的数据类型，还不存在这种类型的变量。例如，以下声明是非法的：
struct Node{
    int key=-1;
    int _cnt=1;

    int sub_tree_size=0;
	Node* _parent=NULL;
    Node* _left=NULL;
    Node* _right=NULL;
    int _bf=0;//平衡因子 bf 变量(平衡因子 = 右子树高度 - 左子树高度)
    // Node(int cnt=1,int bf=0, Node* ): _cnt(cnt),_bf(bf){}
};
Node* _root=new Node;//Node* _root=NULL;

void RotateL(Node* &parent)
{
  Node* subR=parent->_right;
  Node* subRL=subR->_left;
  // 更新节点之间的连接关系
  parent->_right=subRL;
  if(subRL!=NULL)// subRL不为空才需要更新它的父亲
  {
    subRL->_parent=parent;
  }
    //至此第一步完成，建立了一个双向链接
  subR->_left=parent;
  Node* pparent=parent->_parent;//注意写的先后顺序 在更新parent的父节点之前要先获取父节点的父节点
  parent->_parent=subR;
  if(pparent==NULL)// parent为根时的处理
  {
    _root=subR;
    subR->_parent=NULL;
  }
  else 
  {
    if(pparent->_left==parent)//如果parent是左孩子
    {
      pparent->_left=subR;
    }
    else 
    {
      pparent->_right=subR;
    }
    subR->_parent=pparent;
  }
  // 更新平衡因子
  parent->_bf=subR->_bf=0;
  // 更新子树大小

  subR->sub_tree_size=parent->sub_tree_size;
  //注意孩子为空的情况
  parent->sub_tree_size=parent->_cnt*parent->key;
  if(parent->_left!=NULL){
      parent->sub_tree_size+=parent->_left->sub_tree_size;
  }
  if(parent->_right!=NULL){
      parent->sub_tree_size+=parent->_right->sub_tree_size;
  }

//parent->sub_tree_size=parent->_cnt+parent->_left->sub_tree_size+parent->_right->sub_tree_size;

}

void RotateR(Node* &parent)
{
  Node* subL=parent->_left;
  Node* subLR=subL->_right;
  // 更新节点之间的连接关系
  parent->_left=subLR;
  if(subLR!=NULL)
  {
    subLR->_parent=parent;
  }
  subL->_right=parent;
  Node* pparent=parent->_parent;
  parent->_parent=subL;
  if(pparent==NULL)
  {
    _root=subL;
    subL->_parent=NULL;
  }
  else 
  {
    if(pparent->_left==parent)
    {
      pparent->_left=subL;
    }
    else if(pparent->_right==parent)
    {
      pparent->_right=subL;
    }
    subL->_parent=pparent;
  }
  // 更新平衡因子
  parent->_bf=subL->_bf=0;

  subL->sub_tree_size=parent->sub_tree_size;
  parent->sub_tree_size=parent->_cnt*parent->key;
  if(parent->_left!=NULL){
      parent->sub_tree_size+=parent->_left->sub_tree_size;
  }
  if(parent->_right!=NULL){
      parent->sub_tree_size+=parent->_right->sub_tree_size;
  }

}

void RotateRL(Node* &parent)
{
  Node* subR=parent->_right;
  Node* subRL=subR->_left;
  int flag=subRL->_bf;
  // 依次旋转
  RotateR(subR);
  RotateL(parent);
  // 更新平衡因子
  if(flag==1)
  {
    parent->_bf=-1;
  }
  else if(flag==-1) 
  {
    subR->_bf=1;
  }
}


void RotateLR(Node* &parent)
{
  Node* subL=parent->_left;
  Node* subLR=subL->_right;
  int flag=subLR->_bf;// 记录subLR的平衡因子，最后要依据它来更新其他节点的平衡因子
  // 依次旋转
  RotateL(subL);
  RotateR(parent);
  // 根据subLR平衡因子的值更新不同插入情况下的平衡因子
  if(flag==1)// 说明是在subLR的右子树插入的，那么subLR的左子树变为subL的右子树，subL平衡因子变为-1，subLR和parent的为0
  {
    subL->_bf=-1;
  }
  else if(flag==-1)// 说明是在subLR的左子树插入的，subLR的右子树最后会被分给parent作为左子树，parent的平衡因子变为-1，subL和subLR的平衡因子变为0
  {
    parent->_bf=1;
  }
}

void rebalance(Node *&parent,Node *&cur){

        	if(parent->_bf==2)
            {
            if(cur->_bf==1)// 右子树的右子树也高 -->  左单旋
            {
              RotateL(parent);
            }
            else if(cur->_bf==-1)// 右子树的左子树也高  -->  右左双旋
            {
              RotateRL(parent);
            }
          }
          else if(parent->_bf==-2)// 左子树高
          {
            if(cur->_bf==-1)// 左子树的左子树也高  -->  右单旋
            {
              RotateR(parent);
            }
            else if(cur->_bf==1)// 左子树的右子树也高  -->  左右双旋
            {
              RotateLR(parent);
            }
          }
}

bool AVLSEARCH(Node* &_root,int target){
    Node* p=_root;
    while(p!=NULL){
        if(p->key==target){
            return true;
        }
        if(target<p->key){
            p=p->_left;
        }else{
            p=p->_right;
        }

    }
    return false;
}

Node* AVLMIN(Node *&u){
    Node* p=u;
    while(p->_left!=NULL){

        p=p->_left;
    }
    
    return p;
}
int AVLREMOVE(Node *&_root,int z){
    if(AVLSEARCH(_root,z)==false){
        return 0;
    }
    //删除的元素存在
    int ans=0;
    Node* cur=_root;
   // Node* parent=NULL;//注意我们需要记录父节点,因为要维护双向链表
    while(cur->key!=z){

        cur->sub_tree_size-=z;
        if(z<cur->key){
            cur=cur->_left;
        }else{
            cur=cur->_right;
        }
    }
    ans=cur->_cnt;
    cur->sub_tree_size-=z;
    cur->_cnt--;
    if(cur->_cnt==0){
        cout<<"";
       
    }else{
        
        return ans;
    }
    return ans;
    
}

void Delete_func(Node* &p){
    if(p->)
    

}
void keep_func(){

}

void AVLINSERT(Node *&_root,int z){
// 空树的话，就让插入的那个节点作为根
      
      if(_root->key==-1)
      {
          _root->key=z;
          _root->sub_tree_size=z;
          return;
      }
      // 不是空树，就按照搜索树的性质找到插入的位置和它的父亲
      Node* cur=_root;
      Node* parent=NULL;//注意我们需要记录父节点,因为要维护双向链表
      while(cur!=NULL)
      {
        parent=cur;//类似于之前的题的操作,边遍历边更新
        if(cur->key==z){
            cur->sub_tree_size+=z;
            cur->_cnt++;
            return;
        }

        if(z<cur->key)
        {
            cur->sub_tree_size+=z;
            cur=cur->_left;
        }
        else 
        {
            cur->sub_tree_size+=z;
            cur=cur->_right;
        }
      }

    Node* x=new Node;
      // 更新关系，插入节点
    //维护双向链表 parent和child
      x->_parent=parent;
      x->key=z;
      x->sub_tree_size=z;

      if(parent->key < x->key)
      {
        parent->_right=x;
      }
      else 
      {
        parent->_left=x;
      }
      
      cur=x;
      parent=cur->_parent;
      while(parent!=NULL){
      
        // 向上更新平衡因子
        if(cur==parent->_left)
        {
          --(parent->_bf);
        }
        else 
        {
          ++(parent->_bf);
        }
        // 检查是否需要调整
        // 0的话就平衡了
        // -1或1的话还要向上更新
        // -2或2的话需要旋转处理
        if(parent->_bf==0)// 平衡因子为0，整棵树高度依然不变，只是补了原来低的那边，依然平衡
        {
          break;
        }
        else if(parent->_bf==1 || parent->_bf==-1)// 整棵树高度增加了，但是这颗树依然平衡，再往上是否平衡不知道需要继续验证
        {
          cur=parent;
          parent=parent->_parent;
        }
          
        else if(parent->_bf==2 || parent->_bf==-2)
        {
            rebalance(parent,cur);
            break;
        }
      }
}

int func(Node* _root,int upbound){
  int ans=0;
  Node* p=_root;
  while(p!=NULL){

    if(p->key<upbound){
      if(p->_left!=NULL){
      ans+=p->_left->sub_tree_size+p->_cnt*p->key;
      }else{
        ans+=p->_cnt*p->key;
      }
      p=p->_right;

    }else if(p->key==upbound){
      if(p->_left!=NULL){
        ans+=p->_left->sub_tree_size+p->_cnt*p->key;
      }else{
        ans+=p->_cnt*p->key;
      }
      return ans;
    }else{
      p=p->_left;
    }
    
  }
  return ans;
}
int AVLRANGECNTSUM(Node* _root,int lowerbound,int upperbound){
  return func(_root,upperbound)-func(_root,lowerbound);
}

void midTraverse(Node *_root)
{
	if (_root!=NULL)
	{
		midTraverse(_root->_left);
		cout << _root->key<<" " <<_root->_cnt<<" "<<_root->sub_tree_size<<" "<<_root->_bf <<endl;
		midTraverse(_root->_right);
	}
}


int main(int argc, char** argv) {

  int q,p;
  cin>>q>>p;
  int lans=0;
  for(int i=0;i<q;i++){
    int option;
    cin>>option;
    if(option==0){
      int x;
      cin>>x;
      AVLINSERT(_root,(x+lans)%p);
    }else if(option==1){
      int x;
      cin>>x;
      cout<<AVLREMOVE(_root,(x+lans)%p)<<endl;
    }else{
      int l,r;
      cin>>l>>r;
      l=(lans+l)%p;
      r=(lans+r)%p;
      if(l>r){
        swap(l,r);
      }
      int temp=AVLRANGECNTSUM(_root,l,r);
      cout<<temp<<endl;
      lans=temp;
    }
    
  }


    // AVLINSERT(_root,16);
    // AVLREMOVE(_root,16);

    // AVLINSERT(_root,13);
    // AVLREMOVE(_root,13);

    // AVLINSERT(_root,14);
    // AVLINSERT(_root,13);
    // AVLINSERT(_root,13);
    // AVLINSERT(_root,5);
    // AVLINSERT(_root,56);
    // AVLINSERT(_root,45);
    // AVLINSERT(_root,3);
    // AVLINSERT(_root,5);
    // AVLINSERT(_root,545);
    // AVLINSERT(_root,54);
    // AVLINSERT(_root,6);
    // // cout<<AVLMIN(_root)->key<<" "<<AVLMIN(_root)->_cnt<<" "<<AVLMIN(_root)->sub_tree_size<<endl;

    // AVLREMOVE(_root,13);
    // // cout<<AVLMIN(_root)->key<<" "<<AVLMIN(_root)->_cnt<<" "<<AVLMIN(_root)->sub_tree_size<<endl;
    // AVLREMOVE(_root,13);

    // // cout<<AVLMIN(_root)->key<<" "<<AVLMIN(_root)->_cnt<<" "<<AVLMIN(_root)->sub_tree_size<<endl;
    
    // AVLREMOVE(_root,14);

    // AVLINSERT(_root,87);
    // AVLINSERT(_root,90);
    // AVLINSERT(_root,1);
    // AVLINSERT(_root,142);
    // AVLINSERT(_root,12);
    // AVLINSERT(_root,300);

    // AVLREMOVE(_root,45);
    for(int i=0;i<128;i++){
      AVLINSERT(_root,i);
    }

    // cout<<AVLMIN(_root)->key<<" "<<AVLMIN(_root)->_cnt<<" "<<AVLMIN(_root)->sub_tree_size<<endl;
    cout<<"head"<<_root->key<<" "<<_root->_cnt<<" "<<_root->sub_tree_size<<" "<<_root->_bf<<endl;
    
    // cout<<AVLMIN(_root)->key<<" "<<AVLMIN(_root)->_cnt<<" "<<AVLMIN(_root)->sub_tree_size<<endl;
    midTraverse(_root);
    // cout<<"[[[[[[[[[[[[[[[[[[[[["<<endl;

    // AVLINSERT(_root,54);
    // midTraverse(_root);
    // cout<<"======================="<<endl;
    // // // cout<<func(_root,5)<<endl;
    // for(int i=0;i<7;i++){
    //   AVLREMOVE(_root,i);
    // }

    // midTraverse(_root);
    // cout<<AVLRANGECNTSUM(_root,13,500)<<endl;
    // cout<<AVLRANGECNTSUM(_root,3,56);
    system("pause");
	return 0;
}