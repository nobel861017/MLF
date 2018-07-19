//decision_stump_algorithm.cpp
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <algorithm>
#include <time.h>
using namespace std;
struct TUPLE_2{
	double x;
	int y;
};
typedef struct h{
	int s;
	double theta;
} H;

int sign(double x){
	if(x > 0) return 1;
	else return -1;
}

int neg(int y){ return -y; }

void Generate_Data(TUPLE_2 *Data){
	for(int i = 0; i < 20; i++){
		TUPLE_2 cor;
		cor.x = 2.0 * rand() / (double)RAND_MAX - 1.0;
		cor.y = sign(cor.x);
		Data[i] = cor;
	}
}

void Noise(TUPLE_2 *Data){
	for(int i = 0; i < 20; i++){
		double x = rand() / (double)RAND_MAX;
		if(x < 0.2) Data[i].y = neg(Data[i].y);
	}
}

int cmp(const void *a, const void *b){
	TUPLE_2 *A = (TUPLE_2 *)a;
	TUPLE_2 *B = (TUPLE_2 *)b;
	return B->x < A->x;
}

double cal_error(TUPLE_2 *Data, H &h){
	int error_num = 0;
	for(int i = 0; i < 20; i++) if(h.s*sign(Data[i].x - h.theta) != Data[i].y) error_num++;
	return error_num/20.0;
}

double E_in(TUPLE_2 *Data,H &min_h){
	double error_rate_min = 1.0;
	H h;
	memset(&h, 0, sizeof(H));
	for(int i = 0; i <= 20; i++){
		h.s = 1;
		if(i == 0) h.theta = Data[0].x - 1.0;
		else if(i == 20) h.theta = Data[19].x + 1.0;
		else h.theta = (Data[i-1].x + Data[i].x) / 2.0;
		double err_rate = cal_error(Data,h);
		if(err_rate < error_rate_min){
			min_h = h;
			error_rate_min = err_rate;
		}
	}
	for(int i = 0; i <= 20; i++){
		h.s = -1;
		if(i == 0) h.theta = Data[0].x - 1.0;
		else if(i == 20) h.theta = Data[19].x + 1.0;
		else h.theta = (Data[i-1].x + Data[i].x) / 2.0;
		double err_rate = cal_error(Data,h);
		if(err_rate < error_rate_min){
			min_h = h;
			error_rate_min = err_rate;
		}
	}
	//printf("s = %d, theta = %lf\n", min_h->s, min_h->theta);
	return error_rate_min;
}

double E_out(H &h){
	//printf("s = %d, theta = %lf\n", h->s, h->theta);
	return 0.5 + 0.3*(double)h.s*(double)(fabs(h.theta) - 1.0);
}

bool Compare( TUPLE_2 a, TUPLE_2 b ){
	return a.x < b.x;
}

int main(){
	FILE *fp1 = fopen("E_in","w+");
	FILE *fp2 = fopen("E_out","w+");
	//int seed[5000];
	int flag = 0;
	double E_in_rate_sum = 0.0, E_out_rate_sum = 0.0;
	srand(time(NULL));
	//for(int i = 0; i < 1000; i++) seed[i] = rand();
	for(int i = 0; i < 1000; i++){
		//srand(seed[i]);
	    TUPLE_2 Data[20];
	    Generate_Data(Data);
	    Noise(Data);
	    /*if(!flag){
		    for(int j=0;j<20;j++)
		    	printf("%lf ",Data[j].x);
		   	puts("");
	    }*/
	    //qsort(Data, 20, sizeof(TUPLE_2), cmp);
	    sort(Data,Data+20,Compare);
	    /*if(!flag){
		    for(int j=0;j<20;j++)
		    	printf("%lf ",Data[j].x);
		    puts("");
	    }
		flag = 1;*/
		H min_h;
		memset(&min_h, 0, sizeof(H));
        double error_rate_min = E_in(Data,min_h);
        double e_out = E_out(min_h);
        //printf("s = %d, theta = %lf\n", min_h.s, min_h.theta);
        if(i != 999){
        	fprintf(fp1, "%lf ", error_rate_min);
        	fprintf(fp2, "%lf ", e_out);
        }
        else{
        	fprintf(fp1, "%lf\n", error_rate_min);
        	fprintf(fp2, "%lf\n", e_out);
        }
	    printf("mininum E_in: %f\n", error_rate_min);
		E_in_rate_sum += error_rate_min;
		E_out_rate_sum += e_out;
		printf("E_out: %f\n", e_out);
	}
	printf("average E_in: %f\n", E_in_rate_sum / 1000);
	printf("E_out: %f\n", E_out_rate_sum / 1000);
	fclose(fp1);
	fclose(fp2);
	return 0;
}