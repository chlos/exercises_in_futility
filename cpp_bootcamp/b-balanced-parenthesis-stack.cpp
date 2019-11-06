#include <iostream>
#include <string>
#include <stack>


bool is_opening(char);

bool is_closing(char);

bool is_matching_pair(char, char);

bool is_string_balanced(std::string);

void print_result(bool);


int main()
{
    std::string str_to_check;
    std::cin >> str_to_check;
    bool is_balanced = is_string_balanced(str_to_check);
    print_result(is_balanced);
}


bool is_opening(char ch)
{
    if (ch == '(' || ch == '[' || ch == '{')
        return true;
    return false;
}


bool is_closing(char ch)
{
    if (ch == ')' || ch == ']' || ch == '}')
        return true;
    return false;
}


bool is_matching_pair(char opening, char closing)
{
    if (
            opening == '(' && closing == ')' ||
            opening == '[' && closing == ']' ||
            opening == '{' && closing == '}'
    )
        return true;
    return false;
}


bool is_string_balanced(std::string str_to_check)
{
    std::stack<char> st;
    char curr_ch;
    for (unsigned long i = 0; i < str_to_check.length(); ++i) {
        curr_ch = str_to_check[i];
        if (is_opening(curr_ch))
            st.push(curr_ch);
        if (is_closing(curr_ch)) {
            if (st.empty() || !is_matching_pair(st.top(), curr_ch))
                return false;
            else
                st.pop();
        }
    }

    return st.empty() ? true : false;
}


void print_result(bool ok)
{
    if (ok)
        std::cout << "yes";
    else
        std::cout << "no";
}
