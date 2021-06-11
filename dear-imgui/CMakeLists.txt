add_executable(dear_imgui_0 dear_imgui_0.cc)
add_executable(dear_imgui_1 dear_imgui_1.cc)
target_link_libraries(dear_imgui_0 dearimguiadapter)
target_link_libraries(dear_imgui_1 dearimguiadapter)

set_target_properties(dear_imgui_0 PROPERTIES INSTALL_RPATH
    "$LD_LIBRARY_PATH;${CMAKE_INSTALL_PREFIX}/lib")
set_target_properties(dear_imgui_1 PROPERTIES INSTALL_RPATH
    "$LD_LIBRARY_PATH;${CMAKE_INSTALL_PREFIX}/lib")

install(
    TARGETS
    dear_imgui_0
    dear_imgui_1
    RUNTIME DESTINATION bin)