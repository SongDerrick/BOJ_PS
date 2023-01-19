#include <iostream>
int numOfCows(int N,int W,int H,int L){
    int maxW = W / L;
    int maxH = H / L;
    if(maxW*maxH > N){
        return N;
    }
    else {
        return maxW*maxH;
    }
};
  
int main() {
  
int n,w,h,l;
  
scanf("%d %d %d %d", &n, &w, &h, &l);
printf("%d", numOfCows(n,w,h,l));

}