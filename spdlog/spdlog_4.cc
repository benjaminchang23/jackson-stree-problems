#include "spdlog/spdlog.h"
#include "spdlog/sinks/rotating_file_sink.h"

int main()
{
    // Create a file rotating logger with 5mb size max and 3 rotated files
    auto max_size = 1048576 * 5;
    auto max_files = 3;
    const auto logger_name = "some_logger_name";
    const auto log_name = "logs/rotating.txt";
    auto logger = spdlog::rotating_logger_mt(logger_name, log_name, max_size, max_files);
    logger->info("Start logger with name {} at {}", logger_name, log_name);
    spdlog::get("some_logger_name")->info("loggers can be retrieved from a global registry using the spdlog::get(logger_name)");

    return 0;
}