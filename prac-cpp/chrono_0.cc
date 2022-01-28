#include <chrono>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <thread>

int main()
{
    int seconds_counter = 0;

    auto now_time = std::chrono::steady_clock::now();
    auto freq = now_time;

    while (seconds_counter <= 15)
    {
        now_time = std::chrono::steady_clock::now();
        const auto deadline = now_time + std::chrono::milliseconds(1000);

        std::cout << (freq - now_time).count() << std::endl;

        if ((freq-now_time).count() < 0)
        {
            std::stringstream str;
            std::cout << "run timed widget" << std::endl;
            freq = std::chrono::steady_clock::now() + std::chrono::seconds(5);
            auto next_time = std::chrono::system_clock::now() + std::chrono::seconds(5);
            auto time = std::chrono::system_clock::to_time_t(next_time);
            str << std::put_time(std::gmtime(&time), "%FT%TZ") << std::ends;
            std::cout << "next run at " << str.str() << std::endl;
        }

        ++seconds_counter;

        std::this_thread::sleep_until(deadline);
    }


    return 0;
}