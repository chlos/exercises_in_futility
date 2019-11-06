#include <iostream>
#include <vector>
#include <algorithm>


int main()
{
    unsigned long long n_errors, error_no;
    std::vector<unsigned long long> diff(1);
    std::cin >> n_errors;

    std::vector<unsigned long long> errors_orig;
    for (unsigned long long i = 0; i < n_errors; ++i) {
        if (std::cin >> error_no)
            errors_orig.push_back(error_no);
    }
    std::sort(errors_orig.begin(), errors_orig.end());

    std::vector<unsigned long long> errors_fix_1;
    for (unsigned long long i = 0; i < n_errors - 1; ++i) {
        if (std::cin >> error_no)
            errors_fix_1.push_back(error_no);
    }
    std::sort(errors_fix_1.begin(), errors_fix_1.end());
    std::set_difference(
        errors_orig.begin(), errors_orig.end(),
        errors_fix_1.begin(), errors_fix_1.end(),
        diff.begin()
    );
    std::cout << diff.back() << "\n";

    std::vector<unsigned long long> errors_fix_2;
    for (unsigned long long i = 0; i < n_errors - 2; ++i) {
        if (std::cin >> error_no)
            errors_fix_2.push_back(error_no);
    }
    std::sort(errors_fix_2.begin(), errors_fix_2.end());
    std::set_difference(
        errors_fix_1.begin(), errors_fix_1.end(),
        errors_fix_2.begin(), errors_fix_2.end(),
        diff.begin()
    );
    std::cout << diff.back() << "\n";
}
