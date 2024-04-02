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
    std::string s = "[\"nlohmann\", \"json\"]";
    njson second = njson::parse(s);
    std::cout << second.dump() << std::endl;
    njson test_0 = { };

    return 0;
}
