cmake_minimum_required(VERSION 3.5)

project(Parsers VERSION 0.1 LANGUAGES C CXX)

set(BUILD_SHARED_LIBS ON)

add_compile_options(-Wall -Wextra -Werror)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED TRUE)

add_subdirectory(ext)

add_subdirectory(codeforce)
# add_subdirectory(cpp-httplib)
add_subdirectory(dear-imgui)
add_subdirectory(effective-modern-cpp)
add_subdirectory(interview-questions)
add_subdirectory(json)
add_subdirectory(prac-cmake)
add_subdirectory(prac-cpp)
add_subdirectory(spdlog)