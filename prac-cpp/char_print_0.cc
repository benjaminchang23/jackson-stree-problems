#include <stdio.h>
#include <string.h>

#include <iostream>

int main()
{
    char dest_0[9];
    char dest_1[9];
    const char test_0[] = "test_123456789";

    std::cout << "dest_0: " << dest_0 << std::endl;
    strncpy(dest_0, test_0, sizeof(dest_0));
    printf("dest_0 strncpy printf style: %s\n", dest_0);
    std::cout << "dest_0: " << dest_0 << std::endl;

    std::cout << "dest_1: " << dest_1 << std::endl;
    snprintf(dest_1, sizeof(dest_1), "%s", test_0);
    printf("dest_1 snprintf printf style: %s\n", dest_1);
    std::cout << "dest_1: " << dest_1 << std::endl;

    return 0;
}