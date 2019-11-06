#include <iostream>
#include <string>

int main()
{
    std::string s;
    std::cin >> s;

    for (size_t i = 0; i < s.length(); ++i)
        if (s[i] == 'r')
            std::cout << i + 1 << "\n";
    for (long i = s.length() - 1; i >= 0; --i)
        if (s[i] == 'l')
            std::cout << i + 1 << "\n";
}
