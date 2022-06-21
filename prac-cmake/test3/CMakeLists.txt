add_library(test4 test4/test4.cc)
target_include_directories(test4 PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/test4)
message(STATUS "test4 include dir: ${CMAKE_CURRENT_SOURCE_DIR}/test4")

install(
  TARGETS test4
  LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
  RUNTIME DESTINATION ${CMAKE_INSTALL_LIBDIR}
)

set_target_properties(test4 PROPERTIES INSTALL_RPATH
    "$LD_LIBRARY_PATH:${CMAKE_INSTALL_PREFIX}/lib")