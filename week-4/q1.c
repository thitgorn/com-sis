#include "stdio.h"
#include "stdlib.h"
#include "stdint.h"

float** op;
float res[1000][1000];
int row = 0;
int col = -1;
float** binaryToArray(){
  FILE * file = fopen("DATA1000.dat","r");
  op = malloc(sizeof(float*) * 1000);
  for(int i = 0;i<1000;i++){
    op[i] = malloc(sizeof(float*) * 1000);
  }
  int count = 0;
  for(int i = 0;i<1000;i++){
    for(int j = 0;j<1000;j++){
      float temp;
      fread(&temp, sizeof(float), 1, file);
      op[i][j] = temp;
    }
  }
  fclose(file);
  return op;
}

void multiMatrix(){
  for(int i =0;i<1000;i++){
    for(int j = 0;j<1000;j++){
      res[i][j] = 0;
      for(int k = 0;k<1000;k++){
        res[i][j] += op[i][k] * op[k][j];
      }
    }
  }
}

float nextMultiResult(){
  if(col == 1000){
    col = 0;
    row++;
  }
  col++;
  return res[row][col];
}

float nextBinaryArray(){
  if(col == 1000){
    col = 0;
    row++;
  }
  col++;
  return op[row][col];
}

int main(int argc, char const *argv[]) {
   // int count = 0;
   // float** temp = binaryToArray();
   // // printf("%f\n",temp[0][0] );
   // multiMatrix(temp);
   // printf("%f\n",res[0][1] );
   // // printf("%f\n",sqrl(5) );
}
