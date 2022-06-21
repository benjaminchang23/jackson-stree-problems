include(GNUInstallDirs)

add_library(test1
    test1.cc
    test2.cc
)

target_include_directories(test1 PUBLIC ${PROJECT_SOURCE_DIR}/prac-cmake/test2)
message(STATUS "test2 include dir: ${PROJECT_SOURCE_DIR}/prac-cmake/test2")
target_link_libraries(test1 test4)

install(
  TARGETS test1
  LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
  RUNTIME DESTINATION ${CMAKE_INSTALL_LIBDIR}
)

set_target_properties(test1 PROPERTIES INSTALL_RPATH
    "$LD_LIBRARY_PATH:${CMAKE_INSTALL_PREFIX}/lib")

add_executable(do_test_driver do_test_driver.cc)
target_link_libraries(do_test_driver test1)

set_target_properties(do_test_driver PROPERTIES INSTALL_RPATH
    "$LD_LIBRARY_PATH:${CMAKE_INSTALL_PREFIX}/lib")

install(TARGETS do_test_driver RUNTIME DESTINATION bin)
