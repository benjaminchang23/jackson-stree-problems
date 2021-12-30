#include <stdio.h>
#include <string.h>

#include <iostream>

struct char_cont
{
    char data_0[16];
    char data_1[16];
};

inline std::ostream& operator << (std::ostream &o, const char_cont &con)
{
    o << std::string(con.data_0) << ",";
    o << con.data_1;
    return o;
}

int main()
{
    char_cont con_0;
    const auto test_0 = "test_123456789";
    const auto test_1 = "foobarwjj";

    std::cout << "sizeof(con_0.data_0): " << sizeof(con_0.data_0) << std::endl;
    std::cout << "strlen(con_0.data_0): " << strlen(con_0.data_0) << std::endl;
    std::cout << "sizeof(con_0.data_1): " << sizeof(con_0.data_1) << std::endl;
    std::cout << "strlen(con_0.data_1): " << strlen(con_0.data_1) << std::endl << std::endl;

    snprintf(con_0.data_0, sizeof(con_0.data_0), "%s", test_0);
    strncpy(con_0.data_1, test_1, sizeof(con_0.data_1));

    std::cout << "sizeof(con_0.data_0): " << sizeof(con_0.data_0) << std::endl;
    std::cout << "strlen(con_0.data_0): " << strlen(con_0.data_0) << std::endl;
    std::cout << "sizeof(con_0.data_1): " << sizeof(con_0.data_1) << std::endl;
    std::cout << "strlen(con_0.data_1): " << strlen(con_0.data_1) << std::endl << std::endl;

    std::cout << "con_0.data_0: " << con_0.data_0 << std::endl;
    std::cout << "con_0.data_1: " << con_0.data_1 << std::endl;
    std::cout << "con_0: " << con_0 << std::endl;

    return 0;
}