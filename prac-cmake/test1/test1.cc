#include <iostream>

#include <test1.h>
#include <test2.h>

void do_test_1()
{
    std::cout << "do test 1" << std::endl;

    do_test_2();

    return;
}