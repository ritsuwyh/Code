#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <ctime>

using namespace std;
struct TreapNod  { //node declaration
   long long data;
   int priority;
   int cnt;
   long long subtreesize;
   TreapNod* l, *r;
   TreapNod(long long d) { //constructor
      this->data = d;
      this->priority = rand();
      this->cnt=1;
      this->subtreesize=d;
      this->l= this->r = nullptr;
   }
};

int flag=0;
TreapNod* _root = nullptr;

void rotLeft(TreapNod* &root) { //left rotation

   TreapNod* R = root->r;
   TreapNod* X = root->r->l;
   R->l = root;
   root->r= X;

   R->subtreesize=root->subtreesize;
   root->subtreesize=(root->data) *(root->cnt);
   if(root->l){
       root->subtreesize+=root->l->subtreesize;
   }
   if(root->r){
       root->subtreesize+=root->r->subtreesize;
   }

   root = R;
}
void rotRight(TreapNod* &root) { //right rotation
   TreapNod* L = root->l;
   TreapNod* Y = root->l->r;
   L->r = root;
   root->l= Y;

   L->subtreesize=root->subtreesize;
   root->subtreesize=(root->data)*(root->cnt);
   if(root->l){
       root->subtreesize+=root->l->subtreesize;
   }
   if(root->r){
       root->subtreesize+=root->r->subtreesize;
   }
   root = L;
}

void insertNod(TreapNod* &root, long long d) { //insertion
   if (root == nullptr) {
      root = new TreapNod(d);
      return;
   }
   if (d == root->data){
       root->cnt++;
       root->subtreesize+=d;
       return;
   }
   if (d < root->data) {
    root->subtreesize+=d;
    insertNod(root->l, d);
    if (root->l != nullptr && root->l->priority > root->priority){
        // root->subtreesize+=d;
        rotRight(root);
    }
   } else {
    root->subtreesize+=d;
    insertNod(root->r, d);
    if (root->r!= nullptr && root->r->priority > root->priority){
        // root->subtreesize+=d;
        rotLeft(root);
    }
   }
}

// int searchNod(TreapNod* root, int key) {
//    if (root == nullptr)
//       return 0;
//    if (root->data == key)
//       return root->cnt;
//    if (key < root->data)
//       return searchNod(root->l, key);

//     return searchNod(root->r, key);
// }
void deletemaintain(long long key){
    TreapNod* p=_root;
    while(p->data!=key){
        p->subtreesize-=key;
        if(key<p->data){
            p=p->l;
        }else{
            p=p->r;
        }
    }
    flag=p->cnt;
    p->cnt--;
    p->subtreesize-=key;

}
//不能随便用指针和引用,这里是递归所以用的引用，要不然根节点就变了
void deleteNod(TreapNod* &root, long long key) {
   //node to be deleted which is a leaf node
   if (root == nullptr){
       flag=0;
      return;
      }
   if (key < root->data){
        //root->subtreesize-=key;
        deleteNod(root->l, key);
        }
   else if (key > root->data){
       //root->subtreesize-=key;
      deleteNod(root->r, key);
      }
      //node to be deleted which has two children
    else {


    if(root->cnt==0){//说明删除的这个节点不存在
        flag=0;
        return;
    }
    deletemaintain(key);

    }
}
long long func(TreapNod* root,long long upbound){
  long long ans=0;
  TreapNod* p=root;
  while(p!=nullptr){

    if(p->data<upbound){
      if(p->l!=nullptr){
      ans+=p->l->subtreesize+p->cnt*p->data;
      }else{
        ans+=p->cnt*p->data;
      }
      p=p->r;

    }else if(p->data==upbound){
      if(p->l!=nullptr){
        ans+=p->l->subtreesize+p->cnt*p->data;
      }else{
        ans+=p->cnt*p->data;
      }
      return ans;
    }else{
      p=p->l;
    }

  }
  return ans;
}
long long rangesum(TreapNod* root,long long lowerbound,long long upperbound){
  return func(root,upperbound) - func(root,lowerbound);
}

int main(){

srand(time(nullptr));
  long long q,p;
  cin>>q>>p;
  int lans=0;
  for(int i=0;i<q;i++){
    int option;
    cin>>option;
    if(option==0){
      long long x;
      cin>>x;
      insertNod(_root,(x+lans)%p);

    }else if(option==1){
      long long x;
      cin>>x;
      deleteNod(_root,(x+lans)%p);
      cout<<flag<<endl;
      flag=0;

    }else{
      long long l,r;
      cin>>l>>r;
      l=(lans+l)%p;
      r=(lans+r)%p;
      if(l>r){
        swap(l,r);
      }
      long long temp=rangesum(_root,l,r);
      cout<<temp<<endl;
      lans=temp;
    }

  }
    return 0;
}
