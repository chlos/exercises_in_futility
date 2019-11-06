#include <iostream>
#include <string>
#include <algorithm>


int get_n();

std::string get_input_chars(int n);

std::string get_palindrome(std::string chars);


int main()
{
    int n = get_n();
    if (n < 0) {
        std::cout << "Wrong N value";
        return -1;
    }
    std::string input_chars = get_input_chars(n);

    std::cout << get_palindrome(input_chars);
}

int get_n()
{
    int n;
    std::cin >> n;
    if (!std::cin.fail())
        return n;
    else
        return -1;
}

std::string get_input_chars(int n)
{
    std::string str("");
    std::cin >> str;
    return str;
}

std::string get_palindrome(std::string chars)
{
    std::string palindrome;
    if (chars.size() == 0)
        return palindrome;

    int char_count['Z' + 1] = {0};  // A...Z <=> 65...90
    for (unsigned long i = 0; i < chars.size(); ++i)
        ++char_count[(unsigned char)chars[i]];

    std::string left = "", mid = "", right = "";
    char ch = 'A';
    while (ch <= 'Z') {
        if (char_count[ch] % 2 != 0) {
            if (mid == "")
                mid = ch;
            --char_count[ch];
        } else {
            for (int i = 0; i < char_count[ch] / 2; ++i)
                right += ch;
            ch++;
        }
    }
    left = right;
    std::reverse(right.begin(), right.end());
    palindrome = left + mid + right;

    return palindrome;
}
