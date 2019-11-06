#include <iostream>


int main()
{
    unsigned n, m, a;
    std::cin >> n >> m >> a;

    unsigned long long x, x1, x2;
    if (a > 0) {
        x1 = (n + a - 1) / a;
        x2 = (m + a - 1) / a;
        x = x1 * x2;
        std::cout << x << std::endl;
    }
}
