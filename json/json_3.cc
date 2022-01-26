#include <fstream>
#include <iostream>

#include <nlohmann/json.hpp>

using njson = nlohmann::json;

int main()
{
    std::ifstream i("practice_1.json");
    njson root_json;
    i >> root_json;

    auto target_key_0 = "config_version";
    if (!root_json.contains(target_key_0))
    {
        std::cout << "error: missing key: " << target_key_0 << std::endl;
        return -1;
    }
    std::cout << "key: " << target_key_0 << " - value: " << root_json[target_key_0] << std::endl;

    njson config = root_json["config"];

    auto target_key_1 = "db_debug_log";
    if (!config.contains(target_key_1))
    {
        std::cout << "error: missing key: " << target_key_1 << std::endl;
        return -1;
    }
    std::cout << "key: " << target_key_1 << " - value: " << config[target_key_1] << std::endl;

    return 0;
}