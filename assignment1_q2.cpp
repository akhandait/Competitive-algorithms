#include <iostream>
using namespace std;

char L[] = {'D', 'E', 'Y', 'N', 'R', 'O', 'S', 'M'};
int seq[] = {6, 1, 3, 0, 7, 5, 4, 2};
int l = 8;
double t;

bool Satisfies(int C[]) {
    return (1000*(C[6] + C[7]) + 100*(C[1] + C[5]) + 10*(C[3] + C[4]) + C[0] + C[1] == 10000*C[7] + 
    1000*C[5] + 100*C[3] + 10*C[1] + C[2]);
}
void search(int y[], int k) {
	if (k == l) {
		if (Satisfies(y)) {
			for (int i = 0; i < l; i++) cout << L[seq[i]] << '=' << y[seq[i]] << endl; 
		}
	    return;
	}
	else {
		for (int i = 0; i < 10; i++) {
			for (int j = 0; j < k; j++) {
				if (i == y[j]) {
					goto cnt;
				}
			}
			y[k] = i;
			if (k == 2) {
			    if ((y[0] + y[1]) % 10 != y[2]) goto cnt;
			}
			else if (k == 4) {
				if (((y[0] + y[1]) / 10 + y[3] + y[4]) % 10 != y[1]) goto cnt;
			}
			else if (k == 5) {
				if ((y[3]*10+y[0]+y[4]*10+y[1]+y[1]*100+y[5]*100)%1000!=(y[1]*10+y[2]+y[3]*100)) goto cnt;
			}

			search(y, k+1);
			cnt:;
		}
	}
}

int main() {
	clock_t start, end;
	int y[l];
	start = clock();
    search(y, 0);
    end = clock();
    t = ((double)(end - start)) / CLOCKS_PER_SEC;
    cout << "Time taken = " << t << " seconds" << endl;
}