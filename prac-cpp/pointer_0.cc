#include <iostream>
#include <string.h>

void GetInt(uint8_t *m_int)
{
    uint8_t new_int[8];
    *new_int = 101;

    memcpy(m_int, new_int, 8);
}

int main()
{
    uint8_t m_int[8];

    GetInt(m_int);

    std::cout << +m_int[0] << std::endl;

    return 0;
}
