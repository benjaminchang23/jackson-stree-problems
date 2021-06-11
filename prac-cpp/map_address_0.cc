#include <iostream>
#include <unordered_map>

int main()
{
    std::unordered_map<std::string, uint8_t> map;

    map.emplace("one", 1);
    map.emplace("two", 2);

    auto num = map.find("one");

    if (num != map.end())
    {
        std::cout << num->first << num->second << std::endl;
    }
}