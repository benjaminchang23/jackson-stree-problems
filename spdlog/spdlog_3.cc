#include <iostream>

#include "spdlog/spdlog.h"
#include "spdlog/sinks/stdout_color_sinks.h"

int main()
{
    // create color multi threaded logger
    // auto console = spdlog::stdout_color_mt("console");
    auto err_logger = spdlog::stderr_color_mt("stderr");

    auto console_logger = spdlog::get("console");

    if (!console_logger)
    {
        std::cerr << "logger is null" << std::endl;
    }

    return 0;
}