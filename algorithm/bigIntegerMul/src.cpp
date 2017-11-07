#include <iostream>
#include <vector>
using namespace std;
/*
 * 来源：滴滴
 * 大数乘法a * b
 * 假设a, b均逆序
 * c[i+j] = a[i] * b[j]
 * 接下来处理c的进位
 * 最后把c倒过来
 */

void print(vector<int> &a) {
    for (auto c: a) {
        cout<<c;
    }
    cout<<endl;
}
vector<int> bigIntegerMul(vector<int> &a, vector<int> &b) {
    int len_a = a.size();
    int len_b = b.size();
    vector<int> ans(len_a + len_b, 0);
    for (int i=len_a-1;i>=0;i--) {
        int ii = len_a - 1 - i;
        for (int j=len_b-1;j>=0;j--) {
            int jj = len_b - 1 - j;
            ans[ii+jj] += a[ii] * b[jj];
        }
    }
    print(ans);
    int len_ans = len_a + len_b;
    int c = 0;
    for (int i=0;i<len_ans;i++) {
        int remain = (ans[i] + c) % 10;
        c  = (ans[i] + c) / 10;
        ans[i] = remain;
    }
    if (ans[len_ans-1] == 0) {
        len_ans --;
        ans.pop_back();
    }
    int l = 0;
    int r = len_ans-1;
    while (l<r) {
        int tmp = ans[l];
        ans[l] = ans[r];
        ans[r] = tmp;
        l ++;
        r --;
    }
    return ans;
}
int main(){
    vector<int> a = {9,9};
    vector<int> b = {9,9};
    vector<int> ans = bigIntegerMul(a, b);
    print(a);
    print(b);
    print(ans);
    return 0;
}
