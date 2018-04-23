
#include <unistd.h> 
#include <stdio.h>
int main(int argc, char *argv[]) { 
int fda[2]; 

if ( pipe(fda) < 0 ) printf("create pipe failed\n"); 
 switch ( fork() ) {   
      case -1 : printf("fork failed\n"); 
      case 0: 
       close (1); 
       dup ( fda[1] ); 
       close ( fda[1] );
       close ( fda[0] ); 
       printf("in child\n"); 
       execlp ("./mycat", "./mycat" , argv[1] , 0);
       printf ("failed to exec mycat\n");
       break;
      default: 
       close (0);
       dup (fda[0] ); 
       close ( fda[0] );
       close (fda[1] ); 
       execlp ("grep", "grep" , argv[2] , 0);
       printf ("failed to execute grep\n");
       break;
      } 
 }