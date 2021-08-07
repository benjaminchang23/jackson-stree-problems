find_package(spdlog REQUIRED)

add_executable(spdlog_0 spdlog_0.cc)
target_link_libraries(spdlog_0 PRIVATE spdlog::spdlog)

install(TARGETS
    spdlog_0
    )