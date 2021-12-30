#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

bool ContainsUnprintable(const std::string &target_string)
{
    for (const auto & c : target_string)
    {
        if (!std::isprint(c))
            return true;
    }

    return false;
}

void RemoveUnprintable(std::string &target_string)
{
    target_string.erase(std::remove_if(target_string.begin(), target_string.end(),
        [](unsigned char c)
        {
            return !std::isprint(c);
        })
        , target_string.end());
}

int main()
{
    std::vector<std::string> strings;

    char random_0[90];
    char random_1[80];
    char random_2[70];

    strings.emplace_back(",A7AȮ� (invalid encoding)");
    strings.emplace_back(",A7AȮ� *(invalid encoding)");
    strings.emplace_back("test_1234test_123O���U,test_123O���U");
    strings.emplace_back("test_1234test_123��lV,test_123��lV");
    strings.emplace_back("test_1234test_1230R�U,test_1230R�U");
    strings.emplace_back("@K/�,test_123@K/�");

    strings.emplace_back(std::string(random_0));
    strings.emplace_back(std::string(random_1));
    strings.emplace_back(std::string(random_2));

    for (auto & str : strings)
    {
        std::cout << str << std::endl;
        std::cout << "contains unprintable: " << ContainsUnprintable(str) << std::endl;
        RemoveUnprintable(str);
        std::cout << str << std::endl;
        std::cout << "contains unprintable: " << ContainsUnprintable(str) << std::endl << std::endl;
    }

    return 0;
}