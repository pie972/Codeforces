#include<iostream>
#include<cstdlib>
using namespace std;

int main(){
    int n;
    char* hard= "HARD";
    char* easy= "EASY";
    cin>>n;
    for(int i=0;i<n;i++){
        int c;
        cin>>c;
        if(c==1){
            cout<<hard;
            exit(0);
        }
    }
    cout<<easy;
    return 0;
}