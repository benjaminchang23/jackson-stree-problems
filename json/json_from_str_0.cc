#include <iostream>

#include <nlohmann/json.hpp>

using njson = nlohmann::json;

struct Widget {
    int num;
    std::string name;
};

inline std::ostream& operator << (std::ostream &o, const Widget &widget)
{
    o << "num: " << widget.num << ", ";
    o << "name: " << widget.name;

    return o;
}

void from_json(const njson &j, Widget &widget)
{
    j.at("num").get_to(widget.num);
    j.at("name").get_to(widget.name);
}

void to_json(njson &j, const Widget &widget)
{
    j = njson{
        { "num", widget.num },
        { "name", widget.name }
    };
}

int main()
{
    std::string s1 = "[\"nlohmann\", \"json\"]";
    std::string s2 = "{\"nlohmann\": \"json\", \"foo\": 1, \"bar\": 1}";

    try
    {
        njson first = njson::parse(s1);
        njson second = njson::parse(s2);

        if (second.contains("bar"))
        {
            size_t bar_val = second["bar"];
            std::cout << "I see bar as: " << bar_val << std::endl;
        }

        std::cout << first.dump() << std::endl;
        std::cout << second.dump() << std::endl;
    }
    catch(const std::exception& e)
    {
        std::cerr << e.what() << '\n';
    }

    return 0;
}
