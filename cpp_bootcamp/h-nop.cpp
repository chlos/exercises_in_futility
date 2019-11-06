#include <iostream>
#include <vector>
#include <algorithm>


int main()
{
    long long n, m, x;
    std::vector<long long> seq_n, seq_m;
    std::cin >> n;
    for (size_t i = 0; i < n; ++i) {
        std::cin >> x;
        seq_n.push_back(x);
    }
    std::cin >> m;
    for (size_t i = 0; i < m; ++i) {
        std::cin >> x;
        seq_m.push_back(x);
    }

    std::vector< std::vector<long long> > d(n + 1, std::vector<long long> (m + 1, 0));
    for (size_t i = 0; i <= n; ++i) {
        for (size_t j = 0; j <= m; ++j) {
            if (i == 0 || j == 0)
                d[i][j] = 0;
            else if (seq_n[i - 1] == seq_m[j - 1])
                d[i][j] = d[i - 1][j - 1] + 1;
            else
                d[i][j] = std::max(d[i - 1][j], d[i][j - 1]);
        }
    }

    std::cout << d[n][m] << "\n";
}
