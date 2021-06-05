include(GNUInstallDirs)

# add_subdirectory(glfw)

# set root to be expected imgui location
set(imgui_root ${CMAKE_CURRENT_SOURCE_DIR}/imgui)

add_library(dearimguiadapter
    ${imgui_root}/imgui.h
    ${imgui_root}/imgui.cpp
    ${imgui_root}/imgui_demo.cpp
    ${imgui_root}/imgui_draw.cpp
    ${imgui_root}/imgui_tables.cpp
    ${imgui_root}/imgui_widgets.cpp

    ${imgui_root}/backends/imgui_impl_glfw.h
    ${imgui_root}/backends/imgui_impl_opengl3.h
    )

target_include_directories(dearimguiadapter PUBLIC ${imgui_root})

install(
  TARGETS dearimguiadapter 
  LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
  RUNTIME DESTINATION ${CMAKE_INSTALL_LIBDIR}
)

set_target_properties(dearimguiadapter PROPERTIES INSTALL_RPATH
    "$LD_LIBRARY_PATH;${CMAKE_INSTALL_PREFIX}/lib")