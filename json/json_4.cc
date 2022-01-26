#include <fstream>
#include <iostream>

#include <nlohmann/json.hpp>

using njson = nlohmann::json;

struct black_library_config
{
    std::string version;
    std::string db_path = "/mnt/black-library/db/catalog.db";
    std::string logger_path = "/mnt/black-library/log/";
    std::string storage_path = "/mnt/black-library/store/";
    uint8_t manager_worker_count;
    bool binder_debug_log;
    bool cli_debug_log;
    bool db_debug_log;
    bool db_init_new;
    bool db_remote;
    bool factory_debug_log;
    bool main_app_debug_log;
    bool manager_debug_log;
    bool parser_debug_log;
    bool url_puller_debug;
    bool worker_debug_log;
};

inline std::ostream& operator << (std::ostream &o, const black_library_config &config)
{
    o << "version: " << config.version << " ";
    o << "db_path: " << config.db_path << " ";
    o << "logger_path: " << config.logger_path << " ";
    o << "storage_path: " << config.storage_path << " ";
    o << "manager_worker_count: " << config.manager_worker_count << " ";
    o << "binder_debug_log: " << config.binder_debug_log << " ";
    o << "cli_debug_log: " << config.cli_debug_log << " ";
    o << "db_debug_log: " << config.db_debug_log << " ";
    o << "db_init_new: " << config.db_init_new << " ";
    o << "db_remote: " << config.db_remote << " ";
    o << "factory_debug_log: " << config.factory_debug_log << " ";
    o << "main_app_debug_log: " << config.main_app_debug_log << " ";
    o << "manager_debug_log: " << config.manager_debug_log << " ";
    o << "parser_debug_log: " << config.parser_debug_log << " ";
    o << "url_puller_debug: " << config.url_puller_debug << " ";
    o << "worker_debug_log: " << config.worker_debug_log << " ";

    return o;
}

int GetConfig(char *filename)
{
    std::ifstream i(filename);
    njson root_json;
    i >> root_json;

    auto version_key = "config_version";
    if (!root_json.contains(version_key))
    {
        std::cout << "error: missing key: " << version_key << std::endl;
        return -1;
    }
    std::cout << "key: " << version_key << " - value: " << root_json[version_key] << std::endl;

    njson config = root_json["config"];

    std::vector<std::string> config_fields = {
        "binder_debug_log"
        , "cli_debug_log"
        , "db_debug_log"
        , "db_path"
        , "db_init_new"
        , "db_remote"
        , "factory_debug_log"
        , "logger_path"
        , "main_app_debug_log"
        , "manager_debug_log"
        , "parser_debug_log"
        , "storage_path"
        , "url_puller_debug"
        , "worker_debug_log"
        };

    auto target_key_1 = "db_debug_log";
    if (!config.contains(target_key_1))
    {
        std::cout << "error: missing key: " << target_key_1 << std::endl;
        return -1;
    }
    std::cout << "key: " << target_key_1 << " - value: " << config[target_key_1] << std::endl;
}

int main(int argc, char *argv[])
{
    if (argc != 2)
    { 
        std::cout << "Must specify the file" << std::endl;
        exit(-1);
    }

    std::cout << "Using file: " << argv[1] << std::endl;

    GetConfig(argv[1]);

    return 0;
}
