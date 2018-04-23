#include <stdio.h>
#include <stdlib.h>

int row,col;
float f[10000][10000]; // DONT KNOW HOW TO FIX THIS!!
void getFloatInFile(char* filename);

void setUp(char* filename, int row_i, int col_i) {
  row = row_i;
  col = col_i;
  getFloatInFile(filename);

}

void getFloatInFile(char* filename) {
  FILE *fp;
  if((fp=fopen(filename, "r"))==NULL)
   return;

  fseek(fp, 0, SEEK_END);
  long size = ftell(fp);
  fseek(fp, 0, SEEK_SET);

  fread(f, sizeof(float), size, fp);

  fclose(fp);
}

int count = 0;
int hasNext() {
  if(count!= (row*col) + 1) {
    return 1;
  }
  return 0;
}

float next() {
  if(!hasNext()) {
    printf("You did not call hasNext()");
  }
  float data = f[count/row][count%col];
  count++;
  return data;
}
