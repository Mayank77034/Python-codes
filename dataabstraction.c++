#include<iostream>
using namespace std;
class car{
private :
bool startengine ;
public:
void start(){
    startengine = true ;
    cout<<"engine started";
    
}
void drive(){
    if(startengine){
        cout<<"you can drive ";
    }
    else{
        cout<<"you cannot drive unless car not start";
    }
}
};
int main(){
    car key;
    key.start();
    key.drive();
}