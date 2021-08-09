#include "spdlog/sinks/basic_file_sink.h"
int main()
{
    try 
    {
        auto logger = spdlog::basic_logger_mt("basic_logger", "logs/basic-log.txt");
    }
    catch (const spdlog::spdlog_ex &ex)
    {
        std::cout << "Log init failed: " << ex.what() << std::endl;
    }

    return 0;
}