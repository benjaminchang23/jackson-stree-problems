#include <chrono>
#include <iostream>
#include <queue>
#include <random>
#include <vector>

int main()
{
    int num_books, reading_time;
    std::cin >> num_books >> reading_time; // read number of books and total reading time

    std::vector<int> book_list;
    book_list.reserve(num_books);

    std::random_device rd;
    std::mt19937_64::result_type seed = rd() ^ (
            (std::mt19937_64::result_type)
            std::chrono::duration_cast<std::chrono::seconds>(
                std::chrono::system_clock::now().time_since_epoch()
                ).count() +
            (std::mt19937_64::result_type)
            std::chrono::duration_cast<std::chrono::microseconds>(
                std::chrono::high_resolution_clock::now().time_since_epoch()
                ).count() );

    std::mt19937_64 gen = std::mt19937_64(seed);
    std::uniform_int_distribution<int> dist = std::uniform_int_distribution<int>(1, 10000);

    for (int i = 0; i < num_books; ++i)
    {
        int book_time = dist(gen);
        book_list.emplace_back(book_time);
    }

    std::priority_queue<int, std::vector<int>, std::greater<int>> book_queue(book_list.begin(), book_list.end());

    int count = 0;
    bool reached_limit = false;

    while (!book_queue.empty() && !reached_limit)
    {
        int book_time = book_queue.top();
        book_queue.pop();

        reading_time-=book_time;

        if (reading_time >= 0)
        {
            ++count;
        }
        else
        {
            reached_limit = true;
        }
    }

    std::cout << count << std::endl;

    return 0;
}