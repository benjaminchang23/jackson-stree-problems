#include <iostream>

void WidgetFuntion(uint8_t num, char *buf1, char *buf2, size_t count)
{
    std::cout << +num << " - " << buf1[0] << " - " << buf2[0] << " - " << count << std::endl;
}

int main()
{
    const uint8_t buf1 = (300 & 0xff);
    uint8_t buf2 = 0x00;

    WidgetFuntion(1, (char *)&buf1, (char *)&buf2, sizeof(buf1));

    return 0;
}
