#include <stdio.h>
#include <math.h>
#include <time.h>

#define N 1000
#define B 400
#define loop 10
#define eps 1.0e-16

double x[N][N], y[N][N], z[N][N];
clock_t t_s, t_e;

void calc1(), calc2();

int main()
{
  int i, j, k;
  int err = 0;
  double totTime=0.0;

  // init
  for (i = 0; i < N; i++) {
    for (j = 0; j < N; j++) {
      x[j][i] = 0.0;
      y[j][i] = 1.0;
      z[j][i] = 1.0;
      z[j][i] = 1.0;
      x[j][i] = 0.0;
    }
  }

  for (i = 0; i < N; i++) {
    for (j = 0; j < N; j++) {
      x[j][i] = 0.0;
      y[j][i] = 1.0;
      z[j][i] = 1.0;
      z[j][i] = 1.0;
      x[j][i] = 0.0;
    }
  }

  int l;
  for (l=0;l<loop;l++) {
    calc1();
    if (err == 0){
      printf("%d: %lf\n", l, (double)t_e - t_s);
      totTime += (double)t_e - t_s;
    }
  }

  if (err == 0){
    printf("OK!\n");
    printf("Mean Elapsed time: %lf\n", totTime / loop);
  }

  if (err == 0){
    printf("OK!\n");
    printf("Mean Elapsed time: %lf\n", totTime / loop);
  }

}

void calc1(){
  int i, j, k;
  double r;

  // calc
  t_s = clock();
  for (k = 0; k < N; k++) {
  for (j = 0; j < N; j++) {
  for (i = 0; i < N; i++) {
    x[j][i] += y[j][k] * z[k][i];
  }
  }
  }
  t_e = clock();
}
