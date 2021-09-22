#include <spdlog/spdlog.h>
#include <spdlog/sinks/basic_file_sink.h>
#include <spdlog/sinks/stdout_color_sinks.h>

// create logger with 2 targets with different log levels and formats.
// the console will show only warnings or errors, while the file will log all.
int main()
{
    auto console_sink = std::make_shared<spdlog::sinks::stdout_color_sink_mt>();
    console_sink->set_level(spdlog::level::warn);
    // console_sink->set_pattern("[multi_sink_example] [%^%l%$] %v");

    auto file_sink = std::make_shared<spdlog::sinks::basic_file_sink_mt>("logs/multisink.txt", true);
    file_sink->set_level(spdlog::level::trace);

    const auto logger_name = "multi_sink";

    spdlog::logger logger(logger_name, {console_sink, file_sink});
    logger.set_level(spdlog::level::trace);
    spdlog::register_logger(std::make_shared<spdlog::logger>(logger));
    logger.warn("this should appear in both console and file");
    logger.info("this message should not appear in the console, only in the file as info");
    logger.debug("this message should not appear in the console, only in the file as debug");
    logger.trace("this message should not appear in the console, only in the file as trace");

    auto logger_0 = spdlog::get(logger_name);

    if (!logger_0)
        logger.error("logger {} does not exist", logger_name);
    else
        logger.info("Access successful");

    return 0;
}