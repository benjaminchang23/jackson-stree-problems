// based on https://stackoverflow.com/questions/14373934/iterator-loop-vs-index-loop
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

/*
Advantages: familiar to anyone familiar with C-style code, can loop using different strides (e.g. i += 2).

Disadvantages: only for sequential random access containers (vector, array, deque), doesn't work for list, forward_list or the associative containers. Also the loop control is a little verbose (init, check, increment). People need to be aware of the 0-based indexing in C++.
*/

void IndexBased(const std::vector<std::string> &vec)
{
    std::cout << "index based" << std::endl;

    for (std::size_t i = 0; i != vec.size(); ++i)
    {
        std::cout << vec[i] << std::endl;

        // any code including continue, break, return
    }

    std::cout << std::endl;
}

/*
Advantages: more generic, works for all containers (even the new unordered associative containers, can also use different strides (e.g. std::advance(it, 2));

Disadvantages: need extra work to get the index of the current element (could be O(N) for list or forward_list). Again, the loop control is a little verbose (init, check, increment). 
*/

void IteratorBased(const std::vector<std::string> &vec)
{
    std::cout << "iterator based" << std::endl;

    for (auto it = vec.begin(); it != vec.end(); ++it)
    {
        const auto ind = std::distance(vec.begin(), it);

        std::cout << ind << " - " << *it << std::endl;

        // any code including continue, break, return
    }

    std::cout << std::endl;
}

/*
Advantages: same as 2) plus small reduction in loop control (no check and increment), this can greatly reduce your bug rate (wrong init, check or increment, off-by-one errors).

Disadvantages: same as explicit iterator-loop plus restricted possibilities for flow control in the loop (cannot use continue, break or return) and no option for different strides (unless you use an iterator adapter that overloads operator++).
*/
void StlWithLambda(const std::vector<std::string> &vec)
{
    std::cout << "stl with lambda based" << std::endl;

    std::for_each(vec.begin(), vec.end(), [vec](const std::string &elem) {
        auto ind = &elem - &vec[0];

        std::cout << ind << " - " << &elem << " - " << &vec[0] << " - " << elem << std::endl;

        // cannot continue, break or return out of the loop
    });

    std::cout << std::endl;
}

/*
Advantages: very compact loop control, direct access to the current element.

Disadvantages: extra statement to get the index. Cannot use different strides.
*/

void RangeBased(const std::vector<std::string> &vec)
{
    std::cout << "range based" << std::endl;

    for (const auto & elem : vec) {
        auto ind = &elem - &vec[0];

        std::cout << ind << " - " << elem << std::endl;

        // any code including continue, break, return
    }

    std::cout << std::endl;
}

int main()
{
    std::vector<std::string> vec;

    vec.emplace_back("foo");
    vec.emplace_back("bar");
    vec.emplace_back("vac");

    IndexBased(vec);
    IteratorBased(vec);
    StlWithLambda(vec);
    RangeBased(vec);

    return 0;
}