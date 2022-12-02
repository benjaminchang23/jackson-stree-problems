#include <iostream>
#include <string>

void prefix_compare(const std::string &compare, const std::string &target)
{
    if (!compare.compare(0, target.size(), target))
    {
        std::cout << compare << " and " << target << " match" << std::endl;
    }
    else
    {
        std::cout << compare << " and " << target << " do not match" << std::endl;
    }
}

int main()
{
    std::string str1 ("message message--post hasThreadmark  js-post js-inlineModContainer   ");
    std::string str2 ("message message--post hasThreadmark  js-post js-inlineModContainer   nf-gifted");
    std::string str3 ("abc");
    std::string str4 ("ab");

    prefix_compare(str1, str2);
    prefix_compare(str2, str1);
    prefix_compare(str1, str1);

    prefix_compare(str3, str4);
    prefix_compare(str4, str3);
    prefix_compare(str3, str3);

    return 0;
}