#include <iostream>
#include <vector>


int main()
{
    long n, x;
    std::cin >> n;
    std::vector<long long> a, f(n, 1);
    for (long i = 0; i < n; ++i) {
        std::cin >> x;
        a.push_back(x);
    }

    long max_len, max_len_result (0);
    for (long i = 0; i < n; ++i) {
        max_len = 1;
        for (long j = 0; j < i; ++j) {
            if (a[i] > a[j] && f[j] > max_len) {
                max_len = f[j];
            }
        }
        f[i] = max_len + 1;

        if (max_len > max_len_result)
            max_len_result = max_len;
    }

    std::cout << max_len_result << "\n";
}
