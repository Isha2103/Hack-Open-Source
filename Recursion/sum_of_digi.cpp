#include<iostream>
using namespace std;
int sum_digi(int n,int sum)
{
    if(n<10)
        return sum+n;

    return sum_digi(n/10,(n%10)+sum);

    
}  //tail recursive

int main(int argc,char* argv[])
{
    int  n;
    cin>>n;
    cout<<sum_digi(n,0);

       
 
    
}