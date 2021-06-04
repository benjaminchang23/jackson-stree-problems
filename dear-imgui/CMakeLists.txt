add_executable(dear_imgui_0 dear_imgui_0.cc)
target_link_libraries(dear_imgui_0 dearimguiadapter)

set_target_properties(dear_imgui_0 PROPERTIES INSTALL_RPATH
    "$LD_LIBRARY_PATH;${CMAKE_INSTALL_PREFIX}/lib")

install(
    TARGETS
    dear_imgui_0
    RUNTIME DESTINATION bin)