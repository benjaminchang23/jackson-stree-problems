#include <fstream>
#include <iostream>

#include <nlohmann/json.hpp>

using njson = nlohmann::json;

int main()
{
    // store a string in a JSON value
    njson j_string = "this is a string";

    // retrieve the string value
    auto cpp_string = j_string.get<std::string>();
    // retrieve the string value (alternative when a variable already exists)
    std::string cpp_string2;
    j_string.get_to(cpp_string2);

    // retrieve the serialized value (explicit JSON serialization)
    std::string serialized_string = j_string.dump();

    // output of original string
    std::cout << cpp_string << " == " << cpp_string2 << " == " << j_string.get<std::string>() << '\n';
    // output of serialized value
    std::cout << j_string << " == " << serialized_string << std::endl;

    std::cout << "input json: " << std::endl;

    // deserialize from standard input
    njson j;
    std::cin >> j;

    // serialize to standard output
    std::cout << j;

    // the setw manipulator was overloaded to set the indentation for pretty printing
    std::cout << std::setw(4) << j << std::endl;

    // read a JSON file
    std::ifstream i("practice_1.json");
    njson j2;
    i >> j2;

    // write prettified JSON to another file
    std::ofstream o("pretty.json");
    o << std::setw(4) << j2 << std::endl;

    return 0;
}