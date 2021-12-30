#include <iostream>

template <typename X>
std::string Printer(X x)
{
    std::cout << x << std::endl;
}

int main()
{
    Printer("log");
    Printer(5.5);

    return 0;
}
