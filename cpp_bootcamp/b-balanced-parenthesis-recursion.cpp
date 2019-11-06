#include <iostream>
#include <string>
#include <stack>


bool is_opening(char);

bool is_closing(char);

bool is_matching_pair(char, char);

bool is_string_balanced(std::string);

bool is_string_balanced_rec(std::string str_to_check, char current_char, unsigned long current_index);

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


bool is_string_balanced_rec(std::string str_to_check, char prev_char, unsigned long curr_index)
{
    char curr_char = str_to_check[curr_index];
    std::cout << std::endl;
    std::cout << "===== prev_char: " << prev_char << std::endl;
    std::cout << "===== curr_char: " << curr_char << std::endl;
    std::cout << "===== curr_index: " << curr_index << std::endl;
    while (curr_index < str_to_check.length()) {
        ++curr_index;

        if (is_opening(curr_char)) {
            std::cout << curr_char << " is opening" << std::endl;
            if (!is_string_balanced_rec(str_to_check, curr_char, curr_index))
                std::cout << "string not balanced" <<  std::endl;
                return false;
        }
        std::cout << "foo" << std::endl;

        if (is_closing(curr_char)) {
            std::cout << curr_char << "is closing" << std::endl;
            if (is_matching_pair(prev_char, curr_char)) {
                std::cout << prev_char << " " << curr_char << " matching pair" << std::endl;
                return true;
            }
            else
                std::cout << prev_char << " " << curr_char << " NOT matching pair" << std::endl;
                return false;
        }
    }

    std::cout << "OK" << std::endl;
    return true;
    //return prev_char == 0;
}

bool is_string_balanced(std::string str_to_check)
{
    return is_string_balanced_rec(str_to_check, 0, 0);
    //std::stack<char> st;
    //char curr_ch;
    //for (unsigned long i = 0; i < str_to_check.length(); ++i) {
        //curr_ch = str_to_check[i];
        //if (is_opening(curr_ch))
            //st.push(curr_ch);
        //if (is_closing(curr_ch)) {
            //if (st.empty() || !is_matching_pair(st.top(), curr_ch))
                //return false;
            //else
                //st.pop();
        //}
    //}

    //return st.empty() ? true : false;
}


void print_result(bool ok)
{
    if (ok)
        std::cout << "yes";
    else
        std::cout << "no";
}
