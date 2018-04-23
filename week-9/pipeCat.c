
#include <unistd.h> 
#include <stdio.h>

int main(int argc, char *argv[]) { 

    if( argc == 2 ) {
        execlp ("cat", "cat" , argv[1] , 0);
    }

    execlp ("cat", "cat" , "4300.txt" , 0); 
}