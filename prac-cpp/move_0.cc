#include <iostream>
#include <vector>

template <typename T>
void Swap(T &a, T &b)
{
    T temp(std::move(a));
    a = std::move(b);
    b = std::move(temp);
}

template <typename T>
void PrintVector(const std::vector<T> &vec)
{
    for (auto element : vec)
    {
        std::cout << element << " ";
    }
    std::cout << std::endl;
}

int main ()
{
    auto vector_0 = std::vector<int>({0, 1, 2});
    std::vector<int> vector_1({3, 4});

    PrintVector(vector_0);
    PrintVector(vector_1);

    Swap(vector_0, vector_1);

    PrintVector(vector_0);
    PrintVector(vector_1);
}