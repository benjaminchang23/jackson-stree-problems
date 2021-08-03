#include <algorithm>
#include <iostream>
#include <string>

int main()
{
    std::string sanatized_file_name = "---adf--[]as * df-k----";
    const std::string unallowed = " /\\*?<>:;=[]!@|.";

    while (sanatized_file_name.front() == '-')
    {
        sanatized_file_name.erase(sanatized_file_name.begin());
    }

    while (sanatized_file_name.back() == '-' && sanatized_file_name.size() > 0)
    {
        sanatized_file_name.pop_back();
    }

    std::transform(sanatized_file_name.begin(), sanatized_file_name.end(), sanatized_file_name.begin(),
    [&unallowed](char ch)
    {
        return (std::find(unallowed.begin(), unallowed.end(), ch) != unallowed.end()) ? '-' : ch;
    });

    std::cout << "after 1st replace: " << sanatized_file_name << std::endl;

    size_t pos = sanatized_file_name.find("--");

    while (pos != std::string::npos)
    {
        sanatized_file_name.replace(pos, 2, "-");
        pos = sanatized_file_name.find("--");
    }

    std::cout << "after 2nd replace: " << sanatized_file_name << std::endl;

    return 0;
}