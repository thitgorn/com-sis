#include <stdio.h>
#include <stdlib.h>

float f[1000][1000];

void getFloatInFile(char* filename, int row , int col , float f[row][col]) {
  FILE *fp;
  if((fp=fopen(filename, "r"))==NULL)
   return;

  fseek(fp, 0, SEEK_END);
  long size = ftell(fp);
  fseek(fp, 0, SEEK_SET);

  fread(f, sizeof(float), size, fp);

  fclose(fp);
}

void multiplication(char* filename , int row , int col) {
  getFloatInFile(filename, row, col, f);
  for(int i = 0 ; i < row ; i++)
  {
    for(int j = 0 ; j < col ; j++)
    {
      float z = f[i][j];
      printf("%f \n",  z*z);
    }
  }
}
