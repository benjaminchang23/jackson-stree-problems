cmake_minimum_required(VERSION 3.5)

project(Parsers VERSION 0.1 LANGUAGES C CXX)

set(BUILD_SHARED_LIBS ON)

# add_compile_options(
# $<$<NOT:$<STREQUAL:$<TARGET_PROPERTY:SOURCE_DIR>,${PROJECT_SOURCE_DIR}/ext>>:-Wall>
# $<$<NOT:$<STREQUAL:$<TARGET_PROPERTY:SOURCE_DIR>,${PROJECT_SOURCE_DIR}/ext>>:-Wextra>
# $<$<NOT:$<STREQUAL:$<TARGET_PROPERTY:SOURCE_DIR>,${PROJECT_SOURCE_DIR}/ext>>:-Werror>
# )

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED TRUE)

add_subdirectory(ext)

add_subdirectory(codeforce)
add_subdirectory(dear-imgui)
add_subdirectory(effective-modern-cpp)
add_subdirectory(interview-questions)
add_subdirectory(prac-cpp)