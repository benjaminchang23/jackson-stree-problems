#include <ctime>
#include <iomanip>
#include <iostream>
#include <string>
#include <sstream>

std::time_t ParseTimet(const std::string &input, const std::string &format)
{
    struct tm tm_l {
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    };
    strptime(input.c_str(), format.c_str(), &tm_l);
    return mktime(&tm_l);
}

std::string GetEasyString(const std::time_t &time)
{
    std::stringstream str;
    str << std::put_time(std::gmtime(&time), "%F %H:%M") << std::ends;
    return str.str();
}

std::string GetISOString(const std::time_t &time)
{
    std::stringstream str;
    str << std::put_time(std::gmtime(&time), "%FT%TZ") << std::ends;
    return str.str();
}

int main()
{
    std::time_t result = std::time(nullptr);
    std::cout << std::asctime(std::localtime(&result)) << result << " seconds since the Epoch" << std::endl;
    std::cout << "ISO: " << GetISOString(result) << std::endl;
    std::cout << "Easy: " << GetEasyString(result) << std::endl;

    auto parser = ParseTimet("Wednesday, April 18, 2018 7:57 AM", "%A, %B %d, %Y %I:%M %p");
    std::cout << "ISO: " << GetISOString(parser) << std::endl;
    std::cout << "Easy: " << GetEasyString(parser) << std::endl;
}
