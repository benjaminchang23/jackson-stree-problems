#include <iostream>
#include <iterator>
#include <sstream>
#include <string>
#include <vector>


int main()
{
    // int t, n;
    // uint32_t a_start, a_end, b_start, b_end;
    // std::cout << "input number of tests" << std::endl;
    // std::cin >> t; // read t. cin knows that t is an int, so it reads it as such.
    // std::cout << "number of tests: " << t << std::endl;
    // for (int i = 1; i <= t; ++i) {
    //     std::cout << "input number of stacks" << std::endl;
    //     std::cin >> n; // read num of stacks
    //     std::vector<uint64_t> pancakes(n);
    //     std::cout << "pancake stacks: " << n << std::endl;
        
    //     // read stack counts
    //     std::cout << "input stacks" << std::endl;

    //     uint64_t pstack = 0;
    //     for (int i = 0; i < n; ++i)
    //     {
    //         std::cin >> pstack;
    //         pancakes[i] = pstack;
    //     }

    //     // read in start and end
    //     std::cout << "input start and end" << std::endl;
    //     std::cin >> a_start >> a_end >> b_start >> b_end;
    //     std::cout << "start and end: " << a_start << " " << a_end << " " << b_start << " " << b_end << std::endl;
    // std::vector<int> pancakes = {30, 50, 40, 20, 10};
    // std::vector<int> pancakes = {20, 20, 80, 10, 10};
    // std::vector<int> pancakes = {90, 10, 10, 10};
    // std::vector<int> pancakes = {20, 5, 20, 80, 15, 10};
    std::vector<int> pancakes = {200, 200};

    // for (const auto & pancake : pancakes)
    // for (size_t i = 0; i < pancakes.size(); ++i)
    // {
    //     std::cout << pancakes[i] << std::endl;
    // }

    // std::cout << "end pancakes" << std::endl;

    uint32_t a_start = 1;
    uint32_t a_end = 3;
    uint32_t b_start = 1;
    uint32_t b_end = 3;

    // uint32_t a_start = 1;
    // uint32_t a_end = 4;
    // uint32_t b_start = 2;
    // uint32_t b_end = 5;

    // uint32_t a_start = 1;
    // uint32_t a_end = 4;
    // uint32_t b_start = 1;
    // uint32_t b_end = 4;

    // uint32_t a_start = 1;
    // uint32_t a_end = 6;
    // uint32_t b_start = 1;
    // uint32_t b_end = 4;

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
        // for (size_t i = 0; i < pancake_memo_lr.size(); ++i)
        // {
        //     std::cout << "pmem lr" << pancake_memo_lr[i] << std::endl;
        // }

        std::vector<uint64_t> pancake_memo_rl(pancakes.size());
        pancake_memo_rl[pancake_memo_rl.size() - 1] = pancakes[pancakes.size() - 1];
        for (size_t i = pancakes.size() - 1; i-- > 0; )
        {
            pancake_memo_rl[i] = pancakes[i] + pancake_memo_rl[i + 1];
        }
        // for (size_t i = 0; i < pancake_memo_rl.size(); ++i)
        // {
        //     std::cout << "pmem rl" << pancake_memo_rl[i] << std::endl;
        // }

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
        std::cout << "max pancake check: " << max_pancake_check << std::endl;
    }
    // }

    

    return 0;
}