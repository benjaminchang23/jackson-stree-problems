#include <stdint.h>
#include <string.h>

void ReadWidget(uint8_t *buffer1, uint8_t *buffer2, uint16_t size)
{
    memcpy(buffer2, buffer1, size);
}

void WriteWidget(uint64_t address, uint8_t *buffer, uint16_t size)
{
    memcpy(&address, buffer, size);
}

int main()
{
    uint8_t readbuf1[5];
    uint8_t readbuf2[5];

    // copy buf 1 to buf 2
    ReadWidget(readbuf2, readbuf1, sizeof(readbuf2));

    return 0;
}