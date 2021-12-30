#include <iostream>

template <typename X, typename Y>
int Multiply(X x, Y y)
{
    return x * y;
}

int main()
{
    std::cout << Multiply(11, 2) << std::endl;
    std::cout << Multiply(3, 20) << std::endl;

    return 0;
}