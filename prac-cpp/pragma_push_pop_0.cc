#include <iostream>
#include <string>

#pragma pack(push, 1)
struct simple_repeated {
    uint8_t simple_int = 0;
};
#pragma pack(pop)

inline std::ostream& operator << (std::ostream &o, const simple_repeated &repeat)
{
    o << "simple_int: " << unsigned(repeat.simple_int);
    return o;
}

#pragma pack(push, 1)
struct simple_single {
    std::string name;
    simple_repeated repeat_0;
};
#pragma pack(pop)

inline std::ostream& operator << (std::ostream &o, const simple_single &single)
{
    o << "single: " << single.name << " ";
    o << "repeat_0: " << single.repeat_0;
    return o;
}

int main()
{
    simple_repeated repeat;
    simple_single first;
    repeat.simple_int = 1;
    first.name = "first";
    first.repeat_0 = repeat;

    simple_single second;
    second.name = "second";
    second.repeat_0.simple_int = 2;

    std::cout << first << std::endl;
    std::cout << second << std::endl;

    return 0;
}