include(GNUInstallDirs)

add_executable(spdlog_0 spdlog_0.cc)
add_executable(spdlog_1 spdlog_1.cc)
add_executable(spdlog_2 spdlog_2.cc)

target_link_libraries(spdlog_0 PRIVATE spdlog::spdlog)
target_link_libraries(spdlog_1 PRIVATE spdlog::spdlog)
target_link_libraries(spdlog_2 PRIVATE spdlog::spdlog)

install(TARGETS
    spdlog_0
    spdlog_1
    spdlog_2
    RUNTIME DESTINATION bin
    )

set_target_properties(spdlog_0 PROPERTIES INSTALL_RPATH
    "$LD_LIBRARY_PATH;${CMAKE_INSTALL_PREFIX}/lib")
set_target_properties(spdlog_1 PROPERTIES INSTALL_RPATH
    "$LD_LIBRARY_PATH;${CMAKE_INSTALL_PREFIX}/lib")
set_target_properties(spdlog_2 PROPERTIES INSTALL_RPATH
    "$LD_LIBRARY_PATH;${CMAKE_INSTALL_PREFIX}/lib")