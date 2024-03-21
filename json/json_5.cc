#include <iostream>

#include <nlohmann/json.hpp>

using njson = nlohmann::json;

struct Widget {
    int num;
    std::string name;
};

void to_json(njson &j, const Widget &widget)
{
    j = njson{
        { "num", widget.num },
        { "name", widget.name }
    };
}

int main()
{
    njson test_0 = { };
    test_0.emplace_back();
    std::cout << test_0.dump(4) << std::endl;

    njson test_1 = { 0, 1, 2, 3 };
    test_1.emplace_back(4);
    std::cout << test_1.dump(4) << std::endl;

    njson test_2 = { };
    test_2.emplace_back(0);
    std::cout << test_2.dump(4) << std::endl;

    Widget widget_0 = { 0, "zero" };
    Widget widget_1 = { 1, "one" };
    Widget widget_2 = { 2, "two" };
    Widget widget_3 = { 3, "three" };

    njson widget_list_json {};

    njson widget_0_json { widget_0 };
    njson widget_1_json { widget_1 };
    njson widget_2_json { widget_2 };
    njson widget_3_json { widget_3 };

    widget_list_json.emplace_back(widget_0);
    widget_list_json.emplace_back(widget_1);
    widget_list_json.emplace_back(widget_2);
    widget_list_json.emplace_back(widget_3);

    std::cout << widget_list_json.dump(4) << std::endl;

    return 0;
}
