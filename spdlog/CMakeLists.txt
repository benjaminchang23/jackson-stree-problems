include(GNUInstallDirs)

add_executable(spdlog_0 spdlog_0.cc)
target_link_libraries(spdlog_0 PRIVATE spdlog::spdlog)

install(TARGETS
    spdlog_0
    RUNTIME DESTINATION bin
    )

set_target_properties(spdlog_0 PROPERTIES INSTALL_RPATH
    "$LD_LIBRARY_PATH;${CMAKE_INSTALL_PREFIX}/lib")