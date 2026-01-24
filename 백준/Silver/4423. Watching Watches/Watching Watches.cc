#include <bits/stdc++.h>
#define fastio() ios::sync_with_stdio(0); cin.tie(0); cout.tie(0)
using namespace std;

void solve() {
    int k, m;
    while (cin >> k >> m) {
        double diff_per_day = abs(k - m);
        double days_to_sync = 43200.0 / diff_per_day;
        double total_seconds_moved = days_to_sync * (86400.0 - (double)k);
        double final_seconds = fmod(total_seconds_moved, 43200.0);
        int total_minutes = (int)((final_seconds + 30.0) / 60.0);
        total_minutes %= 720;
        
        int hours = total_minutes / 60;
        int mins = total_minutes % 60;
        if (hours == 0) hours = 12;

        cout << k << " " << m << " " 
             << setfill('0') << setw(2) << hours << ":" 
             << setfill('0') << setw(2) << mins << "\n";
    }
}

int main() {
    fastio();
    solve();
    return 0;
}