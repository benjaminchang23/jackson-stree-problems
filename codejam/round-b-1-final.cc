#include <iostream>
#include <iterator>
#include <sstream>
#include <string>
#include <vector>

int main()
{
    int t, n;
    uint32_t a_start, a_end, b_start, b_end;
    std::cin >> t; // read t. cin knows that t is an int, so it reads it as such.
    for (int i = 1; i <= t; ++i) {
        std::cin >> n; // read num of stacks
        std::vector<uint64_t> pancakes(n);
        
        // read stack counts
        uint64_t pstack = 0;
        for (int i = 0; i < n; ++i)
        {
            std::cin >> pstack;
            pancakes[i] = pstack;
        }

        // read in start and end
        std::cin >> a_start >> a_end >> b_start >> b_end;

        // check no overlap
        uint32_t a_target_start = 0;
        uint32_t a_target_end = 0;
        if (a_end <= b_start)
        {
            uint32_t diff = b_start - a_end;
            uint32_t num_index = diff/2 + (diff % 2);
            a_target_start = 0;
            a_target_end = a_end + num_index - 1;

            // sum pancakes
            uint64_t sum_pancakes = 0;
            for (size_t i = a_target_start; i <= a_target_end; ++i)
            {
                sum_pancakes += pancakes[i];
            }

            std::cout << sum_pancakes << std::endl;
            }
        else if (b_end <= a_start)
        {
            uint32_t diff = a_start - b_end;
            uint32_t num_index = diff/2 + (diff % 2);
            a_target_start = a_start - num_index - 1;
            a_target_end = pancakes.size() - 1;

            // sum pancakes
            uint64_t sum_pancakes = 0;
            for (size_t i = a_target_start; i <= a_target_end; ++i)
            {
                sum_pancakes += pancakes[i];
            }

            std::cout << sum_pancakes << std::endl;
        }
        // no overlap
        else
        {
            std::vector<uint64_t> pancake_memo_lr(pancakes.size());
            pancake_memo_lr[0] = pancakes[0];
            for (size_t i = 1; i < pancakes.size(); ++i)
            {
                pancake_memo_lr[i] = pancakes[i] + pancake_memo_lr[i - 1];
            }

            std::vector<uint64_t> pancake_memo_rl(pancakes.size());
            pancake_memo_rl[pancake_memo_rl.size() - 1] = pancakes[pancakes.size() - 1];
            for (size_t i = pancakes.size() - 1; i-- > 0; )
            {
                pancake_memo_rl[i] = pancakes[i] + pancake_memo_rl[i + 1];
            }

            uint64_t max_pancake_check = 0;
            for (size_t i = a_start - 1; i <= a_end - 1; ++i)
            {
                // get lowest memo
                uint64_t lowest = pancake_memo_lr[i];
                if (lowest > pancake_memo_rl[i])
                    lowest = pancake_memo_rl[i];
                
                if (lowest > max_pancake_check)
                    max_pancake_check = lowest;
            }
            std::cout << max_pancake_check << std::endl;
        }
    }

    

    return 0;
}