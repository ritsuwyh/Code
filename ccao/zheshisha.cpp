#include <iostream>
using namespace std;
class node
{
    int value=1;
    
    node* parent=nullptr,*left=nullptr,*right=nullptr;
    /* data */
    
public:
    node(int _value,node* _parent=nullptr){
        value=_value;
        parent=_parent;
    }
    void insert(int _value){
        if (_value>=value){
            if (right){
                right->insert(_value);
            }else{
                right =new node(_value,this);
            }
        }else{
            if (left){
                left->insert(_value);
            }else{
                left =new node(_value,this);
            }
        }
    }
    void remove(int _value){
        if (_value==value){
            
        }else if (_value>value){
            if (right){
                right->remove(_value);
            }else{
                right =new node(_value,this);
            }
        }else{
            if (left){
                left->insert(_value);
            }else{
                left =new node(_value,this);
            }
        }
    }
};
node* root=new node(0,nullptr);

void func(node* &root){
    //root=x;


    node *q=new node;
    root->parent->x=1312312;
    cout<<q->x;
    // node *q=new node;
    // q->parent=p;
    // p->next=q;
    // q->x=101;
    // p=p->next;
    // p->x=11111;
    // root=root->next;




    // root->next=xx;
    // xx->parent=root;

    // xx=xx->next;
    // cout<<"woc"<<xx->x<<endl;
   
}
int main(){
    node *p=new node;

    root->parent=p;
    func(root);
    cout<<root->parent->x;
    // node* xx=new node;
    // xx->x=131;
    // func(root,xx);
    // cout<<root->x;
    // cout<<endl;
    // cout<<root->next->x;
    // cout<<endl;
    // cout<<xx->parent->x;
    system("pause");
    return 0;
}
