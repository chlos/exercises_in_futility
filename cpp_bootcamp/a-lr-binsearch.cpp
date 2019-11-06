#include <iostream>
#include <vector>

using namespace std;

int bin_search(vector<int>& vect, int vect_len, int val) {
    int left = 0, right = vect_len - 1, mid;
    while (left <= right) {
        mid = left + (right - left) / 2;
        if (vect.at(mid) == val)
            return mid;
        else if (vect.at(mid) > val)
            right = mid - 1;
        else
            left = mid + 1;
    }
    return -1;
}

void find_borders(vector<int>& vect, int vect_len, int found_first, int& left, int& right) {
    bool left_is_found = false, right_is_found = false;
    left = found_first;
    right = found_first;

    while (0 < left && !left_is_found) {
        if (vect.at(left - 1) == vect.at(left))
            --left;
        else
            left_is_found = true;
    }

    while (right < vect_len - 1 && !right_is_found) {
        if (vect.at(right + 1) == vect.at(right))
            ++right;
        else
            right_is_found = true;
    }
}

int main() {
    int x;
    int n_m_len = 2;
    vector<int> n_m;
    for (int i = 0; i < n_m_len; ++i)
        if (cin >> x)
            n_m.push_back(x);
    int m_len = n_m.back();
    n_m.pop_back();
    int n_len = n_m.back();
    n_m.pop_back();

    vector<int> nv (n_len);
    for (int i = 0; i < n_len; ++i)
        if (cin >> x)
            nv.at(i) = x;

    vector<int> mv (m_len);
    for (int i = 0; i < m_len; ++i)
        if (cin >> x)
            mv.at(i) = x;

    int left_found, right_found, i_found;
    for (int i = 0; i < m_len; ++i) {
        i_found = bin_search(nv, n_len, mv.at(i));
        if (i_found >= 0) {
            find_borders(nv, n_len, i_found, left_found, right_found);
            cout << left_found + 1 << " " << right_found + 1 << endl;
        } else
            cout << 0 << endl;
    }

    return 0;
}
