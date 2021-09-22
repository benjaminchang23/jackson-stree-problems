include(GNUInstallDirs)

add_executable(spdlog_0 spdlog_0.cc)
add_executable(spdlog_1 spdlog_1.cc)
add_executable(spdlog_2 spdlog_2.cc)
add_executable(spdlog_3 spdlog_3.cc)
add_executable(spdlog_4 spdlog_4.cc)
add_executable(spdlog_5 spdlog_5.cc)

target_link_libraries(spdlog_0 PRIVATE spdlog::spdlog)
target_link_libraries(spdlog_1 PRIVATE spdlog::spdlog)
target_link_libraries(spdlog_2 PRIVATE spdlog::spdlog)
target_link_libraries(spdlog_3 PRIVATE spdlog::spdlog)
target_link_libraries(spdlog_4 PRIVATE spdlog::spdlog)
target_link_libraries(spdlog_5 PRIVATE spdlog::spdlog)

install(TARGETS
    spdlog_0
    spdlog_1
    spdlog_2
    spdlog_3
    spdlog_4
    spdlog_5
    RUNTIME DESTINATION bin
    )

set_target_properties(spdlog_0 PROPERTIES INSTALL_RPATH
    "$LD_LIBRARY_PATH;${CMAKE_INSTALL_PREFIX}/lib")
set_target_properties(spdlog_1 PROPERTIES INSTALL_RPATH
    "$LD_LIBRARY_PATH;${CMAKE_INSTALL_PREFIX}/lib")
set_target_properties(spdlog_2 PROPERTIES INSTALL_RPATH
    "$LD_LIBRARY_PATH;${CMAKE_INSTALL_PREFIX}/lib")
set_target_properties(spdlog_3 PROPERTIES INSTALL_RPATH
    "$LD_LIBRARY_PATH;${CMAKE_INSTALL_PREFIX}/lib")
set_target_properties(spdlog_4 PROPERTIES INSTALL_RPATH
    "$LD_LIBRARY_PATH;${CMAKE_INSTALL_PREFIX}/lib")
set_target_properties(spdlog_5 PROPERTIES INSTALL_RPATH
    "$LD_LIBRARY_PATH;${CMAKE_INSTALL_PREFIX}/lib")