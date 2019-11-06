#include <iostream>
#include <queue>

int main()
{
    long long n, b;
    std::cin >> n;
    std::cin >> b;

    long long t, d;
    std::queue<long long> req_in_times_t, req_handling_times_d;
    for (long long i = 0; i < n; ++i) {
        std::cin >> t;
        std::cin >> d;
        req_in_times_t.push(t);
        req_handling_times_d.push(d);
    }

    long long t_when_server_unblocked(req_in_times_t.front());
    std::queue<long long> req_waiting;
    while (!req_in_times_t.empty() || !req_handling_times_d.empty() || !req_waiting.empty()) {
        if (!req_in_times_t.empty() && !req_handling_times_d.empty()) {
            t = req_in_times_t.front();
            d = req_handling_times_d.front();
            req_in_times_t.pop();
            req_handling_times_d.pop();
        } else
            t = -1;

        if (!req_waiting.empty())
            while ((t >= t_when_server_unblocked || t == -1) && !req_waiting.empty()) {
                t_when_server_unblocked = req_waiting.front();
                req_waiting.pop();
            }

        if (t == -1)
            break;
        else if (t >= t_when_server_unblocked && req_waiting.empty()) {
            t_when_server_unblocked = t + d;
            std::cout << t_when_server_unblocked << "\n";
        } else if (req_waiting.size() < (size_t)b) {
            long long curr_req_finish_time;
            if (req_waiting.empty())
                curr_req_finish_time = t_when_server_unblocked + d;
            else
                curr_req_finish_time = req_waiting.back() + d;
            req_waiting.push(curr_req_finish_time);
            std::cout << curr_req_finish_time << "\n";
        }
        else
            std::cout << "-1" << "\n";
    }
}
