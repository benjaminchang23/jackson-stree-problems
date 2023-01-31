#include <iostream>

int main()
{
    bool set_0 = true;
    bool set_1 = false;

    std::string str_0 = set_0 ? "true" : "false";
    std::string str_1 = set_1 ? "true" : "false";

    std::cout << "str_0: " << str_0 << std::endl;
    std::cout << "str_1: " << str_1 << std::endl;

    return 0;
}