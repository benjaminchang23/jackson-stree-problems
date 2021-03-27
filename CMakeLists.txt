cmake_minimum_required(VERSION 3.5)

project(Parsers VERSION 0.1 LANGUAGES C CXX)

set(BUILD_SHARED_LIBS ON)

add_compile_options(-Wall -Wextra -Werror)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED TRUE)

add_executable(codeforce-279-b codeforce-279-b.cc)

install(TARGETS codeforce-279-b RUNTIME DESTINATION bin)
