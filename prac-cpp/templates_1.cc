#include <iostream>

template <typename T>
T SimpleSum(T a, T b)
{
    return a + b;
}

template <typename T>
T SimpleMultiply(T a, T b)
{
    return a * b;
}

template <typename T, int I>
T FixedMultiply(T num)
{
    return num * I;
}

int main ()
{
    int i = 5;
    int j = 10;
    double a = 5.0;
    double b = 11.3;
    std::cout << SimpleSum(i, j) << std::endl;
    std::cout << SimpleSum(a, b) << std::endl;

    std::cout << SimpleMultiply(i, j) << std::endl;
    std::cout << SimpleMultiply(a, b) << std::endl;

    std::cout << FixedMultiply<int, 3>(10) << std::endl;

    return 0;
}