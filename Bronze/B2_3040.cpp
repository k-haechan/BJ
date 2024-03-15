# 백설 공주와 일곱 난쟁이, 2023년 6월 19일 20:52:06, 2024kb, 0ms, 965b
#include <bits/stdc++.h>
using namespace std;

int n[9];

void solve1() {
    for(int i=0;i<9;i++) {
        cin>>n[i];
    }
    sort(n, n+9);

    do {
        int sum=0;
        for(int i=0;i<7;i++) {
            sum+=n[i];
            if(sum==100) {
                for(int j=0;j<7;j++)
                    cout<<n[j]<<'\n';
                exit(0);
            }
               
        }
    } while(next_permutation(n,n+9));
}

void c(int start, int nn, int r, vector<int> v) {
    if(v.size()==r) {
        int sum=0;
        for(int i : v) sum+=n[i];
        if(sum == 100) {
            for(int i : v) cout<< n[i]<<'\n'; 
            exit(0);
        }
        return ;
    }

    for(int i=start+1;i<nn;i++) {
        v.push_back(i);
        c(i,nn,r,v);
        v.pop_back();
    }
}


void solve2() {
    for(int i=0;i<9;i++) {
        cin>>n[i];
    }
    sort(n, n+9);
    vector<int> v;
    c(-1,9,7,v);

}
int main()
{
    solve2();
    return 0;
}
