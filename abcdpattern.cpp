/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <iostream>

using namespace std;

int main()
{
    int row=1;
    while(row<=4){
        int col=1;
        char ch=('A'+4-row);
        while(col<=row){
            cout<<ch;
            ch=ch+1;
            col=col+1;
        }
        cout<<endl;
        row=row+1;
    }
    return 0;
}