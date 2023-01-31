#include <iostream>

enum class MyEnum : uint8_t
{
    FIRST,
    SECOND,
    THIRD,

    _NUM_ENUMS
};

int main()
{
    std::cout << static_cast<int>(MyEnum::FIRST) << std::endl;
    std::cout << static_cast<int>(MyEnum::SECOND) << std::endl;
    std::cout << static_cast<int>(MyEnum::THIRD) << std::endl;

    auto foo = static_cast<int>(MyEnum::SECOND) + static_cast<int>(MyEnum::THIRD);

    std::cout << "foo: " << foo << std::endl;

    return 0;
}